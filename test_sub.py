from PMO import *
import config

topic = "krolik"

sub = PMO("192.168.41.24", "2000", topic)

sub.subscriber_frame()

