import os

# imagen a encriptar
image_path = 'image.jpg'

# encriptar imagen
def encrypt_image(image_path, output_path):
    key = os.urandom(8)  # genera una clave aleatoria de 8 bytes

    with open(image_path, 'rb') as file:  # abrir imagen en binario
        image_data = file.read()

    encrypted_image_data = bytearray(image_data)  # convierte la imagen en un byte-array

    # manipular bytes por metodo XOR
    for index, byte in enumerate(encrypted_image_data):
        encrypted_image_data[index] = byte ^ key[index % len(key)]  # XOR a cada byte

    with open(output_path, 'wb') as file:  # guardar imagen encriptada
        file.write(encrypted_image_data)

    return key  # retornar clave utilizada para encriptar

# desencriptar imagen
def decrypt_image(encrypted_image_path, key, output_path):
    with open(encrypted_image_path, 'rb') as file:  # Abrir la imagen
        encrypted_image_data = file.read()  # Leer datos de la imagen

    decrypted_image_data = bytearray(encrypted_image_data)  # Convertir datos en byte-array para modificarlos

    # Aplicar XOR con la clave para utilizada para encriptar
    for index, byte in enumerate(decrypted_image_data):
        decrypted_image_data[index] = byte ^ key[index % len(key)]  # XOR a cada byte

    with open(output_path, 'wb') as file:  # guardar imagen desencriptada
        file.write(decrypted_image_data)

# menu en terminal
def menu():
    while True:
        print("\nOpciones:")
        print("1. Encriptar imagen")
        print("2. Desencriptar imagen")
        print("3. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':
            key = encrypt_image(image_path, 'image_encrypted.jpg')  # encripta la imagen y guardar la clave
            print("Imagen encriptada y guardada como 'image_encrypted.jpg'")
            with open('image_key.bin', 'wb') as key_file:  # guardar la clave en un archivo .bin
                key_file.write(key)
            print("Clave de encriptación guardada en 'image_key.bin'")

        elif choice == '2':
            if os.path.exists('image_key.bin'):  # verificamos si el archivo de clave existe en la misma carpeta
                with open('image_key.bin', 'rb') as key_file:  # leer la clave
                    key = key_file.read()
                decrypt_image('image_encrypted.jpg', key, 'image_decrypted.jpg')  # usar clave para desencriptar la imagen
                print("Imagen desencriptada y guardada como 'image_decrypted.jpg'")
            else:
                print("No se encontró la clave de encriptación.")

        elif choice == '3':
            print("Saliendo del programa.")  # Terminar programa
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

menu()