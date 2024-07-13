import cv2
import time
from ultralytics import YOLO
from picamera2 import Picamera2
import subprocess

# Load the YOLOv8 model
model = YOLO('best_model_2.pt')

target_class_name = 14

# Initialize the camera
dispW = 800
dispH = 800

picam2 = Picamera2()
picam2.preview_configuration.main.size = (dispW, dispH)
picam2.preview_configuration.main.format = 'RGB888'
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

webCam = '/dev/video2'
cam = cv2.VideoCapture(webCam)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
cam.set(cv2.CAP_PROP_FPS, 30)

def detect_birds():
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        
        results = model(frame)
        i=-1
        for box in results:
            i+=1
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
