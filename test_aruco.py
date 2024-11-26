from PMO import *
import config
import  time

topic = "krolik"

sub = PMO(config.host, config.port, topic)

while True:
    frame = sub.subscriber_frame()
    ids = sub.aruco_detect_id(frame,True)
    print(ids)
