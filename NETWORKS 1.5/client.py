import socket

def main():
    # Overview and menu (client "left side")
    print("========== TAM Sorting Client ==========\n")
    print("Overview: This client sends a TAM string (letters T, A, M ending with '#') to the server,\n")
    print("and then displays the sorted result received back from the server.\n")
    print("========================================")
    
    HOST = '127.0.0.1'  # server's hostname or IP address
    PORT = 12345        # server's port

    while True:
        print("\nMenu:")
        print("1. Enter TAM string and send to server")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            tam_input = input("Enter TAM string ending with '#': ").strip()
            if not tam_input.endswith('#'):
                print("Error: The string must end with '#'")
                continue
            # Create a socket connection to the server.
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.connect((HOST, PORT))
                except ConnectionRefusedError:
                    print("Could not connect to the server. Make sure the server is running.")
                    continue
                # Send the TAM string to the server.
                s.sendall(tam_input.encode())
                # Wait for the sorted result from the server.
                data = s.recv(1024)
                if not data:
                    print("No response received from the server.")
                    continue
                sorted_str = data.decode()
                print("Received sorted TAM string from server:", sorted_str)
        elif choice == '2':
            print("Exiting client...")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == '__main__':
    main()

