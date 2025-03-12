import sys
import qrcode

print("oi")
parametro = str(sys.argv[1])
imagem = qrcode.make("www.google.com")
imagem.save("_qrcodes/"+ parametro + ".jpg")