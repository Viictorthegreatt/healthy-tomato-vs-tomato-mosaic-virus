import streamlit as st
import numpy as np 
import tensorflow as tf 
from PIL import Image 
import pathlib

st.title("🍅 Healthy Tomato vs Tomato Mosaic Virus")

# Instructions for using the application

st.markdown("""
### How to Use the Application

1. Upload a clear image of a tomato leaf.
2. The image should be in JPG, JPEG, or PNG format.
3. Wait for the model to process the image.
4. The application will display the predicted class and confidence level.

**Possible predictions:**
- Healthy Tomato
- Tomato Mosaic Virus
""")

st.divider()

st.write(
    "Upload an image of a tomato leaf to determine whether "
    "it is healthy or affected by Tomato Mosaic Virus."
)


# Path to the saved Custom CNN model
CNN_MODEL_PATH = "models/tomato_leaf_cnn_final.keras"

# Load the Custom CNN model
cnn_model = tf.keras.models.load_model(
    CNN_MODEL_PATH
)

st.success("Custom CNN model loaded successfully!")
# Class names must follow the same order used during training

class_names = [
    "Tomato Mosaic Virus",
    "Healthy Tomato"
]
 # Upload a tomato leaf image

uploaded_file = st.file_uploader(
    "Upload a tomato leaf image",
    type=["jpg", "jpeg", "png"],
    key="tomato_leaf_uploader"
)

if uploaded_file is not None:

    # Open the uploaded image
    image = Image.open(
        uploaded_file
    ).convert("RGB")

    # Display the uploaded image
    st.image(
        image,
        caption="Uploaded Tomato Leaf Image",
        use_container_width=True
    )

    # Resize the image to the size used during training
    resized_image = image.resize(
        (128, 128)
    )

    # Convert the image to a NumPy array
    image_array = np.array(
        resized_image
    )

    # Add the batch dimension
    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    # Make prediction
    prediction = cnn_model.predict(
        image_array,
        verbose=0
    )

    # Get the predicted class
    predicted_index = np.argmax(
        prediction[0]
    )

    predicted_class = class_names[
        predicted_index
    ]

    # Calculate confidence
    confidence = (
        prediction[0][predicted_index] * 100
    )

    # Display result
    st.subheader(
        "Prediction Result"
    )

    if predicted_class == "Healthy Tomato":

        st.success(
            f"Prediction: {predicted_class}"
        )

    else:

        st.warning(
            f"Prediction: {predicted_class}"
        )

    st.write(
        f"Confidence: **{confidence:.2f}%**"
    )
    st.divider()

st.caption(
    "This application uses a Custom Convolutional Neural Network "
    "(CNN) to classify tomato leaf images."
)