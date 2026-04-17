import qrcode

def generar_qr(data, nombre_archivo="qr.png"):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)
    print(f"QR generado: {nombre_archivo}")


print("1) URL (imagen, video, web)")
print("2) Texto")
opcion = input("Elige opción:\n")

if opcion == "1":
    url = input("Ingresa la URL:\n")
    generar_qr(url, "qr_url.png")

elif opcion == "2":
    texto = input("Ingresa el texto:\n")
    generar_qr(texto, "qr_texto.png")

else:
    print("Opción inválida")