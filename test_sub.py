from PMO import *
import config

topic = "krolik"

sub = PMO(config.host, config.port, topic)

sub.subscriber_frame()

