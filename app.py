from flask import Flask, render_template, Response
import torch
import cv2

app = Flask(__name__)

# Load the custom-trained YOLOv5 model
model = torch.hub.load('yolov5', 'custom', path='best.pt', source='local')  # Ensure best.pt is in your root

# Generate video frames using OpenCV and save annotated video
def gen_frames():
    cap = cv2.VideoCapture(r'C:\\object_detect\\video.mp4')

    # VideoWriter setup
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter('output_annotated.mp4', fourcc, fps, (width, height))

    while True:
        success, frame = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # restart the video
            continue

        # Detect objects using the model
        results = model(frame)
        annotated_frame = results.render()[0]

        # Save the frame to video
        out.write(annotated_frame)

        # Encode the frame to JPEG
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        # Yield the frame in a streaming-compatible format
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()
    out.release()

@app.route('/')
def index():
    return render_template('index.html')  # Ensure templates/index.html exists

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
