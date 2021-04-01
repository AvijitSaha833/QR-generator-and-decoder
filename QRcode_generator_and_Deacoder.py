import qrcode
from pyzbar.pyzbar import decode
from PIL import Image         # have to install Pillow or PIL for save and make image


def file_location():
    tmp = input("Enter the location \n").split("\\")
    return ("/".join(tmp))
def encoder():
    qr = qrcode.QRCode(version=1,box_size=12,border=3)
    data=input("Enter your Massage\n")
    qr.add_data(data)
    qr.make(fit=True)
    img= qr.make_image(fill_color="black",back_color="white")
    path = file_location()
    file_name=input("Enter the image name with format (Example: abc.jpg)\n")
    img.save(path+"/"+file_name)

def decoder():
    path = file_location()
    print(decode(Image.open(path)))


if __name__ == '__main__':
    f=0
    f=int(input("Press:\n 1 to make QRCode\n 2 to decode QRCode\n"))
    if f==1:
        encoder()
    elif f==2:
        decoder()
    else:
        print("Wrong input try again!!")



