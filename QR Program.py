/* Generate QR code using python:-

QR CODE- Quick response Code

STEPS TO FOLLOW:-
Install module 'qrcode'using pip(terminal-pip install qrcode) install packages */

--------------PROGRAM TYPE 1------------------
import qrcode
img = qrcode.make('https://www.linkedin.com/in/er-shubham-kumar-b4028b296')
print(type(img))  # qrcode.image.pil.PilImage
img.save("qrr.png")
print("qr code successful")

----------PROGRAM TYPE 2----------------------


import qrcode
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
)
qr.add_data('https://www.linkedin.com/in/er-shubham-kumar-b4028b296')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
imag.save("text.png")