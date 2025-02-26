import cv2
import os

# Load the image
img = cv2.imread("mypic.jpg")  # Replace with the correct image path

# Input secret message and password
msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Save the password and message length to a file for decryption
with open("password.txt", "w") as f:
    f.write(f"{password}\n{len(msg)}")  # Save password and message length

# Create dictionaries for character-to-value and value-to-character mapping
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Initialize variables for pixel manipulation
n = 0
m = 0
z = 0

# Embed the secret message into the image
for char in msg:
    img[n, m, z] = d[char]  # Embed the character into the pixel
    print(f"Encrypted: {char} -> {img[n, m, z]} at ({n}, {m}, {z})")  # Debug
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through the RGB channels

# Save the encrypted image in a lossless format (PNG)
cv2.imwrite("encryptedImage.png", img)

# Open the encrypted image (for Windows)
os.system("start encryptedImage.png")
