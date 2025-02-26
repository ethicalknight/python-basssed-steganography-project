import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")

# Read the password and message length from the file
with open("password.txt", "r") as f:
    password = f.readline().strip()  # Read the password
    msg_length = int(f.readline().strip())  # Read the message length

# Recreate the dictionary for value-to-character mapping
c = {i: chr(i) for i in range(255)}

# Input password for decryption
pas = input("Enter passcode for Decryption:")

# Check if the password is correct
if password == pas:
    # Initialize variables for pixel extraction
    message = ""
    n = 0
    m = 0
    z = 0

    # Extract the secret message from the image
    for _ in range(msg_length):  # Use the saved message length
        char = c[img[n, m, z]]  # Extract the character from the pixel
        print(f"Decrypted: {img[n, m, z]} -> {char} at ({n}, {m}, {z})")  # Debug
        message += char
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through the RGB channels

    # Display the decrypted message
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
