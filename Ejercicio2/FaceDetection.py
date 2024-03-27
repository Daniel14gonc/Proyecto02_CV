import cv2

from utils import detect_faces, draw_face_rectangle

# Inicializar la captura de video desde la cámara web
cap = cv2.VideoCapture(0)

while True:
    # Leer un cuadro del video
    ret, frame = cap.read()

    frontal_faces, profile_faces = detect_faces(frame)

    draw_face_rectangle(frame, frontal_faces)
    draw_face_rectangle(frame, profile_faces)

    # Mostrar el cuadro con los rostros detectados
    cv2.imshow('Detector de rostros en tiempo real', frame)

    # Romper el bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el objeto de captura y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
