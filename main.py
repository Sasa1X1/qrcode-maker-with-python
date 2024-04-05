import qrcode
import time  # Import the time module for timestamp generation

# Generate the QR code image
img = qrcode.make(input("But A Link Or A Text: "))

# Create a unique and descriptive filename with a PNG extension
filename = f"qr_code_{round(time.time())}.png"  # Example: qr_code_1654345678.987654.png

# Save the image with the generated filename
img.save(filename)

print(f"QR code image saved as: {filename}")
