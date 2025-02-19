import tkinter as tk
import socket

HOST = '127.0.0.1'  # server's IP address
PORT = 12345        # server's port

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TAM Sorting Client GUI")
        self.geometry("500x400")
        # Create container for frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MenuPage, OverviewPage, TAMInputPage):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(MenuPage)

    def show_frame(self, frame_class):
        """Bring a frame to the front."""
        frame = self.frames[frame_class]
        frame.tkraise()

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title = tk.Label(self, text="Main Menu", font=("Arial", 20))
        title.pack(pady=20)

        overview_btn = tk.Button(self, text="Overview", font=("Arial", 14),
                                 command=lambda: controller.show_frame(OverviewPage))
        overview_btn.pack(pady=10)

        tam_btn = tk.Button(self, text="1. Enter TAM string and send to server", font=("Arial", 14),
                            command=lambda: controller.show_frame(TAMInputPage))
        tam_btn.pack(pady=10)

        exit_btn = tk.Button(self, text="2. Exit", font=("Arial", 14),
                             command=self.quit)
        exit_btn.pack(pady=10)

class OverviewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        title = tk.Label(self, text="Overview", font=("Arial", 20))
        title.pack(pady=20)

        overview_text = (
            "This project implements a client-server system for sorting TAM strings. \n\n"
            "A TAM string consists of the letters T, A, and M and ends with a '#' character. \n\n"
            "The client sends the TAM string to the server, which sorts it so that all T's appear first, \n"
            "followed by A's, and finally M's. The server then sends the sorted string back to the client."
        )
        text_label = tk.Label(self, text=overview_text, font=("Arial", 12), wraplength=450, justify="left")
        text_label.pack(pady=10)

        back_btn = tk.Button(self, text="Back to Menu", font=("Arial", 14),
                             command=lambda: controller.show_frame(MenuPage))
        back_btn.pack(pady=10)

class TAMInputPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        title = tk.Label(self, text="Enter TAM String", font=("Arial", 20))
        title.pack(pady=20)
        
        # Input field for TAM string
        self.input_entry = tk.Entry(self, font=("Arial", 14), width=40)
        self.input_entry.pack(pady=10)
        # Hint label
        hint = tk.Label(self, text="Please enter a TAM string ending with '#'", font=("Arial", 12))
        hint.pack(pady=5)
        
        send_btn = tk.Button(self, text="Send", font=("Arial", 14),
                             command=self.send_tam_string)
        send_btn.pack(pady=10)
        
        # Label for displaying result or error message
        self.result_label = tk.Label(self, text="", font=("Arial", 12), fg="blue", wraplength=450)
        self.result_label.pack(pady=10)
        
        back_btn = tk.Button(self, text="Back to Menu", font=("Arial", 14),
                             command=lambda: controller.show_frame(MenuPage))
        back_btn.pack(pady=10)
    
    def send_tam_string(self):
        """Connects to the server, sends the TAM string, and displays the sorted result."""
        tam_input = self.input_entry.get().strip()
        if not tam_input.endswith('#'):
            self.result_label.config(text="Error: The string must end with '#'")
            return

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(tam_input.encode())
                data = s.recv(1024)
                if data:
                    sorted_str = data.decode()
                    self.result_label.config(text="Sorted TAM string: " + sorted_str)
                else:
                    self.result_label.config(text="No response received from the server.")
        except Exception as e:
            self.result_label.config(text=f"Error connecting to server: {e}")

if __name__ == '__main__':
    app = Application()
    app.mainloop()
