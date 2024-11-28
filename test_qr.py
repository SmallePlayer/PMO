from PMO import *
import  time

topic = "krolik"

sub = PMO("192.168.43.178", "2000", topic)

while True:
    ids = sub.subscriber_qr(True)
    print(ids)
