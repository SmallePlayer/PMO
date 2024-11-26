from PMO import *
import config

topic = "krolik"

pub = PMO(config.host, config.port, topic)

pub.publish_frame(0)
