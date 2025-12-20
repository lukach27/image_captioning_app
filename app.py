import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import numpy as np
import torch

### DO NOT EDIT IMPORTS ABOVE THIS LINE ###

# -----------------------------------------------------------------------------
# STEP 1: MODEL LOADING
# -----------------------------------------------------------------------------
@st.cache_resource
def load_caption_model():
    # TODO: Load the Processor (Handles image resizing & tokenization)
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    
    # TODO: Load the Model 
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

# TODO
processor, model = load_caption_model()

# -----------------------------------------------------------------------------
# STEP 2: UI LAYOUT
# -----------------------------------------------------------------------------
# TODO: set title and sidebar
st.set_page_config(page_title="Image Captioning App", page_icon="🖼️", layout="wide")

# Display Name and Student ID
st.markdown("---")
st.markdown("**Name:** Luka Čuturilo | **Student ID:** 912500138")
st.markdown("---")

st.title("🖼️ Image Captioning App")
st.markdown("Upload an image and generate captions using the BLIP vision-language model.")

# TODO: set sidebar sliders
with st.sidebar:
    st.header("⚙️ Parameter Controls")
    
    # 1. Temperature (min_value=0.1, max_value=1.5, value=0.1, step=0.1)
    temperature = st.slider("Temperature", min_value=0.1, max_value=1.5, value=0.7, step=0.1,
                           help="Controls the randomness and variability of generated captions. Higher values = more creative, lower values = more deterministic.")
    
    # 2. Max Length (min_value=5, max_value=30, value=20, step=1)
    max_length = st.slider("Max Length", min_value=5, max_value=30, value=20, step=1,
                          help="Maximum number of tokens in the generated caption.")
    
    # 3. Min Length (min_value=3, max_value=20, value=5, step=1)
    min_length = st.slider("Min Length", min_value=3, max_value=20, value=5, step=1,
                          help="Minimum number of tokens in the generated caption.")
    
    # 4. Number of Variations (min_value=1, max_value=5, value=1, step=1)
    num_variations = st.slider("Number of Variations", min_value=1, max_value=5, value=1, step=1,
                              help="Number of different captions to generate for the same image.")
    
    # Validation: Ensure min_length <= max_length
    if min_length > max_length:
        st.warning("⚠️ Min Length should be less than or equal to Max Length. Adjusting Min Length.")
        min_length = max_length

# -----------------------------------------------------------------------------
# STEP 3: MAIN PIPELINE
# -----------------------------------------------------------------------------
# TODO: Introduction text under title
st.markdown("### Upload an image to generate captions")

# TODO: File uploader for images, accept jpg, jpeg, png
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"],
                                 help="Upload an image in JPG, JPEG, or PNG format")

if uploaded_file is not None:
    # TODO: If an image is uploaded, display it
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # TODO: Create a input box for starting text prompt
    st.markdown("### Optional: Conditional Captioning")
    start_text = st.text_input("Starting text (optional)", 
                               placeholder="Enter a starting phrase for the caption (e.g., 'A beautiful')",
                               help="If provided, the model will generate captions starting with this text.")

    # # TODO: Create a button called 'Generate Caption' to trigger the AI
    if st.button("Generate Caption", type="primary"):
        # You may add a loading spinner here while the model is generating captions
        with st.spinner("Generating caption(s)..."):
            
            # TODO: Display a subheader 'Caption(s):'
            st.subheader("Caption(s):")
            
            # TODO: PRE-PROCESSING (Convert Image & Text to Tensors) ---
            # If user provided start_text, we pass it as 'text'. 
            # Otherwise we just pass the image.
            if start_text and start_text.strip():
                inputs = processor(image, text=start_text, return_tensors="pt")
            else:
                inputs = processor(image, return_tensors="pt")
            
            # TODO: Create a loop that runs 'num_captions' times
            captions = []
            for i in range(num_variations):
                # TODO: Pass the inputs and parameters to generate caption(s).
                # Some parameters are already given.
                # It should also contain the parameter values given by the user via the sliders.
                with torch.no_grad():
                    out = model.generate(
                        **inputs,
                        do_sample=True,             
                        temperature=temperature,
                        max_length=max_length,
                        min_length=min_length,
                        top_k=50
                    )

                # TODO: POST-PROCESSING (Decode Tensors back to Text)
                # The model gives us numbers, we need to decode them to words.
                # You may omit special tokens.
                caption_text = processor.decode(out[0], skip_special_tokens=True)
                captions.append(caption_text)
            
                # TODO: Display the result(s) depending on number of variations.
                if num_variations == 1:
                    st.success(f"**Caption:** {caption_text}")
                else:
                    st.write(f"**Variation {i+1}:** {caption_text}")
            
            # Display all captions in a summary if multiple variations
            if num_variations > 1:
                st.markdown("---")
                st.markdown("### All Captions Summary")
                for idx, cap in enumerate(captions, 1):
                    st.markdown(f"{idx}. {cap}")