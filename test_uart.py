import uart
import config

def main():
    data = [100,0,-98,12]
    uart.uart_send(data)
    print(f"Отправляю данные: {data}")
    response = uart.uart_read()
    print(f"response: {response}")

if __name__ == "__main__":
    main()