

import torch
"""
This script uses the Stable Diffusion model to generate an image based on a given prompt.
Modules:
    torch: PyTorch library for tensor computations and GPU acceleration.
    diffusers: Library for loading and using diffusion models, such as Stable Diffusion.
Functions:
    None
Usage:
    The script loads a pre-trained Stable Diffusion model, generates an image from a text prompt, and saves the image to a file.
Variables:
    model_id (str): Identifier for the pre-trained Stable Diffusion model.
    pipe (StableDiffusionPipeline): Pipeline for generating images using the Stable Diffusion model.
    prompt (str): Text prompt for generating the image.
    image (PIL.Image.Image): Generated image based on the prompt.
Output:
    The generated image is saved as "output.png" in the current directory.
"""
from diffusers import StableDiffusionPipeline

# Load the pre-trained model
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# Generate an image
prompt = "A painting of a futuristic city"
image = pipe(prompt).images[0]

# Save the image
image.save("output.png")
