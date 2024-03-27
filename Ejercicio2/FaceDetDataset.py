import cv2
import os

from utils import detect_faces, draw_face_rectangle

path = './part1_UTKface'

output_path = './part1_UTKface_detected'

os.makedirs(output_path, exist_ok=True)


path_images = os.listdir(path)

max_images = 40
count = 0

for image in path_images:
    if count >= max_images:
        break
    image_path = os.path.join(path, image)
    frame = cv2.imread(image_path)
    frontal_faces, profile_faces = detect_faces(frame)

    draw_face_rectangle(frame, frontal_faces)
    draw_face_rectangle(frame, profile_faces)

    # save the image with the rectangles
    output_image_path = os.path.join(output_path, image)
    cv2.imwrite(output_image_path, frame)

    count += 1
