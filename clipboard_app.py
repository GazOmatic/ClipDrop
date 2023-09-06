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
        entry_name = request.form.get('entry_name', '').strip()
        
        # If the name field is empty, use a default name
        if not entry_name:
            entry_name = f"Copy {len(clipboard_contents) + 1}"

        clipboard_contents.append((entry_name, new_content))
        socketio.emit('new_content', {'name': entry_name, 'content': new_content})
        
        return redirect(url_for('index'))
    return render_template('clipboard.html', contents=clipboard_contents)

@app.route("/clear-clipboard", methods=['POST'])
def clear_clipboard():
    clipboard_contents.clear()  # Clear the list
    return "Clipboard cleared", 200

@app.route("/delete/<int:item_index>", methods=['POST'])
def delete_item(item_index):
    if 0 <= item_index < len(clipboard_contents):
        del clipboard_contents[item_index]
        socketio.emit('delete_content', item_index)
    return redirect(url_for('index'))

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=8080)
    # eventlet.wsgi.server(eventlet.listen(('', 8080)), app)