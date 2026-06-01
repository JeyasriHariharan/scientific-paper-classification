# 📄 AI Scientific Paper Classification System

## Project Overview
An AI-based system that automatically classifies 
scientific paper abstracts into research domains 
and extracts important keywords using NLP.

## 🎯 Features
- Research Domain Classification
- Keyword Extraction using KeyBERT
- Confidence Score Display
- Interactive Web Interface

## 📊 Models & Results
| Model | Type | Accuracy |
|-------|------|----------|
| Logistic Regression | ML | 94.16% |
| Naive Bayes | ML | 92.91% |
| Random Forest | ML | 95.65% |
| CNN Text Model | DL | 95.40% |
| BiLSTM | DL | 94.85% |
| DistilBERT | Transformer | 87.00% |

## 🏆 Best Model
Random Forest with 95.65% accuracy!

## 🔑 Keyword Extraction Methods
- TF-IDF Keywords
- SpaCy Noun Phrases
- KeyBERT (Best Results!)

## 🛠️ Technologies Used
- Python
- Scikit-learn
- NLTK
- SpaCy
- KeyBERT
- Streamlit
- Hugging Face

## 📁 Dataset
- Source: arXiv Paper Abstracts
- Total Papers: 56,181
- Domains: Computer Vision, Machine Learning

## 🚀 How to Run
1. Clone this repository
2. Install requirements:
   pip install -r requirements.txt
3. Run the app:
   streamlit run app.py

## 📝 Project By
**Jeyasri Karpaga Murukesan**
GUVI - HCL | Master Data Science Program