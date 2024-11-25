# Configuracion inicial
<<<<<<< HEAD

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Conectando a la red...')
        sta_if.active(True)
        sta_if.connect('Cooperadora Alumnos', '')
        while not sta_if.isconnected():
            print(".", end = "")
    print('network config:', sta_if.ifconfig())
    
do_connect()
=======
>>>>>>> 6e7db1a9c52ff9f28ebdc30f475bf3cfe2a6c7b9
