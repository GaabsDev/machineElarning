import cv2
import numpy as np
import tensorflow as tf

# Carregar o modelo de detecção pré-treinado do TensorFlow Object Detection API
detection_model = tf.saved_model.load('path/to/detection/model')

# Inicializar o classificador de faces do OpenCV
face_cascade = cv2.CascadeClassifier('path/to/haarcascade_frontalface_default.xml')

# Capturar vídeo da webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Detecção de faces usando TensorFlow Object Detection API
    input_tensor = tf.convert_to_tensor(frame)
    detections = detection_model(input_tensor)

    for detection in detections['detection_boxes']:
        y_min, x_min, y_max, x_max = detection.numpy()
        h, w, _ = frame.shape
        x_min, y_min, x_max, y_max = int(x_min * w), int(y_min * h), int(x_max * w), int(y_max * h)

        # Recortar a área da face
        face = frame[y_min:y_max, x_min:x_max]

        # Reconhecimento de faces usando OpenCV
        gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_face, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(face, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Face Detection and Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
