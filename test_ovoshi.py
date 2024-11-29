from PMO import *
import  time
import uart
import detect_ovoshi

topic = "krolik"

sub = PMO("192.168.43.178", "2000", topic)

while True:
    frame = sub.subscriber_frame()
    ovoshi_ = detect_ovoshi.detect_ovosh(frame,False)
    if ovoshi_ == "grysha":
        uart.send_array(0)
    elif ovoshi_ == "red_perec":
        uart.send_array(5)
    elif ovoshi_ == "lemon":
        uart.send_array(6)
    print(ovoshi_)
