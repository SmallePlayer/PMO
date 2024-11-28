import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200)
time.sleep(2)  # Ожидание инициализации соединения


def send_array(arr):
    """Отправка массива из 4 целых чисел."""
    #print(f"Отправляю данные: {arr}")
    ser.write(f"{arr}".encode())


def read_response():
    """Чтение ответа от Arduino."""
    response = []
    line = ser.readline().decode().strip()
    parts = line.split()
    for part in parts:
        try:
            value = int(part)
            response.append(value)
        except ValueError:
            pass
    return response