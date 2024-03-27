import cv2

# Cargar los clasificadores preentrenados para detección de rostros frontales y de perfil
frontal_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
profile_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

def detect_faces(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detectar rostros frontales en el cuadro
    frontal_faces = frontal_face_cascade.detectMultiScale(gray_frame, 1.1, 4)

    # Detectar rostros de perfil en el cuadro
    profile_faces = profile_face_cascade.detectMultiScale(gray_frame, 1.1, 4)

    return frontal_faces, profile_faces

def draw_face_rectangle(frame, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)