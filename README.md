# Muffin vs Chihuahua Image Classifier
An end-to-end image classification project built with PyTorch and Flask, designed to distinguish between images of muffins and chihuahuas. The project covers the full machine learning workflow — from data preprocessing and model training to deployment and real-time inference via a web interface.

## Project Overview
This project demonstrates how a deep learning model can be trained and deployed as a usable web application. A ResNet18 model was trained using PyTorch and served through a Flask backend, allowing users to upload images and receive instant predictions through a browser-based interface.

### Model & Training
- Framework: PyTorch
- Architecture: ResNet18
- Loss Function: CrossEntropyLoss
- Optimiser: Stochastic Gradient Descent (SGD)
- Accuracy Achieved: __98.99%__ 

### Training Pipeline
- Image preprocessing and resizing
- Dataset loading and batching
- Model training and evaluation
- Model checkpoint saving for deployment

### Web Application
- Backend: Flask (Python)
- Frontend: HTML, Jinja templating, JavaScript
- Features:
  * Image upload and real-time prediction 
  * REST API endpoints for inference and feedback 
  * Live accuracy tracking based on user feedback

### How to Run

```bash
pip install torch torchvision flask numpy
```

```bash
python app.py
```

Open your browser and go to:
`http://127.0.0.1:5068`

### Key Takeaways:
- Built a complete ML data pipeline from preprocessing to deployment
- Gained hands-on experience with CNN-based image classification
- Implemented real-time inference and performance monitoring
- Demonstrated end-to-end model-to-product workflow

### Future Improvements:
- Support multi-class image classification
- Visualise prediction confidence scores
- Replace manual accuracy tracking with automated evaluation

## Author
Built independently as a hands-on deep learning and deployment project.
