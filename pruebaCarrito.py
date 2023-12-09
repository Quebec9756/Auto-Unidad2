import speech_recognition as sr
import serial

# CONFIGURACIÓN PARA LA CONEXIÓN CON ARDUINO ###
puerto = 'COM3'
arduino = serial.Serial(puerto, 9600)
################################################

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
        comando = 0
    elif cadena == "izquierda":
        comando = 1
    elif cadena == "derecha":
        comando = 2
    elif cadena == "detente":
        comando = 3
    else:
        print("Comando no reconocido")

    ## ENVÍO DE LA INSTRUCCIÓN AL ARDUINO ###########################
    if type(comando) == int:
        arduino.write(comando.encode())



######## EXCEPCIONES ################################################
except sr.UnknownValueError:
    print("Unknown Value Error")
except sr.RequestError as e:
    print("Request error:", format(e))
except Exception as ex:
    print("Error:", format(ex))
#####################################################################