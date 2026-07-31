# 🍅 Healthy Tomato vs Tomato Mosaic Virus Classification

A deep learning application that classifies tomato leaf images as either **Healthy Tomato** or **Tomato Mosaic Virus**, using both a **Custom Convolutional Neural Network (CNN)** and a **Transfer Learning model**. The models are deployed as an interactive web application using **Streamlit**.

## 🔗 Live App

https://healthy-tomato-vs-tomato-mosaic-virus-6bh9bbvb37meky9if329ey.streamlit.app/
---

## 🔗 Overview

This project was developed for **Laboratory Exercise 10: Cloud Computing and AI Model Deployment for Engineering Applications**.

The project covers the complete machine-learning deployment workflow:

1. Training a Custom CNN model using labelled tomato-leaf images.
2. Training and evaluating a Transfer Learning model.
3. Saving the trained models in Keras format.
4. Building an interactive Streamlit application for image upload and prediction.
5. Displaying predictions and confidence scores from both models.
6. Deploying the application on Streamlit Community Cloud through GitHub.

---

## 🔗 Model

- **Task:** Binary image classification  
  *(Healthy Tomato vs. Tomato Mosaic Virus)*

- **Models Used:**
  - Custom Convolutional Neural Network (CNN)
  - Transfer Learning model

- **Input Size:** 128 × 128 RGB images

- **Input Preprocessing:**
  - Images are resized to 128 × 128 pixels.
  - Images are converted to RGB format.
  - Images are converted into NumPy arrays.
  - Pixel values are normalized from 0–255 to 0–1.
  - A batch dimension is added before prediction.

- **Output:**
  - Healthy Tomato
  - Tomato Mosaic Virus

- **Prediction Results:**
  - Predicted class from the Custom CNN model
  - Confidence score from the Custom CNN model
  - Predicted class from the Transfer Learning model
  - Confidence score from the Transfer Learning model

> **Note:** The models were trained only to distinguish between **Healthy Tomato** and **Tomato Mosaic Virus**. Images containing other tomato diseases or unrelated objects may still be classified as one of these two classes because the models are limited to the classes used during training.

---

## 🔗 How to Use the Application

1. Open the **Streamlit application** using the live app link.
2. Click **Browse files** or the image-upload area.
3. Select a tomato-leaf image in **JPG, JPEG, or PNG** format.
4. The uploaded image will be displayed in the application.
5. Click the **Predict** button, if available.
6. The application processes the image and sends it to both trained models.
7. View the results, including:
   - Custom CNN predicted class
   - Custom CNN confidence score
   - Transfer Learning predicted class
   - Transfer Learning confidence score

---

## 🔗 Project Structure

```text
healthy-tomato-vs-tomato-mosaic-virus/
│
├── app.py
├── tomato_leaf_cnn_final.keras
├── custom_cnn_best.keras
├── requirements.txt
├── README.md
```


## 🔗 File Description

• app.py – Contains the Streamlit application code.

• tomato_leaf_cnn_final.keras – Saved Custom CNN model.

• custom_cnn_best.keras – Saved Transfer Learning model.

• requirements.txt – Contains the Python libraries required to run the application.

• README.md – Provides information and instructions for the project.

**🔗 Running Locally**

° Clone the repository: Viictorthegreatt/healthy-tomato-vs-tomato-mosaic-virus

° Move into the project directory: cd healthy-tomato-vs-tomato-mosaic-virus

° Install the required libraries: pip install -r requirements.txt

° Run the Streamlit application: streamlit run app.py

° The application will open in a web browser.


**🔗 Tools Used**

Python · TensorFlow · Keras · Streamlit · NumPy · Pillow · Git · GitHub · Streamlit Community Cloud


**🔗 Challenges Encountered**

Several challenges were encountered during the development and deployment of the application:

• The saved model files were initially missing from the GitHub repository.

• The model file paths in app.py did not match the locations of the saved models.

• Syntax and indentation errors occurred while using the try and except blocks

• The application initially loaded only the Custom CNN model instead of both models.

• Streamlit required time to detect changes from GitHub and redeploy the application.

• TensorFlow displayed CUDA warnings because the deployment environment did not have GPU support.

• These challenges were resolved by correctly uploading both model files, updating the model paths, correcting the Python syntax and indentation, and modifying the model-loading function to load and return both models.


**🔗 Possible Improvements**

 Future versions of the application could include:

• Adding more tomato-leaf diseases.

• Training with a larger and more diverse dataset.

• Improving model accuracy and generalization.

• Adding a comparison chart for both models.

• Displaying prediction probabilities visually.

• Adding model-performance metrics.

• Including information on disease symptoms and possible management methods.

**🔗 Course Information**

Course: Laboratory Exercise 10 – Cloud Computing and AI Model Deployment for Engineering Applications

Project: Healthy Tomato vs Tomato Mosaic Virus Classification

Deployment Platform: Streamlit Community Cloud

- Streamlit URL: https://healthy-tomato-vs-tomato-mosaic-virus-6bh9bbvb37meky9if329ey.streamlit.app/

- GitHub Repository: Viictorthegreatt/healthy-tomato-vs-tomato-mosaic-virus

  **🔗 Authors**
  
  - Ekpenyong, Victor Isaiah - 23/EG/CE/005
  - Archibong, Otobong Bassey - 23/EG/CE/045
  - Joseph, Ediongoabasi Etoufok- 23/EG/CE/105
  - 
