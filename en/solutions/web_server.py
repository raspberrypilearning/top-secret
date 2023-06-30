import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine


ssid = 'SSID here'
password = 'psk_here'


def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
    

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection


def webpage(temperature, state) -> str:
    title = "Raspberry Pi Pico W"
    state_style = "far fa-lightbulb" if state == "ON" else "fas fa-lightbulb"
        
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>{title}</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
            </head>
            <body>
                <div class="container">
                    <div class="px-4 py-5 my-5 text-center">
                        <img class="d-block mx-auto mb-4" src="https://cdn.cdnlogo.com/logos/r/98/raspberry-pi.svg" alt="Raspberry Pi Logo" width="100">
                        <h1 class="display-5 fw-bold">{title}</h1>
                        <div class="col-lg-6 mx-auto">
                          <p class="lead mb-4">Temperature is {temperature}</p>
                          <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
                            <form action="./lighton">
                                <input class="btn btn-success btn-lg px-4 gap-3" type="submit" value="Light on" />
                            </form>
                            <form action="./lightoff">
                                <input class="btn btn-danger btn-lg px-4 gap-3" type="submit" value="Light off" />
                            </form>
                          </div>
                        </div>
                        <p>&nbsp;</p>
                        <p><i class="{state_style} fa-5x"></i></p>
                      </div>                    
                </div>
                <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
                <script defer src="https://use.fontawesome.com/releases/v5.15.4/js/all.js" integrity="sha384-rOA1PnstxnOBLzCLMcre8ybwbTmemjzdNlILg8O7z1lUkLXozs4DHonlDtnE7fpc" crossorigin="anonymous"></script>
            </body>
            </html>
            """
    return str(html)

def serve(connection):
    #Start a webserver
    state = 'OFF'
    pico_led.off()
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            #led.on()
            pico_led.on()
            state = 'ON'
        elif request =='/lightoff?':
            pico_led.off()
            #led.off()
            state = 'OFF'
        temperature = pico_temp_sensor.temp
        html = webpage(temperature, state)
        client.send(html)
        client.close()


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
