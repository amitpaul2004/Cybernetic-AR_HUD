from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__, static_folder='static')

# serve index.html from project root
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# optional: serve other static files if needed
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    # debug=True helps during development (auto reload)
    app.run(host='127.0.0.1', port=5000, debug=True)
