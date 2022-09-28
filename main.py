pin0mio = 0

def on_every_interval():
    global pin0mio
    pin0mio = pins.digital_read_pin(DigitalPin.P0)
    if pin0mio:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
loops.every_interval(20, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)
