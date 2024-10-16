
# Real-Time Face Recognition System Using OpenCV and LBPH Algorithm

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Features](#features)
4. [Installation](#installation)
5. [Usage](#usage)
6. [How It Works](#how-it-works)
7. [File Structure](#file-structure)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview
This project implements a Real-Time Face Recognition System using OpenCV and the Local Binary Patterns Histograms (LBPH) algorithm. The system captures video input from a camera, detects faces in real-time, and recognizes individuals based on a pre-trained model. The primary goal of this project is to demonstrate the application of computer vision techniques for face recognition, providing a foundation for more complex implementations such as security systems, attendance management, and user authentication.

## Technologies Used
- **Python**: The primary programming language for implementing the face recognition algorithms.
- **OpenCV**: A powerful library for computer vision tasks that provides tools for image processing and manipulation.
- **NumPy**: A library for numerical computing in Python, which aids in handling arrays and matrices for image data.
- **scikit-learn**: A machine learning library that supports the training and evaluation of models.
- **Git**: Version control system used to manage the project files.
- **Git Large File Storage (LFS)**: A Git extension for managing large files efficiently.

## Features
- **Real-Time Face Detection**: Utilizes Haar Cascades for detecting faces in live video streams.
- **Face Recognition**: Implements the LBPH algorithm to recognize faces from a pre-trained model.
- **User-Friendly Interface**: Displays recognized names on the video feed, making it easy to identify individuals.
- **Train New Faces**: Allows adding new faces to the model by providing images, which can be retrained for better accuracy.

## Installation
Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<username>/Real-Time-Face-Recognition-System-Using-OpenCV-Python-and-LBPH-Algorithm.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Real-Time-Face-Recognition-System-Using-OpenCV-Python-and-LBPH-Algorithm
   ```

3. **Install Required Packages**:
   Make sure you have Python installed on your system. Install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

   _Note: If you don’t have a `requirements.txt` file, you can create one by using the following command to capture the current environment packages:_
   ```bash
   pip freeze > requirements.txt
   ```

## Usage
To run the Face Recognition System:

1. Ensure your camera is connected and functioning.
2. Run the main script:
   ```bash
   python main.py
   ```

3. The system will open a window displaying the live video feed with recognized faces. Press `q` to exit the program.

## How It Works
1. **Face Detection**: The system uses Haar Cascade classifiers to detect faces in the video stream. These classifiers are pre-trained and can identify frontal faces in images.

2. **Feature Extraction**: Once a face is detected, the LBPH algorithm extracts features from the face image, which involves converting the image into a histogram representation based on local binary patterns.

3. **Recognition**: The extracted features are compared with those stored in the model. If a match is found, the recognized name is displayed on the video feed.

4. **Training**: To train the model with new faces, images of the individuals should be added to a designated folder, and the training script should be run.

## File Structure
```plaintext
Real-Time-Face-Recognition-System-Using-OpenCV-Python-and-LBPH-Algorithm/
│
├── .gitignore             # Specifies files to be ignored by Git
├── README.md              # Project documentation
├── requirements.txt       # Required Python packages
├── Trainer.yml            # Configuration file for training settings
├── main.py                # Main script to run the face recognition system
├── train.py               # Script to train the model with new face images
├── data/                  # Directory containing training images
│   ├── person1/           # Images of person 1
│   ├── person2/           # Images of person 2
│   └── ...
└── models/                # Directory for storing trained models
    └── face_recognition_model.xml
```

## Contributing
Contributions to this project are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to submit a pull request or open an issue.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Feel free to modify any section to better fit your project's specifics! Let me know if you need any further adjustments or additional information!
