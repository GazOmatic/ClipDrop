from bottle import Bottle, request, template, redirect, response

app = Bottle()

clipboard_contents = []

@app.route("/", method=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'save_server' in request.forms:
        new_content = request.forms.get('content')
        clipboard_contents.append(new_content)
        redirect("/")
    return template('clipboard', contents=clipboard_contents)

@app.route('/events')
def sse():
    def event_stream():
        count = len(clipboard_contents)
        while True:
            if len(clipboard_contents) > count:
                count = len(clipboard_contents)
                yield f"data: {clipboard_contents[-1]}\n\n"

    response.content_type = "text/event-stream"
    response.cache_control = "no-cache"
    response.connection = "keep-alive"
    return event_stream()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True,reloader=True)

