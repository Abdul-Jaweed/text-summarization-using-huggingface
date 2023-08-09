from transformers import pipeline
import gradio as gr


model = pipeline("Summarization")

def predict(promt):
    summary = model(promt)[0]("summary_text")
    return summary



with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="Enter the block to summarize", lines=4)
    gr.Interface(fn=predict, inputs=textbox, outputs="text")

demo.launch()