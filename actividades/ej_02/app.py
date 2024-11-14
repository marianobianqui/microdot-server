# Aplicacion del servidor
from microdot import Microdot, send_file
from machine import Pin

app = Microdot()

led1 = Pin(32, Pin.OUT)
led2 = Pin(33, Pin.OUT)
led3 = Pin(25, Pin.OUT)

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route("/<dir>/<file>")
async def static(request, dir, file):
    return send_file("/"+ dir +"/" + file)

@app.route("/led/toggle/<int:led>")
async def LED(request, led):
    global led1
    if led == 1:
        led1.value(not led1.value())
    if led == 2:
        led2.value(not led2.value())
    if led == 3:
        led3.value(not led3.value())

    return { "status" : "ok" }

    


app.run(port = 80)

@app.route("<dir>/<file>")
async def static