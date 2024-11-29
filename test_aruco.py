from PMO import *
import  time
import uart

topic = "krolik"

sub = PMO("192.168.43.178", "2000", topic)

while True:
    frame = sub.subscriber_frame()
    ids = sub.aruco_detect_id(frame,True)
    if ids == 20:
        uart.send_array(ids)
    print(ids)
