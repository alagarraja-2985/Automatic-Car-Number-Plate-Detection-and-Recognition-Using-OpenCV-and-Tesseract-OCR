import cv2
import os
import pytesseract

# Specify the installed location of Tesseract executable:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cascade_path = r'C:\Users\alaga\Desktop\project\IOC\haarcascade_russian_plate_number.xml'
img_folder = r'C:\Users\alaga\Desktop\project\IOC\car number plate'

plate_cascade = cv2.CascadeClassifier(cascade_path)
if plate_cascade.empty():
    print("Error: Cascade did not load. Check the XML file path.")
    exit(1)

for img_name in os.listdir(img_folder):
    img_path = os.path.join(img_folder, img_name)
    img = cv2.imread(img_path)
    if img is None:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(25, 25))

    for (x, y, w, h) in plates:
        plate_img = img[y:y+h, x:x+w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, "Number Plate", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        plate_gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
        _, plate_thresh = cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY)

        text = pytesseract.image_to_string(plate_thresh, config='--psm 7')
        print(f"Detected Number Plate Text: {text.strip()}")

    cv2.imshow("Result", img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
