from PMO import *
import  time

topic = "krolik"

sub = PMO("192.168.1.139", "2000", topic)

while True:
    frame = sub.subscriber_frame()
    ids = sub.aruco_detect_id(frame,True)
    print(ids)
