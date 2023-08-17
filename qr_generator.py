import qrcode

def generate_qr_code(data, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(output_path)

def main():
    num_qrs = int(input("Enter the number of QR codes to generate: "))
    entities = [f"Entity{i}" for i in range(1, num_qrs + 1)]

    for entity in entities:
        data = f"Entity: {entity}"
        output_path = f"{entity}_qr_code.png"
        generate_qr_code(data, output_path)
        print(f"Generated QR code for {entity} and saved as {output_path}")

if __name__ == "__main__":
    main()
