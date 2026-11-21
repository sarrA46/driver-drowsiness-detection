
import cv2
import dlib
import numpy as np
from scipy.spatial import distance
from imutils import face_utils
import sys
import serial
import time

print("Python lance avec succes !")

# ==========================================
# COMMUNICATION ARDUINO
# ==========================================

try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)
    print("Arduino connecte sur COM3")

except Exception as e:
    print("Impossible de se connecter a Arduino :", e)
    arduino = None


# ==========================================
# CHARGEMENT DU MODELE DLIB
# ==========================================

PREDICTOR_PATH = (
    r"C:\Users\yosra\OneDrive\Bureau"
    r"\shape_predictor_68_face_landmarks.dat"
)

try:
    predictor = dlib.shape_predictor(PREDICTOR_PATH)
    print("Shape predictor charge avec succes !")

except Exception as e:
    print("ERREUR DLIB :", e)

    if arduino:
        arduino.close()

    sys.exit()


# ==========================================
# INITIALISATION WEBCAM
# ==========================================

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Webcam introuvable")

    if arduino:
        arduino.close()

    sys.exit()

else:
    print("Webcam OK")


# ==========================================
# CALCUL DE L'EYE ASPECT RATIO (EAR)
# ==========================================

def eye_aspect_ratio(eye):

    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])

    ear = (A + B) / (2.0 * C)

    return ear


# ==========================================
# PARAMETRES DE DETECTION
# ==========================================

EAR_THRESHOLD = 0.25
EAR_CONSEC_FRAMES = 20

COUNTER = 0
ALERT_ON = False

# Eviter l'envoi repetitif des memes commandes
last_command = None


# ==========================================
# DETECTEUR DE VISAGE DLIB
# ==========================================

detector = dlib.get_frontal_face_detector()

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


# ==========================================
# BOUCLE PRINCIPALE
# ==========================================

while True:

    ret, frame = cap.read()

    if not ret:
        print("Image non recue de la webcam.")
        break

    frame = cv2.resize(frame, (640, 480))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray, 0)

    # Aucun visage detecte
    if len(faces) == 0:

        COUNTER = 0
        ALERT_ON = False

        if arduino and last_command != 'N':
            arduino.write(b'N')
            last_command = 'N'

    # ======================================
    # DETECTION DES YEUX
    # ======================================

    for face in faces:

        shape = predictor(gray, face)

        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0

        # Dessiner les contours des yeux
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)

        cv2.drawContours(
            frame, [leftEyeHull], -1, (0, 255, 0), 1
        )

        cv2.drawContours(
            frame, [rightEyeHull], -1, (0, 255, 0), 1
        )

        # ==================================
        # DETECTION DE SOMNOLENCE
        # ==================================

        if ear < EAR_THRESHOLD:
            COUNTER += 1
        else:
            COUNTER = 0

        if COUNTER >= EAR_CONSEC_FRAMES:

            ALERT_ON = True

            if arduino and last_command != 'O':
                arduino.write(b'O')
                last_command = 'O'

            cv2.putText(
                frame,
                "SLEEPING !!!",
                (150, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0, 0, 255),
                3
            )

        else:

            ALERT_ON = False

            if arduino and last_command != 'N':
                arduino.write(b'N')
                last_command = 'N'

        # Affichage EAR
        cv2.putText(
            frame,
            f"EAR: {ear:.2f}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

        # Affichage compteur
        cv2.putText(
            frame,
            f"Counter: {COUNTER}",
            (10, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

    # ======================================
    # AFFICHAGE DE L'ETAT
    # ======================================

    status = "Alert: ON" if ALERT_ON else "Alert: OFF"

    color = (0, 0, 255) if ALERT_ON else (0, 255, 0)

    cv2.putText(
        frame,
        status,
        (450, 460),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        color,
        2
    )

    cv2.imshow("Driver Drowsiness Detection", frame)

    # Quitter avec Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# ==========================================
# LIBERATION DES RESSOURCES
# ==========================================

cap.release()

cv2.destroyAllWindows()

if arduino:
    arduino.write(b'N')
    arduino.close()

print("Programme termine.")
