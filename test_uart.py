import PMO
import uart


def main():
    data = uart.read()
    print(data)
    uart.write(data)

if __name__ == "__main__":
    main()