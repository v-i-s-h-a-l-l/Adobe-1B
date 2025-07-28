# DocuMind AI- ML Powered Document Outline Extractor

![WhatsApp Image 2025-07-27 at 23 02 43_6c90f94c](https://github.com/user-attachments/assets/e354f825-b22b-4b2d-a5ba-d08c25218396)
## 🧐 What is this?
DocuMind AI – Semantic PDF & Heading Extractor is an advanced document intelligence pipeline designed to simplify the processing and understanding of large, complex PDFs.

In this part it combines semantic search, heading detection, and structured output generation to help users — whether students, researchers, or professionals — extract meaningful content quickly based on a specified persona and job-to-be-done.
`output perfectly works with the ipynb file added in the repo`
## 👤who it is for?
- Students 
- Professional
- Researcher
- Developers
## ✨ Key Capabilities
- 🔍 Semantic Understanding — Automatically finds the most relevant section of each document by comparing content to user-defined tasks using a transformer-based model.

- 🧾 Heading Detection — Identifies and extracts structured headings and outlines to make navigation easier.

- 📦 Structured Output — Exports results in clean, machine-readable JSON format for downstream tasks like summarization, recommendation, or integration with AI systems.

Whether you're filtering through academic papers, technical manuals, travel guides, or multilingual reports, DocuMind AI turns document overload into actionable insight.

## 🗺️ Roadmap
![WhatsApp Image 2025-07-28 at 15 34 12_9bc718ff](https://github.com/user-attachments/assets/f9726335-d546-4f3c-8805-36dd7444a06d)


- Accepts one or more document collections, where each collection includes:

  -  A set of PDF files

  -  A JSON file describing the user persona and their job-to-be-done

- Performs intelligent processing by:

  -  Extracting and structuring text from PDFs into section-wise paragraphs

  -  Computing semantic similarity between the task description and document sections using a pre-trained transformer model (sentence-transformers/multi-qa-MiniLM-L6-cos-v1)

  - Selecting the most relevant section from each PDF based on semantic understanding

- Outputs a structured and usable result:

  -  The most semantically relevant paragraph per document

  -  Associated metadata:

      - Section title

      - Page number

      - Rank (relevance score)

      - Document ID / file name
### 👨‍🏫📉🤖 Ml model used
  The core model powering semantic understanding in this project is sentence-transformers/multi-qa-MiniLM-L6-cos-v1, a lightweight yet high-performance transformer fine-tuned for semantic search and question-answering tasks.

  `sentence-transformers/multi-qa-MiniLM-L6-cos-v1` from the Sentence-Transformers library
  <img width="271" height="186" alt="image" src="https://github.com/user-attachments/assets/2adb2af0-bbd6-4f28-ac15-92f08e1649ad" />

- Architecture Details:
    - Base: MiniLM (6 Transformer layers)

    - Hidden Size: 384

    - Transformer Layers: 6

    - Attention Heads: 12

    - Pooling Strategy: Mean pooling over token embeddings

    - Similarity Function: Cosine similarity

    - Fine-tuned On: Multi-domain QA datasets (e.g., MS       MARCO, Natural Questions, SQuAD, HotpotQA)

⚙️ How It Works:
- Text is tokenized and passed through the MiniLM encoder.

- Mean pooling is applied over the output token embeddings to get a fixed-size sentence embedding.

- These embeddings represent the semantic meaning of queries and document sections.

- Cosine similarity is used to compare the query with document sections.

- The highest-matching section(s) are selected based on similarity score.
### 📁 Folder Structure
![WhatsApp Image 2025-07-28 at 16 01 02_f1931a65](https://github.com/user-attachments/assets/d8cb5fc4-d1f4-43fa-a514-d7631d74c367)


###  Use Case Examples

-  **Travel Planning** — Extract top suggestions from multiple travel guides
-  **Enterprise Search** — Find policy-relevant sections in internal documents
-  **Educational Curation** — Select the best explanation from multiple tutorials
   **Recipe Recommendation** — Pull out the most relevant cooking tips for a given dietary goal

##  🛠️Setup instruction
1. Clone the Repository
  `git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name`

2. Build the Docker Image
    Make sure Docker Desktop is installed and running.

    Then build the image using:
      - `docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier` .
      -  mysolutionname can be your project name (e.g., pdf-title-extractor)
      -  somerandomidentifier can be a version tag (e.g., v1)

3. Prepare Input and Output Folders
   - Inside the root of the repo:
      `mkdir input`
      `mkdir output`
    - Put your test PDF files inside the input/ folder.
    - The model will write results to the output/ folder.

    - You can also use the sample PDFs from sample_dataset/pdfs/ by copying them:
      `cp sample_dataset/pdfs/*.pdf input/`
4. Run the Docker Container
    - On Linux/macOS or Git Bash:
`docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf-title-extractor:v1`
    -  On Windows PowerShell:
`docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output --network none pdf-title-extractor:v1`
5. View the Output
    - After the run finishes:
        -   Check the output/ folder.
        -   You should see the extracted headings or results in JSON or other format.

## Results:
### Performance metrics
![WhatsApp Image 2025-07-28 at 14 36 25_54e78812](https://github.com/user-attachments/assets/a24b0183-3c4a-47d2-b4ad-7482a78875e1)


### Input json 
<img width="789" height="355" alt="image" src="https://github.com/user-attachments/assets/23b318c2-76e5-4b18-961c-da4f6f1f6853" />


### Output json
<img width="807" height="589" alt="image" src="https://github.com/user-attachments/assets/751cb479-c4ec-4a03-a3ef-0a184b426c51" />


## Authors

- [@SHRIYAASK](https://github.com/SHRIYAASK)
- [@V-i-s-h-a-l](https://github.com/v-i-s-h-a-l-l)
- [@Allan-A1](https://github.com/Allan-A1)


