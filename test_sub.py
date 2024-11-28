from PMO import *


topic = "krolik"

sub = PMO("192.168.43.178", "2000", topic)
while True:
    frame = sub.subscriber_frame()
    sub.subscriber_qr(True)
    sub.aruco_detect_id(frame, True)