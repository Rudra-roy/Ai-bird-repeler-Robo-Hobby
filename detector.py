import cv2
import time
from ultralytics import YOLO
import subprocess

# Load the YOLOv8 model
model = YOLO('best_model_2.pt')

target_class_name = 14

# Initialize the camera
camera = cv2.VideoCapture(0)  # Change 0 to the camera index

def detect_birds():
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        
        results = model(frame)
        i=-1
        for box in results:
            i+=1
            # x1, y1, x2, y2 = box.boxes.xyxy[0]
            class_name = box.boxes.cls
            conf = box.boxes.conf
            print(class_name)
            print(conf)
            if class_name[i]== target_class_name:
                if conf[i] > 0.20:
                    print("Bird detected!")
                    play_sound()
                    time.sleep(1)  # Wait for the sound to play
                    break

def play_sound():
    subprocess.run(["python3", "play_sound.py"])

if __name__ == "__main__":
    detect_birds()
