import serial
import time
import random

def send_serial_message(port, baudrate, message, header):
    """
    Sends a message over a serial connection with a header byte (18-24).
    
    :param port: Serial port (e.g., "COM3" or "/dev/ttyUSB0")
    :param baudrate: Baud rate for communication
    :param message: The string message to send
    """
    try:
        # Open serial connection
        ser = serial.Serial(port, baudrate, timeout=1)

        main_message = message.encode("utf-8")
        header_bytes = bytes([header, len(main_message)])

        # Convert to bytes: Header (1 byte) + Message (encoded to bytes)
        # Send the data
        ser.write(header_bytes)
        ser.write(main_message)


        print(header_bytes)
        print(f"Sent: {main_message}")

        # Close serial connection
        ser.close()

    except serial.SerialException as e:
        print(f"Error: {e}")

msgs = [
    'Hello world!',
    '你好世界',
]

send_serial_message("/dev/ttyUSB0", 115200, "Hello, ", 20)  # Change "COM3" to match your serial port
time.sleep(0.02)
send_serial_message("/dev/ttyUSB0", 115200, "world!", 16)  # Change "COM3" to match your serial port
time.sleep(2)
send_serial_message("/dev/ttyUSB0", 115200, "world!", 20)  # Change "COM3" to match your serial port

