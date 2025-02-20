# Text extraction, summarization and Q&A

import PyPDF2
from transformers import pipeline

# 1. Text extraction from PDF

def extract_text(file_path):
    text = ""

    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text
    
    return text

#Summarization pipeline

summarizer = pipeline("summarization", model="google/pegasus-xsum")

def generate_summary(text):
    summary_list = summarizer(text, max_length=200, min_length=60, do_sample=False)
    return summary_list[0]['summary_text']

# Q&A Pipeline

qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

def answer_question(context, question):
    result = qa_pipeline({
        'context': context,
        'question':question
    })
    
    return result['answer']