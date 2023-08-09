from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

textbox = gr.Textbox(placeholder="Enter the block to summarize", lines=4)
interface = gr.Interface(fn=predict, inputs=textbox, outputs="text",  title="Text Summarization by Abdul Jaweed")

interface.launch()
