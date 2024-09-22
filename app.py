import gradio as gr
from image_cap import generate_caption

def greet(image, text):
    return 

demo = gr.Interface(
    fn=greet,
    inputs=[gr.inputs.Image(type="pil"), "text"],
    outputs=["text"],
)

demo.launch(server_name="0.0.0.0", server_port= 7860)