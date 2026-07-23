# ⚡ Content Automation Pipeline

> Batch-generates Twitter posts, LinkedIn content, email copies, 
> and blog titles from simple CSV input — powered by local LLM.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Ollama](https://img.shields.io/badge/Ollama-LLaMA3.1-green)
![Excel](https://img.shields.io/badge/Output-Excel-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

📸 Demo

<img width="1912" height="962" alt="Content Automation Pipeline" src="https://github.com/user-attachments/assets/6c7f2fc9-1a92-443e-9590-244b5fac708e" />


## ✨ Features

- **CSV input** — add unlimited topics in seconds
- **Multi-platform output** — Twitter (3 variants), LinkedIn, Email, Blog titles
- **Local AI** — runs on your GPU, zero cloud API costs
- **Excel export** — 5 organized sheets, ready to use immediately
- **Batch processing** — generate 50+ pieces of content per run

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| AI Generation | Ollama + LLaMA 3.1 8B |
| Data Processing | Pandas |
| Output | OpenPyXL (Excel) |
| Hardware | NVIDIA RTX 3060 (GPU-accelerated) |

---

## 🚀 Installation

**1. Clone the repository**
```bash
git clone https://github.com/sawtrader/content-automation-pipeline.git
cd content-automation-pipeline
```

**2. Install dependencies**
```bash
pip install pandas tqdm openpyxl requests
```

**3. Setup Ollama**
```bash
ollama pull llama3.1:8b
ollama serve
```

**4. Run**
```bash
python main.py
```

---

## 📖 Usage

**1. Edit `sample_input.csv` dengan topik kamu:**

```csv
topic,tone,target_audience,brand_name
Your topic here,professional,target audience,Brand Name
```

**2. Jalankan pipeline:**
```bash
python main.py
```

**3. Buka file Excel output** — ada 5 sheet:
- **Twitter** — 3 variasi per topik
- **LinkedIn** — long-form post
- **Email** — subject + preview text
- **Blog Titles** — 5 judul per topik
- **Summary** — statistik run

---

## 💼 Business Use Cases

- **Marketing agencies** — generate content for multiple clients at scale
- **E-commerce** — product descriptions and social posts in bulk
- **Content creators** — never run out of post ideas
- **Startups** — launch content strategy without hiring a copywriter

---

## 📋 Project Structure

content-automation-pipeline/

├── main.py             # Pipeline orchestrator

├── generator.py        # LLM content generation logic

├── sample_input.csv    # Example input file

└── README.md

---

*Built with Python + Local LLM | GPU-accelerated on NVIDIA RTX 3060 - Created by Surya Adriwiranata*
