# Clipboard App

This is a small Flask-based web application for managing a simple clipboard. You can use this app to copy and save text entries with custom names, clear the clipboard, and delete specific entries. The app utilizes Flask for the web framework and Flask-SocketIO for real-time updates.

## Features

- **Copy and Save**: You can copy text content to the clipboard and give each entry a custom name. If you don't provide a name, a default name will be assigned.

- **Real-time Updates**: The app uses Flask-SocketIO to provide real-time updates when new entries are added or when entries are deleted.

- **Clear Clipboard**: You can clear the entire clipboard in one click.

- **Delete Entries**: You can delete individual entries from the clipboard.

## Installation

1. Clone this repository or download the `clipboard_app.py` file.

2. Install the required dependencies using pip:

   ```bash
   pip install flask flask-socketio eventlet
   ```

3. Run the application:

   ```bash
   python clipboard_app.py
   ```

The app will be accessible at `http://localhost:8080`.

## Usage

- Access the application in your web browser at `http://localhost:8080`.

- To copy and save text to the clipboard, enter the text in the input field and optionally provide a custom name. Click the "Save to Clipboard" button.

- To clear the entire clipboard, click the "Clear Clipboard" button.

- To delete individual entries, click the "Delete" button next to the entry you want to remove.

## Dependencies

- Flask: A micro web framework for Python.
- Flask-SocketIO: An extension for Flask that adds support for WebSocket-based communication.
- Eventlet: A concurrent networking library for Python that works with Flask-SocketIO.

## Notes

- By default, the app runs in debug mode and listens on `0.0.0.0:8080`. You can modify the host and port in the `if __name__ == "__main__":` block of the script.

- Eventlet is currently commented out in the code. If you decide to use it instead of the default WebSocket library, you can uncomment the relevant lines and install the Eventlet library.

Feel free to customize and extend this clipboard app for your needs. Enjoy using it!