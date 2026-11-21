
<img width="704" height="404" alt="shematic capture" src="https://github.com/user-attachments/assets/da25259e-5843-4f33-a168-05629215c24d" />

# Driver Drowsiness Detection System 🚗

## 📌 Project Overview

This project aims to develop an intelligent Driver Drowsiness Detection System using Computer Vision and Embedded Systems.

The system monitors the driver's eyes in real time through a webcam using Python, OpenCV and Dlib. It calculates the Eye Aspect Ratio (EAR) to detect prolonged eye closure, which may indicate driver fatigue or drowsiness.

When drowsiness is detected, an Arduino automatically activates an alert system consisting of an RGB LED, a buzzer and a DC motor.

## 🎯 Objectives

- Detect driver drowsiness in real time.
- Monitor eye movements using facial landmarks.
- Calculate the Eye Aspect Ratio (EAR).
- Send detection signals from Python to Arduino.
- Activate audio and visual alerts.
- Control a motor according to the driver's alertness state.

## 🛠️ Technologies Used

**Software:**
- Python
- OpenCV
- Dlib
- NumPy
- SciPy
- Imutils
- PySerial

**Hardware:**
- Arduino UNO
- Webcam
- RGB LED
- Buzzer
- DC Motor

## ⚙️ System Architecture

1. The webcam captures the driver's face.
2. Dlib detects facial landmarks.
3. The system extracts eye coordinates.
4. The Eye Aspect Ratio (EAR) is calculated.
5. If the eyes remain closed for a predefined number of consecutive frames, drowsiness is detected.
6. Python sends a serial command to Arduino.
7. Arduino activates the appropriate alerts.

## 👁️ Eye Aspect Ratio (EAR)

The Eye Aspect Ratio is used to estimate whether the driver's eyes are open or closed.

EAR is calculated using the following formula:

EAR = (||P2-P6|| + ||P3-P5||) / (2 × ||P1-P4||)

When the EAR value falls below a predefined threshold for a certain number of consecutive frames, the system detects possible drowsiness.

## 🚨 Alert Mechanism

| System State | RGB LED | Buzzer | Motor |
|---|---|---|---|
| Normal | Green | OFF | ON |
| Drowsiness detected (first 3 seconds) | Orange | Intermittent | ON |
| Prolonged drowsiness | Red | ON | OFF |

## 📂 Project Structure

```text
Driver-Drowsiness-Detection-System/
│
├── python/
│   └── drowsiness_detection.py
├── arduino/
│   └── drowsiness_alert.ino
├── images/
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Driver-Drowsiness-Detection-System.git
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the Dlib facial landmarks model

Download `shape_predictor_68_face_landmarks.dat` and place it in the project directory.

The model is required for facial landmark detection.

### 4. Configure Arduino

- Open `arduino/drowsiness_alert.ino` in Arduino IDE.
- Connect the Arduino UNO.
- Select the correct COM port.
- Upload the program.

### 5. Run the Python application

Configure the Arduino serial port and the facial landmarks model path in the Python script.

Then execute:

```bash
python python/drowsiness_detection.py
```

## 📦 Python Dependencies

- opencv-python
- dlib
- numpy
- scipy
- imutils
- pyserial

## 🔮 Future Improvements

- Integrate facial yawning detection.
- Add head pose estimation.
- Develop a graphical user interface.
- Integrate GPS and IoT monitoring.
- Send remote notifications in case of detected drowsiness.
- Improve detection accuracy under different lighting conditions.

## 👩‍💻 Author

**Your Name**

Embedded Systems & IoT Student

## 📄 License

This project is licensed under the MIT License.
