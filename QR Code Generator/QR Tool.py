import os
import qrcode
import cv2
from pyzbar.pyzbar import decode

def generator(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

def reader(image_path):
    img = cv2.imread(image_path)
    detected_barcodes = decode(img)

    for barcode in detected_barcodes:
        qr_data = barcode.data.decode('utf-8')
        print(f"\nDetected QR code data: {qr_data}")
        return qr_data

    print("\nNo QR code found.")
    return None

choice = input("Do you want to (g)enerate QR code for a link or (r)etrieve link from QR Code? (g/r): ").lower()

if choice == 'g':
    link = input("Enter the URL or text to encode into a QR code: ")
    name = os.path.join(os.getcwd(), "qr_code.png")
    generator(link, name)
elif choice == 'r':
    path = input("Enter the path to the QR code image: ")
    reader(path)
else:
    print("Invalid choice. Please enter 'g' to generate or 'r' to retrieve.")
