import serial
import random

def send_serial_message(port, baudrate, message, headerbits):
    """
    Sends a message over a serial connection with a header byte (18-24).
    
    :param port: Serial port (e.g., "COM3" or "/dev/ttyUSB0")
    :param baudrate: Baud rate for communication
    :param message: The string message to send
    """
    try:
        # Open serial connection
        ser = serial.Serial(port, baudrate, timeout=1)

        # Generate a random header between 0 and 7
        header = int(headerbits,2)

        # Convert to bytes: Header (1 byte) + Message (encoded to bytes)
        data_to_send = bytes([header]) + message.encode("utf-8")

        # Send the data
        ser.write(data_to_send)
        print(f"Sent: {data_to_send}")
        print(header)

        # Close serial connection
        ser.close()

    except serial.SerialException as e:
        print(f"Error: {e}")

# Example Usage
send_serial_message("COM3", 115200, "fsa",'0b110')  # Change "COM3" to match your serial port
#leftmost bit: completed/no
#middle bit: transcribe(0)/translate(1)
#rightmost bit: left speaker(0)/right speaker(1)