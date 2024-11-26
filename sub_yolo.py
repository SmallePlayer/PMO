import PMO
import config
from ultralytics import YOLO
import  time

topic = "krolik"

sub = PMO(config.host, config.port, topic)

while True:
    frame = sub.subscriber_frame()
    time.sleep(1)
    class_id = sub.yolo_detect("11", "n", frame, True)
    print(class_id)
