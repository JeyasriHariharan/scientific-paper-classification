import streamlit as st
import pickle
import gdown
import os
import re
import nltk
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from keybert import KeyBERT

st.set_page_config(
    page_title="Scientific Paper Classifier",
    page_icon="📄",
    layout="wide"
)

@st.cache_resource
def load_models():
    model_files = {
        'rf_model.pkl': '1TLHp8UbZGRIRMR4VEc_NCVyD9ZvknVq2',
        'tfidf.pkl': '1aVrQA7UhlYVkpQMEbkFtlKCOHPzxtdFb',
        'label_encoder.pkl': '1ZqqmLzsICNaoGelaQRLk56LVHe2XVs-g'
    }
    for filename, file_id in model_files.items():
        if not os.path.exists(filename):
            gdown.download(
                f'https://drive.google.com/uc?id={file_id}',
                filename,
                quiet=False
            )
    rf = pickle.load(open('rf_model.pkl', 'rb'))
    tfidf = pickle.load(open('tfidf.pkl', 'rb'))
    le = pickle.load(open('label_encoder.pkl', 'rb'))
    return rf, tfidf, le

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(w)
              for w in tokens if w not in stop_words]
    return ' '.join(tokens)

st.title("📄 AI Scientific Paper Classifier")
st.markdown("### Classify research papers and extract keywords!")
st.markdown("---")

st.sidebar.title("📊 About This App")
st.sidebar.info("""
**AI Paper Classifier**

This app uses Machine Learning to:
- 🖥️ Classify papers into domains
- 🔑 Extract important keywords
- 📊 Show confidence scores

**Models Used:**