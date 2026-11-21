# Driver Drowsiness Detection System 🚗

A real-time driver drowsiness detection system using computer vision and Arduino.

## 🛠️ Technologies
- Python
- OpenCV
- Dlib
- Arduino
- SciPy
- PySerial
<img width="704" height="404" alt="shematic capture" src="https://github.com/user-attachments/assets/da25259e-5843-4f33-a168-05629215c24d" />


## ⚙️ Features
- Real-time face and eye detection.
- Eye Aspect Ratio (EAR) calculation.
- Detection of prolonged eye closure.
- Arduino communication via serial port.
- Automatic alert using RGB LED, relay, and motor.

## 🔧 Hardware
- Arduino
- Webcam
- RGB LED (Common Anode)
- Buzzer
- Relay
- DC Motor

## 🚀 How It Works
1. The camera captures the driver's face.
2. Python detects facial landmarks and calculates the EAR.
3. If the eyes remain closed, an alert is triggered.
4. Arduino receives the signal and activates the alert system.

## ▶️ Installation

Install the required Python libraries:

```bash
pip install opencv-python dlib scipy pyserial
```

Download the `shape_predictor_68_face_landmarks.dat` file and place it in the project directory.

Run the Python script:

```bash
python main.py
```

## 👩‍💻 Author
Developed as an embedded systems and computer vision project.
