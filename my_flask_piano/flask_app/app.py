# flask_app/app.py
from flask import Flask, send_file, render_template_string
import threading
import os
from static.game import capture_screen, run_game  # Import your Pygame functions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <!doctype html>
        <title>Pygame Web App</title>
        <h1>Pygame Web App</h1>
        <img id="game_frame" src="/frame">
        <script>
            setInterval(function() {
                document.getElementById('game_frame').src = '/frame?' + new Date().getTime();
            }, 1000 / 30);  // Refresh the frame 30 times per second
        </script>
    ''')

@app.route('/frame')
def frame():
    return send_file('flask_app/static/screen.png', mimetype='image/png')

def run_flask():
    app.run(debug=True, host='0.0.0.0', port=5001)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    run_game()  # Run Pygame in the main thread
