import socket
import threading

IP = "0.0.0.0"
PORT = 6789
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    # TCP connection set up
    connected = True
    while connected:
        # Interpret the message sent from the client
        msg = conn.recv(SIZE).decode(FORMAT)
        filename = msg.split()[1]
        f = open(filename[1:])
        print(f"[{addr}] {msg}")

        outputdata = f.read()
        # Send the connection message
        conn.send(bytes("HTTP/1.1 200 OK","UTF-8"))
        conn.send(outputdata.encode())

    conn.close()
        # break

def main():
    print("[STARTING] Server is starting...")
    # Create a server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to server address: IP and Port
    server.bind(ADDR)
    # Ask the server to listen to multiple connections
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        # Create a main thread
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
