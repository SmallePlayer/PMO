import zmq
import time
import cv2
import base64
import numpy as np

import config
import uart
from publish_pyobj_video import video_potok
from subscriver_pyobj_video import video_read
from ultralytics import YOLO


class PMO:
    def __init__(self, ip_addr=config.host, port=config.port, topic="pmo"):
        self.ip_address = ip_addr
        self.port_host = port
        self.name_topic = topic

    def publish_string(self, data: str, delay: int):
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

    def publish_video(self, video_path, show: bool):
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

    def publish_frame(self, video_path):
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind(f"tcp://{self.ip_address}:{self.port_host}")
        cap = cv2.VideoCapture(video_path)
        while True:
            encode_frame = PMO.__capture_camera(self,cap)
            socket.send_string(f"{self.name_topic} {encode_frame}")

    def subscriber_frame(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(f"tcp://{self.ip_address}:{self.port_host}")
        socket.setsockopt_string(zmq.SUBSCRIBE, self.name_topic)
        while True:
            data = socket.recv_string()
            topic, encode_frame = data.split(' ', maxsplit=1)
            frame = PMO.__decoding_frame(self, encode_frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break


        cv2.waitKey()
        cv2.destroyAllWindows()

    def __capture_camera(self, cap):
        ret, frame = cap.read()
        success, encoded_frame = cv2.imencode('.jpg', frame)
        jpg_frame_text = base64.b64encode(encoded_frame).decode('utf-8')
        return jpg_frame_text

    def __decoding_frame(self, encode_frame):
        img = base64.b64decode(encode_frame)
        nparray = np.frombuffer(img, np.uint8)
        frame = cv2.imdecode(nparray, cv2.IMREAD_COLOR)
        return frame

    def uart_send(self):
        uart.write()

    def uart_recv(self):
        data = uart.read()
        print(data)

    def yolo_detect(self, version: str, weight: str, frame, show: bool):
        model = YOLO(f'yolo{version}{weight}.pt')
        results = model.predict(source=frame, show=show, imgsz=640)
        result = results[0]
        for box in result.boxes:
            class_id = box.cls[0].item()
            return class_id
