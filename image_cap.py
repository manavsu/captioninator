import requests
from PIL import Image
import torch
from transformers import AutoProcessor, Blip2ForConditionalGeneration
import logging
import re

log = logging.getLogger(__name__)

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using {device} for inference")

# Load the pretrained processor and model
# processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base", clean_up_tokenization_spaces=True)
# model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b", clean_up_tokenization_spaces=True)
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16).to(device)

filler_words = open("filler_words.txt").readlines()
filler_words = [word.strip() for word in filler_words]

def get_hashtags(image):
    if not image:
        return "No image uploaded"
    
    # You do not need a question for image captioning
    inputs = processor(images=image, return_tensors="pt").to(device, torch.float16)

    # Generate a caption for the image
    outputs = model.generate(**inputs, max_length=50)

    log.debug(f"raw output tokens: {outputs}")

    # Decode the generated tokens to text
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    # Print the caption
    print(f"generated caption: {caption}")

    words = re.findall(r'\w+', caption)
    words.sort()
    words = set(words)
    hashtags = ', '.join(f'#{word.lower()}' for word in words if word and word not in filler_words)

    print(f"generated hashtags: {hashtags}")
    return hashtags
