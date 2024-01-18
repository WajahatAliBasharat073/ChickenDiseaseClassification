## Chicken Disease Classification
This project aims to develop an accurate chicken disease classification system using fecal images from a Kaggle dataset. The system can help poultry farmers and veterinarians diagnose chicken diseases quickly and easily.

## Dataset
The dataset contains 5,000 fecal images of chickens with various diseases, such as coccidiosis, necrotic enteritis, salmonellosis, and healthy. 

## Requirements
The project is implemented in Python and requires the following libraries:

- Scikit-learn
- TensorFlow
- pandas
- Flask
## Methodology
**The project follows these steps:**

- Data augmentation: Apply random transformations, such as rotation, zoom, and flip, to the images to increase the diversity and size of the dataset.
- Data normalization: Scale the pixel values of the images to the range [0, 1] to reduce the variance and improve the convergence of the model.
- Data regularization: Add a small amount of noise to the images to reduce overfitting and improve the robustness of the model.
- Feature extraction: Use VGG16, a pre-trained convolutional neural network, to extract high-level features from the images.
- Classification: Use SVM, a linear classifier, to classify the images into different disease categories based on the extracted features.
- Model evaluation: Use accuracy, precision, recall, and F1-score metrics to measure the performance of the model on the test set.
The project is also designed using modular programming, which means that the code is divided into smaller, reusable, and independent modules. This makes the code easier to read, maintain, and debug, as well as facilitates collaboration and testing.

## Results
The model achieves an accuracy of 88% on the test set, which is 18% better than the baseline model, which is a simple logistic regression. The system also provides a user-friendly Flask web application that allows users to upload fecal images and get instant diagnosis of chicken diseases.

## Future Work
**Some possible directions for future work are:**

- Extend the system to classify other types of poultry diseases, such as avian influenza, Newcastle disease, and Marek’s disease.
- Explore more advanced deep learning techniques, such as transfer learning, fine-tuning, and attention mechanisms, to improve the feature extraction and classification capabilities of the model.
