import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import ImageTk, Image


def generate_qr_code():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if not file_path:
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    # Display the generated QR code
    img = Image.open(file_path)
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

    messagebox.showinfo("Success", f"QR code for {url} has been generated and saved to {file_path}")


# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place the URL entry widget
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10, padx=30)

# Create and place the Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=20)

# Create a label to display the generated QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Run the application
root.mainloop()
