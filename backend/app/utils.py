import os
from transformers import pipeline

summarizer = pipeline("summarization")

def save_file(upload_file):
    try:
        file_location = f"files/{upload_file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(upload_file.file.read())
        return file_location
    except Exception as e:
        return None

def summarize_document(text):
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']
