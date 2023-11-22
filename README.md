# Image Encoder

## Descripción
El programa "Image Encoder" encripta y desencriptar imágenes. La encriptación aquí no es una seguridad criptográfica real, sino más bien una forma de modificar los datos de la imagen para que no puedan ser reconocidos a simple vista. Luego, el programa puede revertir estos cambios para restaurar la imagen a su estado original con una clave generada durante la encriptacion.

## Cómo funciona?
- **Encriptación**: El programa toma una imagen llamada `image.jpg` que esta en la misma carpeta y la procesa para cambiar sus datos. Esta imagen procesada se guarda con un nuevo nombre y no se puede leer o abrir normalmente.

- **Desencriptación**: Para volver a poder leer o abrir la imagen, el programa puede revertir el proceso de encriptación, utilizando una clave que se genera y guarda automáticamente durante la encriptación.

- **Clave de encriptación**: Es un pequeño archivo que el programa crea una clave en una archivo `.bin`, para recordar cómo revertir los cambios hechos a la imagen. Es crucial para el proceso de desencriptación.

## Instrucciones de Uso
### Preparación
1. **Ubicación de la Imagen**: Asegúrate de que haya una imagen llamada `image.jpg` en la misma carpeta que el programa.
2. **Abrir la terminal**: Necesitarás usar la Terminal de tu computadora para ejecutar el programa.

### Ejecución
1. **Navegar a la Carpeta del Programa**:
   - Navega a la carpeta donde guardaste el programa, te puedes apoyar con los comando `ls` para saber que carpetas hay y `cd + nombre carpeta` para moverte entre carpetas.
2. **Ejecutar el Programa**:
   - Escribe `python img_encoder.py` o `python3 img_encoder.py` en la Terminal y presiona Enter.

### Uso del Programa
- Una vez ejecutado, verás un menú con opciones.
- Elige la opción `1` para encriptar la imagen. Se creará una nueva imagen encriptada y un archivo con la clave.
- Elige la opción `2` para desencriptar la imagen usando el archivo de clave guardado.
- Elige la opción `3` para salir del programa.