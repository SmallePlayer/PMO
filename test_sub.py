from PMO import PMO
import config

topic = "krolik"

pub = PMO("192.168.43.73", "2000", topic)

pub.subscriber_frame()