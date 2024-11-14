#defino función 
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect("Cooperadora Alumnos", "")
        while not sta_if.isconnected():
            print(".",end="")
    print("Network config:", sta_if.ifconfig())
do_connect()

from microdot import Microdot
app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')
@app.route("/<dir>/<file>")
async def styles(request,dir,file):
        return send_file("/"+dir+"/"+file)

app.run(port=80)
