from PMO import *


topic = "krolik"

pub = PMO("192.168.43.34", '2000', topic)

pub.publish_frame(0)
