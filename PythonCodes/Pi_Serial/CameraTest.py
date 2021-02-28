from flask import Flask, Response
import cv2

cam = cv2.VideoCapture(0)

def gen_frames():
    while True:
        success, frame = cam.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

app = Flask(__name__)
@app.route("/")
def index():
    return 'video feed'

@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':
    app.run(debug=True, port=80, host='192.168.86.128')
    