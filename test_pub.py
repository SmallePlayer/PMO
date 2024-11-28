from PMO import *

topic = "krolik"

pub = PMO("192.168.1.139", '2000', topic)

pub.publish_frame(0)
