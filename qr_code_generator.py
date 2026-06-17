import qrcode

data = input("Enter URL or Text : ").strip()
filename = input("Enter Filename :").strip()

qr = qrcode.QRCode(box_size = 10, border = 4)
qr.add_data(data)

image = qr.make_image(fill_color = 'blue',back_color = 'white')
image.save(filename)

print(f'QR code saved as {filename}')