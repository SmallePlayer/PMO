from PMO import *
import config

topic = "krolik"

sub = PMO("192.168.41.24", config.port, topic)

sub.subscriber_frame()

