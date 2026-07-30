import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# -------------------------------------------------
# PAGE SETTINGS
# -------------------------------------------------
st.set_page_config(
    page_title="Healthy Tomato vs Tomato Mosaic Virus",
    page_icon="🍅",
    layout="centered"
)

# -------------------------------------------------
# APP TITLE
# -------------------------------------------------
st.title("🍅 Healthy Tomato vs Tomato Mosaic Virus")

st.write(
    "Upload an image of a tomato leaf to classify it as "
    "**Healthy Tomato** or **Tomato Mosaic Virus** using both "
    "the Custom CNN and Transfer Learning models."
)

# -------------------------------------------------
# LOAD BOTH MODELS
# -------------------------------------------------

@st.cache_resource
def load_models():
    try:
        # Custom CNN model
        custom_cnn_model = tf.keras.models.load_model(
        "tomato_leaf_cnn_final.keras")

        # Transfer Learning model
        transfer_learning_model = tf.keras.models.load_model(
        "custom_cnn_best.keras")

        return custom_cnn_model, transfer_learning_model


# Load both models
custom_cnn_model, transfer_learning_model = load_models()

# Display confirmation
st.success("Custom CNN and Transfer Learning models loaded successfully!")

# -------------------------------------------------
# CLASS NAMES
# IMPORTANT:
# This order must be the same as the order used
# when the models were trained.
# -------------------------------------------------

class_names = [
    "Tomato Mosaic Virus",
    "Healthy Tomato"
]


# -------------------------------------------------
# IMAGE PREPROCESSING
# -------------------------------------------------

def preprocess_image(image):

    # Resize image to the size used during training
    image = image.resize((128, 128))

    # Convert image to a NumPy array
    image_array = np.array(image)

    # Convert image values from 0–255 to 0–1
    image_array = image_array / 255.0

    # Add the batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    return image_array


# -------------------------------------------------
# PREDICTION FUNCTION
# -------------------------------------------------

def make_prediction(model, processed_image):

    prediction = model.predict(
        processed_image,
        verbose=0
    )

    # For models with two output neurons
    if prediction.shape[-1] == 2:

        predicted_index = np.argmax(prediction[0])

        confidence = float(
            prediction[0][predicted_index]
        )

    # For models with one sigmoid output
    else:

        probability = float(
            prediction[0][0]
        )

        if probability >= 0.5:

            predicted_index = 1

            confidence = probability

        else:

            predicted_index = 0

            confidence = 1 - probability

    predicted_class = class_names[
        predicted_index
    ]

    return predicted_class, confidence


# -------------------------------------------------
# IMAGE UPLOADER
# -------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload a tomato leaf image",
    type=["jpg", "jpeg", "png"],
    key="tomato_leaf_uploader"
)


# -------------------------------------------------
# DISPLAY IMAGE AND PREDICTIONS
# -------------------------------------------------

if uploaded_file is not None:

    # Open uploaded image
    image = Image.open(
        uploaded_file
    ).convert("RGB")

    # Display the image
    st.image(
        image,
        caption="Uploaded Tomato Leaf",
        use_container_width=True
    )

    # Preprocess the image
    processed_image = preprocess_image(
        image
    )

    st.subheader("Prediction Results")

    # ---------------------------------------------
    # CUSTOM CNN PREDICTION
    # ---------------------------------------------

    custom_class, custom_confidence = (
        make_prediction(
            custom_cnn_model,
            processed_image
        )
    )

    st.markdown(
        "### Custom CNN Model"
    )

    st.write(
        f"**Prediction:** {custom_class}"
    )

    st.write(
        f"**Confidence:** "
        f"{custom_confidence * 100:.2f}%"
    )

    st.progress(
        int(custom_confidence * 100)
    )

    # ---------------------------------------------
    # TRANSFER LEARNING PREDICTION
    # ---------------------------------------------

    transfer_class, transfer_confidence = (
        make_prediction(
            transfer_learning_model,
            processed_image
        )
    )

    st.markdown(
        "### Transfer Learning Model"
    )

    st.write(
        f"**Prediction:** {transfer_class}"
    )

    st.write(
        f"**Confidence:** "
        f"{transfer_confidence * 100:.2f}%"
    )

    st.progress(
        int(transfer_confidence * 100)
    )

    # ---------------------------------------------
    # COMPARE BOTH MODELS
    # ---------------------------------------------

    st.divider()

    st.subheader(
        "Comparison of Both Models"
    )

    if custom_class == transfer_class:

        st.success(
            "Both models agree: "
            f"**{custom_class}**"
        )

    else:

        st.warning(
            "The two models gave different "
            "predictions."
        )

        st.write(
            "Custom CNN prediction: "
            f"**{custom_class}**"
        )

        st.write(
            "Transfer Learning prediction: "
            f"**{transfer_class}**"
        )