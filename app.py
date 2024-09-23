import gradio as gr
from image_cap import get_hashtags

def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# Hashtaginator")
        gr.Markdown("Upload an image to generate relevant hashtags.")
        
        with gr.Column():
            image_input = gr.Image(type="pil", label="Upload Image")
            generate_button = gr.Button("Generate Hashtags")
            hashtags_output = gr.Textbox(label="Generated Hashtags")
        
        generate_button.click(fn=get_hashtags, inputs=image_input, outputs=hashtags_output)
    
    return demo

demo = create_interface()
demo.launch(server_name="0.0.0.0", server_port=7860)