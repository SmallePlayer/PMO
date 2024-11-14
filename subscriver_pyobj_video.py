import zmq
import cv2

def video_read(host, port, topic_name):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    socket.connect(f"tcp://{host}:{port}")

    socket.setsockopt_string(zmq.SUBSCRIBE, '')
    while True:
        string = socket.recv_string()
        if (string == topic_name):
            messages = socket.recv_pyobj()
            cv2.imshow('Client 1', messages)
            key = cv2.waitKey(30)
