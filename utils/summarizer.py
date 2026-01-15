from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_notes(text):
    summary = summarizer(text, max_length=150, min_length=60, do_sample=False)
    return summary[0]['summary_text']
