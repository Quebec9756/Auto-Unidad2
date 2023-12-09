import speech_recognition as sr
import serial
from pynput import keyboard

puerto = 'COM3'
arduino = serial.Serial(puerto, 9600)

print('Presiona ESPACIO para dictar un comando y ESC para cancelar:')
def on_press(key):
    if key == keyboard.Key.space:
        # RECONOCIMIENTO DE VOZ
        r = sr.Recognizer()
        print("Inicia...")
        with sr.Microphone() as source:
            audio = r.listen(source)
        print("Registro generado!")
        try:
            ## PROCESAMIENTO DEL DICTADO ####################################
            cadena = str(r.recognize_google(audio, language="es-MX")).lower()
            print("Mensaje: " + cadena)

            comando = ""

            if cadena == "avanza":
                comando = "0"
            elif cadena == "reversa":
                comando = "1"
            elif cadena == "izquierda":
                comando = "2"
            elif cadena == "derecha":
                comando = "3"
            elif cadena == "detente":
                comando = "4"
            else:
                print("Comando no reconocido.")

            print(comando)
            arduino.write(comando.encode())
            print('\nPresiona ESPACIO para dictar un comando y ESC para cancelar:')

        except sr.UnknownValueError:
            print("Unknown Value Error")
        except sr.RequestError as e:
            print("Request error:", format(e))
        except Exception as ex:
            print("Error:", format(ex))
    elif key == keyboard.Key.esc:
        listener.stop()

def on_release(key):
    print('Se liberó', key)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

