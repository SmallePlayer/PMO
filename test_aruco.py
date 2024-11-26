from PMO import *
import config
import  time

topic = "krolik"

sub = PMO(config.host, config.port, topic)

while True:
    frame = sub.subscriber_frame()
    time.sleep(1)
    ids = sub.aruco_detect_id(frame,True)
    print(ids)
