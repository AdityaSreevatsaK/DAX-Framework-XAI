# DAX Framework - XAI

**Domain-Aligned Explainability Framework for Responsible AI Deployment**

---

## 🧠 What is the DAX Framework?

The **DAX (Domain-Aligned Explainability)** Framework is a practical guide for selecting Explainable AI (XAI) techniques tailored to real-world application needs. Rather than organizing XAI tools by algorithm class, DAX aligns method selection with:

- **Data Modality** (e.g., tabular, text, images)
- **Domain Constraints** (e.g., legal, ethical, regulatory)
- **Explanation Goals** (e.g., auditing, trust, debugging)

This repository provides a minimal prototype of the DAX decision tree (as introduced in our paper) to help researchers and engineers identify the most appropriate XAI technique for their application context.

---

## 📌 Paper Reference

> **A Domain-Aligned Framework for Explainable AI: Matching Techniques to Application Needs**  
> *Aditya Sreevatsa K (2025). Under submission.*

In the paper, we:
- Propose a new XAI taxonomy guided by contextual requirements
- Map key XAI methods to five domains (Healthcare, Finance, NLP/LLMs, Law & Policy, Vision)
- Validate our approach through retrospective case studies
- Offer this repo as a prototype decision-support tool

---

## 📄 License

This repository is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this work, provided appropriate credit is given to the author.

---



## 🚀 Quick Start

### 🔧 Requirements
Please refer [Requirements](requirements.txt) file.
To install dependencies, run:  
```bash
pip install -r requirements.txt
```

### ▶️ Usage
```bash
streamlit run App.py
```
