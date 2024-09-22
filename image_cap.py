import requests
from PIL import Image
import torch
from transformers import AutoProcessor, BlipForConditionalGeneration

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using {device} for inference")

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base", clean_up_tokenization_spaces=True)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)


def generate_caption():
    # Load your image, DONT FORGET TO WRITE YOUR IMAGE NAME
    img_path = "office.jpg"
    # convert it into an RGB format our
    image = Image.open(img_path).convert('RGB')

    # You do not need a question for image captioning
    text = ""
    inputs = processor(images=image, text=text, return_tensors="pt").to(device)

    # Generate a caption for the image
    outputs = model.generate(**inputs, max_length=50)

    # Decode the generated tokens to text
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    # Print the caption
    print(caption)