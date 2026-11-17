# Image Captioning App

A small Streamlit app that generates captions for uploaded images using the pretrained BLIP model (`Salesforce/blip-image-captioning-base`) from Hugging Face Transformers.

## Features

- Upload a JPG/PNG image and generate a caption
- **Guided generation:** optionally give the start of the sentence (e.g. "A photo of a") and the model continues it
- Adjustable generation parameters in the sidebar: temperature, minimum and maximum caption length, and number of caption variations (sampling with `top_k=50`)

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

The model weights are downloaded from Hugging Face on first run.
