import qrcode

print("       📱 QR CODE GENERATOR")
print("================================")

data = input("Enter text or URL: ")

if data.strip() == "":
    print("❌ You didn't enter anything.")
else:

    filename = input(
        "Enter file name (without .png): "
    )

    if filename.strip() == "":
        filename = "qr_code"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )
    image.save(filename + ".png")
    print("\n✅ QR CODE CREATED!")
    print("📁 File:", filename + ".png")