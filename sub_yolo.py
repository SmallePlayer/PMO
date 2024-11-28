from PMO import *
from ultralytics import YOLO
import  time

topic = "krolik"

sub = PMO("192.168.43.178", "2000", topic)

while True:
    frame = sub.subscriber_frame()
    time.sleep(1)
    class_id = sub.yolo_detect("11", "n", frame, True)
    print(class_id)
