from transformers import pipeline
import gradio as gradio

model = pipeline("summarization")

def fun1(statement):
    bac = statement.lower()
    print(bac)
    return bac

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="text",lines=4)
    gr.Interface(fn=predict,inputs=textbox,outputs="text")

demo.launch()