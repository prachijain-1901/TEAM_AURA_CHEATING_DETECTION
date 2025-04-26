# TEAM_AURA_CHEATING_DETECTION
🎯 An AI-powered cheating detection system using YOLOv5 for Offline Exams.
🚀 Project Overview:
Ensuring fairness in offline exams is challenging due to human limitations in detecting cheating. It is an AI-powered system that integrates with live CCTV feeds and connects invigilators via a web or mobile application, delivering real-time alerts through notifications.It uses computer vision to analyze body and hand movements, identifying suspicious behaviors such as posture shifts, note passing, or turning around.
Powered by YOLOv5, the system also detects prohibited items like mobile phones,hidden paper chits.

📂 Project Structure

├── yolov5/                 # YOLOv5 model & scripts

├── test/                   # Test images/videos for detection

├── templates/              # Web interface files

├── static/                 # CSS & styling elements

├── output_annotated.mp4    # Processed detection results

├── data.yaml               # Dataset configuration

├── best.pt                 # Trained YOLOv5 model weights

├── app.py                  # Main application script

├── README.md               # Project documentation


⚙️ Installation & Setup


1️⃣ Clone this repository:

git clone https://github.com/prachijain-1901/TEAM_AURA_CHEATING_DETECTION.git


2️⃣ Install dependencies:

pip install -r requirements.txt


3️⃣ Run the application:

python app.py


🎥 Usage Guide
- Upload video/images for cheating detection.
- The YOLOv5 model processes input and highlights potential cheating instances.
- Detection results are saved as output_annotated.mp4
  

📊 Model & Performance
- Model Used: YOLOv5
- Detection Accuracy:
  ![Screenshot 2025-04-26 111052](https://github.com/user-attachments/assets/221b0bbc-59bf-40c1-97bf-e73c2c2011f1)
- Results:
- ![Screenshot 2025-04-26 110906](https://github.com/user-attachments/assets/e70d7e50-6b9d-4a45-9d0f-4d94acd02637)


