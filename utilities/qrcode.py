import qrcode

print("--------------------")
print("📱 QR CODE GENERATOR")
print("--------------------")

# Get input from the user
data = input("Enter text or URL: ")

# Create QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create image
image = qr.make_image(
    fill_color="black",
    back_color="white"
)

# Save the QR code
image.save("my_qr_code.png")

print("\n✅ QR code generated successfully!")
print("📁 Saved as: my_qr_code.png")