import gradio as gr
from image_cap import get_hashtags

demo = gr.Interface(
    fn=get_hashtags,
    inputs=["image"],
    outputs=["text"],
)

demo.launch(server_name="0.0.0.0", server_port=7860)