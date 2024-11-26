from PMO import *
import uart
import config

def main():
    ua = PMO(ip_addr=config.host, port=config.port, topic="uart")
    data = [100,0,-98,12]
    ua.uart_send(data)
    print(f"Отправляю данные: {data}")
    response = ua.uart_read()
    print(f"response: {response}")

if __name__ == "__main__":
    main()