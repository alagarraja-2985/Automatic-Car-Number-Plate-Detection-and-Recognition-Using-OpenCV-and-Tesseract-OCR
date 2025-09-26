# License Plate Detection and Recognition

An end-to-end Python system to automatically **detect car license plates** and **extract their text numbers** using OpenCV and Tesseract OCR.  
Supports processing of live webcam video, video files, or a dataset of static images.

---

## Features

- Detect number plates using Haar Cascade classifier
- Extract text from detected plates using Tesseract OCR
- Works with webcam, video files, image datasets
- Outputs bounding boxes and OCR results
- Easy to adapt and extend

---

## Directory Structure

LicensePlateRecognition/
│
├── data/
│ └── number_plate/ # Image dataset for number plate recognition
│ └── haarcascade_russian_plate_number.xml
│
├── src/
│ ├── car_number_plate_v1.py # Basic detection (bounding boxes)
│ ├── car_number_plate_v2.py # Detection + OCR (for images)
│ └── car_number_plate_v3.py # Unified (webcam, video, folder)
│
├── sample_video.mp4 # (Optional) Demo video sample
├── README.md
├── requirements.txt


---

## Setup

1. **Clone the repository:**
    ```
    git clone https://github.com/yourusername/LicensePlateRecognition.git
    cd LicensePlateRecognition
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Install Tesseract OCR:**
    - Download and install from:  
      https://github.com/UB-Mannheim/tesseract/wiki  
    - Update the script path if necessary:
      ```
      pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
      ```

---

## Usage

- **Run unified script (choose webcam, video, or images):**
    ```
    python src/car_number_plate_v3.py
    ```

- **Run just number plate detection on images:**
    ```
    python src/car_number_plate_v1.py
    ```

- **Run number plate detection & OCR on images:**
    ```
    python src/car_number_plate_v2.py
    ```

> The scripts will prompt to select input and paths as needed.

---

## Requirements

- Python 3.x
- OpenCV
- Pytesseract
- Tesseract-OCR (system installed)

Your `requirements.txt` should contain:


---

## Example Output

- Detected license plate will be shown with a green rectangle.
- Extracted number will be printed in the console, e.g.:
    ```
    Detected Number Plate Text: MH12AB1234
    ```

---

## Notes

- If using your own dataset, put images inside `data/number_plate/`.
- You must have `haarcascade_russian_plate_number.xml` in the same `data` folder.

---

## License

This project is open-source and available under the MIT License.

---