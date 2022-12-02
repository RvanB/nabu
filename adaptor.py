import serial
import time

conn = serial.Serial("/dev/tty.usbserial-A10KGEAX", baudrate=111000)

def write(connection, *values):
    connection.write(bytearray(values))

    print("Sent", ' '.join(map(hex, values)))


def main():
    print("Waiting for NPC...")
    
    res = conn.read()
    print("Well met!")
    write(conn, 0x10, 0x06, 0xe4)
    
    res = conn.read()
    print("Received", res)
    write(conn, 0x10, 0x06)

    res = conn.read()
    print("Received", res)
    write(conn, 0x9f, 0x10, 0xe1)
    
    
if __name__ == "__main__":
    main()


