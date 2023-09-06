from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO

# import eventlet
# eventlet.monkey_patch()


app = Flask(__name__)
socketio = SocketIO(app,async_mode="eventlet")

clipboard_contents = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'save_server' in request.form:
        new_content = request.form['content']
        clipboard_contents.append(new_content)
        socketio.emit('new_content', new_content)  # Emitting a new_content event to all connected clients.
        return redirect(url_for('index'))
    return render_template('clipboard.html', contents=clipboard_contents)

@app.route("/clear-clipboard", methods=['POST'])
def clear_clipboard():
    clipboard_contents.clear()  # Clear the list
    return "Clipboard cleared", 200


if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=8080)
    # eventlet.wsgi.server(eventlet.listen(('', 8080)), app)