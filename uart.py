import serial
import struct

def read():
    ser_read = serial.Serial('/dev/ttyUSB0', 115200)

    array_size_bytes = ser_read.read(2)
    if len(array_size_bytes) != 2:
        print(f"Не удалось прочитать размер массива: {len(array_size_bytes)}")
        return None


    array_size = struct.unpack('<H',array_size_bytes)[0]
    print(f"Принят размер массива: {array_size}")

    received_array = []
    for _ in range(array_size):
        element_bytes = ser_read.read(2)
        if len(element_bytes) != 2:
            print("Не удалось прочитать элемент массива")
            break

        element = struct.unpack('<h',element_bytes)[0]
        received_array.append(element)
    print(f"Received array: {received_array}")
    return  received_array

def write(received_array):
    ser_write = serial.Serial('/dev/ttyUSB0',115200)
    response_array = [x*2 for x in received_array]
    response_length = len(response_array)

    ser_write.write(struct.pack('<H',response_length))

    for value in response_array:
        ser_write.write(struct.pack('<h',value))
    print(f"Sent Response: {response_array}")