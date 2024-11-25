from PMO import *
import config
from ultralytics import YOLO
import  time

topic = "krolik"

sub = PMO("192.168.43.34", config.port, topic)

while True:
    frame = sub.subscriber_frame()
    time.sleep(1)
    class_id = sub.yolo_detect("11", "n", frame, False)
    print(class_id)
