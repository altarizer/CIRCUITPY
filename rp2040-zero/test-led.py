import machine
pin = machine.Pin(29, machine.Pin.OUT)

#pin.value(0)
pin.value(1)
#pin.value(True)
pin.value(False)
pin.high()
#pin.low()