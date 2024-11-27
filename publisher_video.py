from PMO import *
import config

topic = "krolik"

pub = PMO("192.168.43.73", '2000', topic)

pub.publish_video(0,True)
