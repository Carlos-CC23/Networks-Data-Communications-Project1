# Networks-Data-Communications-Project
First project for networks and data communications for the Spring 2025 semester.

To run the server and client code in Visual Studio Code, follow these steps:

1. Open VS Code and create a new folder for your project (or open an existing folder).

2. Inside that folder, create three files: server.py, client.py, and gui_client.py, then paste the corresponding code into each file.

3. Make sure you have Python installed and that the Python extension is enabled in VS Code.

4. Open the integrated terminal in VS Code by selecting Terminal > New Terminal.

5. First, run gui_client:
   • In the terminal, type:  
  python3 gui_client.py  
   (On Windows, you might need to type:  
  python gui_client.py)

6. The gui_client will open a window with Menu. it'll have 3 buttons you can press. To enter a string, you'll need to follow the next step.

7. Open a second terminal instance in VS Code:
   • You can click the plus icon (+) in the terminal panel to open another terminal.
   
8. In the new terminal, run the server:
   • Type:  python3 server.py  
   (Or on Windows:  
  python server.py)

9. Now you enter the string on the window opened. Read instructions before typing and hitting enter.
    
**Note: Every time the string is sorted, the server connection is gone. In order to get a new string to get sorted again, you'll need to run the server again.**

By following these steps, you'll have the gui_client running in one terminal and the server in another, allowing them to communicate as designed.
