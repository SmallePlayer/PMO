import time
import uart

def main():
    data = [4, 3, 2, 1]
    while True:
        uart.send_array(data)
        print(f"Отправляю данные: {data}")
        response = uart.read_response()
        print(f"response: {response}")
        data = [x*2 for x in response]
        time.sleep(0.1)

if __name__ == "__main__":
    main()