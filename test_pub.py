from PMO import *
import config

topic = "krolik"

pub = PMO("192.168.43.178", '2000', topic)

pub.publish_frame(0)
