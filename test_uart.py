import time
import uart

def main():
    data = [4, 3, 2, 1]
    while True:
        uart.send_array(data)
        print(f"Отправляю данные: {data}")

if __name__ == "__main__":
    main()