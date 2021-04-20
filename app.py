import numpy as np
import cv2
from mss import mss
from PIL import Image
from screeninfo import get_monitors
from flask import Flask, render_template, Response

app = Flask(__name__)

monotor = get_monitors()[0]
cords = {'top':0 , 'left': 0 , 'width': monotor.width, 'height': monotor.height }

def gen_frames():  
    while True:
        with mss() as sct :
            img = np.array(sct.grab(cords))
            ret, buffer = cv2.imencode('.jpg', img)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/screen_0')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="192.168.31.38", debug=True)
