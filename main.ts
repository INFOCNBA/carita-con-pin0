let pin0mio = 0
loops.everyInterval(20, function () {
    pin0mio = pins.digitalReadPin(DigitalPin.P0)
    if (pin0mio) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
basic.forever(function () {
	
})
