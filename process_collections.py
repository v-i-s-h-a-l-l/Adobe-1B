import os
import json
from datetime import datetime
from collections import defaultdict
import pdfplumber
import torch
from sentence_transformers import SentenceTransformer, util

# Load the model from local folder (no internet!)
model_path = "./models/sentence-transformers/multi-qa-MiniLM-L6-cos-v1"
model = SentenceTransformer(model_path)

def extract_paragraphs(pdf_path):
    all_paragraphs = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            if not text:
                continue
            lines = text.split("\n")
            current_title, current_para = "", ""
            for line in lines:
                if line.isupper() or (len(line.split()) <= 6 and line == line.title()):
                    if current_para:
                        all_paragraphs.append({
                            "title": current_title,
                            "text": current_para.strip(),
                            "page_number": page_num
                        })
                        current_para = ""
                    current_title = line.strip()
                else:
                    current_para += " " + line
            if current_para:
                all_paragraphs.append({
                    "title": current_title,
                    "text": current_para.strip(),
                    "page_number": page_num
                })
    return all_paragraphs

def process_collection(collection_path):
    input_file = os.path.join(collection_path, "challenge1b_input.json")
    output_file = os.path.join(collection_path, "challenge1b_output.json")

    with open(input_file, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    persona = input_data["persona"]["role"]
    task = input_data["job_to_be_done"]["task"]
    documents = input_data["documents"]
    input_documents = [doc["filename"] for doc in documents]

    all_candidates = []
    for doc in input_documents:
        pdf_path = os.path.join(collection_path, "PDFs", doc)
        if not os.path.exists(pdf_path):
            print(f"[❌] Missing PDF: {pdf_path}")
            continue
        paras = extract_paragraphs(pdf_path)
        for para in paras:
            para["document"] = doc
            all_candidates.append(para)

    job_embedding = model.encode(task, convert_to_tensor=True)
    grouped_by_doc = defaultdict(list)
    for para in all_candidates:
        grouped_by_doc[para["document"]].append(para)

    selected_chunks = []
    for doc, paras in grouped_by_doc.items():
        texts = [p["text"] for p in paras]
        embeddings = model.encode(texts, convert_to_tensor=True)
        scores = util.cos_sim(job_embedding, embeddings)[0]
        best_idx = int(torch.argmax(scores))
        best_para = paras[best_idx]
        best_para["score"] = float(scores[best_idx])
        selected_chunks.append(best_para)

    selected_chunks = sorted(selected_chunks, key=lambda x: x["score"], reverse=True)

    extracted_sections = []
    subsection_analysis = []

    for rank, para in enumerate(selected_chunks, 1):
        extracted_sections.append({
            "document": para["document"],
            "section_title": para["title"],
            "importance_rank": rank,
            "page_number": para["page_number"]
        })
        subsection_analysis.append({
            "document": para["document"],
            "refined_text": para["text"],
            "page_number": para["page_number"]
        })

    output_json = {
        "metadata": {
            "input_documents": input_documents,
            "persona": persona,
            "job_to_be_done": task,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=2)

    print(f"[✅] Output written to {output_file}")

def main():
    base_dir = os.getcwd()
    for folder in os.listdir(base_dir):
        collection_path = os.path.join(base_dir, folder)
        if os.path.isdir(collection_path) and folder.startswith("Collection"):
            process_collection(collection_path)

if __name__ == "__main__":
    main()
