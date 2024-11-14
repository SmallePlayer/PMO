import cv2
import zmq


def video_potok(Video_path, addr, port, topic, show):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(f"tcp://{addr}:{port}")

    while True:
        vid_capture = cv2.VideoCapture(Video_path)
        while vid_capture.isOpened():
            ret, frame = vid_capture.read()
            if ret:
                if show == True:
                    cv2.imshow('Server', frame)
                socket.send_string(topic)
                socket.send_pyobj(frame)
                key = cv2.waitKey(30)
            else:
                break
        vid_capture.release()
    else:
        cv2.destroyAllWindows()

