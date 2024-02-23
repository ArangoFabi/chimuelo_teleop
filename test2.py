import serial
import time

# Ajusta el puerto serial de acuerdo a tu configuración
ser = serial.Serial('COM4', 115200)  # Cambia 'COM3' al puerto serial de tu Arduino

def enviar_comando(comando):
    ser.write((comando + '\n').encode())
    time.sleep(0.25)  # Espera breve para asegurar que el comando se envíe

while True:
    # Menú de comandos
  
    opcion = input("tecla: ")

    if opcion == "q":
        enviar_comando("q") 
    

    elif opcion == "e":
        enviar_comando("e")


    elif opcion == "z":
        enviar_comando("z")


    elif opcion == "c":
        enviar_comando("c")

        

    elif opcion == "s":
        enviar_comando("s")

        
    elif opcion == "w":
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# Cierra el puerto serial cuando hayas terminado
ser.close()
