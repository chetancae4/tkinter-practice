#QRCODE GEANRATOR
import qrcode
qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
data="chetan shirpa not infected with corona"  #when we scan genarated qrcode it will display hello iam qrcode
qr.add_data(data)  #adding text to qr code
qr.make(fit=True)
img=qr.make_image(fill='black',back_ground='white')
img.save('1.png')
#see a png file of qr code is created in this folder