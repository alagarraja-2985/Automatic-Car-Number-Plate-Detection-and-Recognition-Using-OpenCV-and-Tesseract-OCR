import cv2
import os

# Path to Haar Cascade XML for number plate detection
cascade_path = r'C:\Users\alaga\Desktop\project\IOC\haarcascade_russian_plate_number.xml' # Ensure this file is present in your directory

# Path to your folder containing car images
img_folder = r'C:\Users\alaga\Desktop\project\IOC\car number plate'

plate_cascade = cv2.CascadeClassifier(cascade_path)
if plate_cascade.empty():
    print("Error: Cascade did not load. Check file path and download.")
    exit(1)

# Load the Haar Cascade classifier
plate_cascade = cv2.CascadeClassifier(cascade_path)

# Check if the folder exists
if not os.path.isdir(img_folder):
    print(f"Folder not found: {img_folder}")
else:
    # Loop through each image in the folder
    for img_name in os.listdir(img_folder):
        img_path = os.path.join(img_folder, img_name)
        img = cv2.imread(img_path)

        # If image cannot be loaded, skip
        if img is None:
            continue

        # Convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect number plates
        plates = plate_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=4,
            minSize=(25, 25)
        )

        # Draw rectangles around detected plates
        for (x, y, w, h) in plates:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        # Display result
        cv2.imshow("Result", img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
