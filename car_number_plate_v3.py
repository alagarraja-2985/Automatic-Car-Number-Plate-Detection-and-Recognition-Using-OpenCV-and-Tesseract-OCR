import cv2
import os
import pytesseract

# Configure Tesseract executable path if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cascade_path = r'C:\Users\alaga\Desktop\project\IOC\haarcascade_russian_plate_number.xml'
default_img_folder = r'C:\Users\alaga\Desktop\project\IOC\car number plate'
default_video_path = r'C:\Users\alaga\Desktop\project\IOC\sample_video.mp4'  # Change if you want a default

plate_cascade = cv2.CascadeClassifier(cascade_path)
if plate_cascade.empty():
    print("Error: Cascade did not load. Check the XML file path.")
    exit(1)
def detect_and_ocr(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(25, 25))
    for (x, y, w, h) in plates:
        plate_img = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Number Plate", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        plate_gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
        _, plate_thresh = cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY)
        text = pytesseract.image_to_string(plate_thresh, config='--psm 7')
        print(f"Detected Number Plate Text: {text.strip()}")
    return frame

def process_images(folder):
    for img_name in os.listdir(folder):
        img_path = os.path.join(folder, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue
        annotated_img = detect_and_ocr(img)
        resized_img = cv2.resize(annotated_img, (1080, 1920))
        cv2.imshow("Result", resized_img)
        key = cv2.waitKey(0)
        if key == 27:  # ESC key to break
            break
    cv2.destroyAllWindows()

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file {video_path}")
        return
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        annotated_frame = detect_and_ocr(frame)
        resized_frame = cv2.resize(annotated_frame, (1080, 1920))
        cv2.imshow("Video Result", resized_frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break
    cap.release()
    cv2.destroyAllWindows()

def process_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error opening webcam")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        annotated_frame = detect_and_ocr(frame)
        resized_frame = cv2.resize(annotated_frame, (1080, 1920))
        cv2.imshow("Webcam Result", resized_frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    print("Choose input type:")
    print("1: Live Webcam")
    print("2: Video File")
    print("3: Image Folder")
    choice = input("Enter 1, 2 or 3: ").strip()

    if choice == '1':
        print("Starting Live Webcam...")
        process_webcam()
    elif choice == '2':
        video_path = input(f"Enter video file path (press enter for default '{default_video_path}'): ").strip()
        if not video_path:
            video_path = default_video_path
        process_video(video_path)
    elif choice == '3':
        folder_path = input(f"Enter image folder path (press enter for default '{default_img_folder}'): ").strip()
        if not folder_path:
            folder_path = default_img_folder
        process_images(folder_path)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
