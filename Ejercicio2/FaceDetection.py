import cv2
import itertools
from utils import detect_faces, draw_face_rectangle
import numpy as np

IOU_THRESHOLD = 0.5

# Función para calcular el área de intersección entre dos rectángulos
def intersection_over_union(rect1, rect2):
    # Coordenadas de los rectángulos
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2

    # Coordenadas del rectángulo de intersección
    x_intersection = max(x1, x2)
    y_intersection = max(y1, y2)
    w_intersection = min(x1 + w1, x2 + w2) - x_intersection
    h_intersection = min(y1 + h1, y2 + h2) - y_intersection

    # Calcular áreas de los rectángulos
    area_rect1 = w1 * h1
    area_rect2 = w2 * h2
    area_intersection = max(0, w_intersection) * max(0, h_intersection)

    # Calcular área de intersección sobre unión
    iou = area_intersection / (area_rect1 + area_rect2 - area_intersection)
    return iou

# Inicializar la captura de video desde la cámara web
cap = cv2.VideoCapture(0)

while True:
    # Leer un cuadro del video
    ret, frame = cap.read()

    frontal_faces, profile_faces = detect_faces(frame)
    
    if type(frontal_faces) == tuple:
        frontal_faces = np.array(frontal_faces)
    if type(profile_faces) == tuple:
        profile_faces = np.array(profile_faces)
    
    frontal_faces = frontal_faces.tolist()
    profile_faces = profile_faces.tolist()
    
    all_faces = frontal_faces + profile_faces
    
    
    
    # Verificar si hay al menos dos caras detectadas
    if len(all_faces) >= 2:
        # Iterar sobre todas las combinaciones de pares de caras
        for pair in itertools.combinations(all_faces, 2):
            # Calcular el área de intersección entre las caras
            iou = intersection_over_union(pair[0], pair[1])
            # Si el área de intersección es mayor al 80% del área de una de las caras, eliminar una de ellas
            if iou >= IOU_THRESHOLD:
                # Eliminar una de las caras
                if pair[0] in all_faces:
                    all_faces.remove(pair[0])
                    

    draw_face_rectangle(frame, all_faces)
    #draw_face_rectangle(frame, profile_faces)

    # Mostrar el cuadro con los rostros detectados
    cv2.imshow('Detector de rostros en tiempo real', frame)

    # Romper el bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el objeto de captura y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
