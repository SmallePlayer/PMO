import zmq
import time
import cv2
from publish_pyobj_video import video_potok
from subscriver_pyobj_video import video_read


class PMO:
    def __init__(self, ip_addr, port, topic):
        self.ip_address = ip_addr
        self.port_host = port
        self.name_topic = topic

    def publish_string(self, data, delay):
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind(f"tcp://{self.ip_address}:{self.port_host}")
        while True:
            message = f"{self.name_topic} {data}"
            socket.send_string(message)
            time.sleep(delay)

    def subscriber(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(f"tcp://{self.ip_address}:{self.port_host}")
        socket.setsockopt_string(zmq.SUBSCRIBE, self.name_topic)
        while True:
            data = socket.recv_string()
            return data

    def publish_video(self, video_path, show):
        video_potok(video_path,
                    self.ip_address,
                    self.port_host,
                    self.name_topic,
                    show
                    )

    def subscriber_video(self):
        video_read(self.ip_address,
                   self.port_host,
                   self.name_topic
                   )