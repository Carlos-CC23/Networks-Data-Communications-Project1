#!/usr/bin/env python3
import socket

def sort_tam_server(tam_tab):
    """Sorts the array tam_tab (list of characters) so that all 'T's come first,
    followed by all 'A's, then all 'M's. Uses a three-pointer approach."""
    low = 0
    mid = 0
    high = len(tam_tab) - 1
    while mid <= high:
        if tam_tab[mid] == 'T':
            if mid != low:
                # Swap the current element with the element at low.
                tam_tab[low], tam_tab[mid] = tam_tab[mid], tam_tab[low]
            low += 1
            mid += 1
        elif tam_tab[mid] == 'M':
            if mid != high:
                # Swap the current element with the element at high.
                tam_tab[mid], tam_tab[high] = tam_tab[high], tam_tab[mid]
            high -= 1
        else:
            # Letter is 'A'
            mid += 1
    return tam_tab

def main():
    # Overview and menu (server "right side")
    print("========== TAM Sorting Server ==========")
    print("Overview: This server receives a TAM string (letters T, A, M ending with '#'),")
    print("sorts it so that all T's appear first, then A's, and finally M's,")
    print("and sends the sorted string back to the client.")
    print("========================================\n")

    HOST = '127.0.0.1'  # localhost
    PORT = 12345        # arbitrary non-privileged port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print("Server listening on {}:{}".format(HOST, PORT))
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            data = conn.recv(1024)
            if not data:
                print("No data received.")
                return
            # Decode the received data and remove trailing '#' if present.
            tam_str = data.decode().strip()
            if tam_str.endswith('#'):
                tam_str = tam_str[:-1]
            print("Received TAM string:", tam_str)
            # Store the string in a list (TAM_TAB_Server)
            tam_tab = list(tam_str)
            # Sort the array using sort_tam_server.
            sorted_tab = sort_tam_server(tam_tab)
            sorted_str = ''.join(sorted_tab)
            print("Sorted TAM string:", sorted_str)
            # Send the sorted string back to the client.
            conn.sendall(sorted_str.encode())
            print("Sorted string sent to client.")
            
if __name__ == '__main__':
    main()
