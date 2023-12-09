import serial
from pynput import keyboard

puerto = 'COM3'
arduino = serial.Serial(puerto, 9600)

comandos = {
    'w': '0',  # Avanza
    's': '1',  # Reversa
    'a': '2',  # Izquierda
    'd': '3',  # Derecha
    'x': '4'   # Detener
}

comando_actual = comandos['x']
def enviar_comando(comando):
    global comando_actual
    if comando != comando_actual:
        arduino.write(comando.encode())
        comando_actual = comando
        print(f'Comando enviado: {comando}')
def on_key_press(key):
    try:
        key_char = key.char
        if key_char in comandos:
            comando = comandos[key_char]
            enviar_comando(comando)
    except AttributeError:
        pass
def on_key_release(key):
    if key == keyboard.Key.esc:
        listener.stop()

with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
