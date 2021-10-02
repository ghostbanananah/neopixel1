radio.onReceivedNumber(function (receivedNumber) {
    program = receivedNumber
    change = 1
    basic.showNumber(program)
})
input.onButtonPressed(Button.A, function () {
    if (program < 9) {
        program += 1
    }
    basic.showNumber(program)
    change = 1
    radio.sendNumber(program)
})
input.onButtonPressed(Button.B, function () {
    if (program >= 1) {
        program += -1
    }
    basic.showNumber(program)
    change = 1
    radio.sendNumber(program)
})
let red_pos = 0
let blue_pos = 0
let change = 0
let program = 0
let strip = neopixel.create(DigitalPin.P0, 12, NeoPixelMode.RGB)
program = 0
change = 1
basic.showNumber(program)
radio.setGroup(42)
basic.forever(function () {
    if (program == 0) {
        for (let index = 0; index < 11; index++) {
            strip.shift(1)
            strip.show()
            basic.pause(200)
        }
        for (let index = 0; index < 11; index++) {
            strip.shift(-1)
            strip.show()
            basic.pause(200)
        }
    } else if (program == 7 || program == 6) {
    	
    } else {
        strip.rotate(-1)
        strip.show()
        basic.pause(200)
    }
    if (change == 1) {
        change = 0
        if (program == 0) {
            strip.clear()
            strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
        } else if (program == 1) {
            strip.clear()
            strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Violet))
            strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Orange))
            strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Blue))
            strip.setPixelColor(3, neopixel.colors(NeoPixelColors.Violet))
            strip.setPixelColor(4, neopixel.colors(NeoPixelColors.Orange))
            strip.setPixelColor(5, neopixel.colors(NeoPixelColors.Blue))
            strip.setPixelColor(6, neopixel.colors(NeoPixelColors.Violet))
            strip.setPixelColor(7, neopixel.colors(NeoPixelColors.Orange))
            strip.setPixelColor(8, neopixel.colors(NeoPixelColors.Blue))
            strip.setPixelColor(9, neopixel.colors(NeoPixelColors.Violet))
            strip.setPixelColor(10, neopixel.colors(NeoPixelColors.Orange))
            strip.setPixelColor(11, neopixel.colors(NeoPixelColors.Blue))
        } else if (program == 2) {
            strip.clear()
            strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Orange))
            strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Green))
            strip.setPixelColor(4, neopixel.colors(NeoPixelColors.Indigo))
        } else if (program == 3) {
            strip.clear()
            strip.showRainbow(1, 360)
        } else if (program == 4) {
            strip.clear()
            strip.showColor(neopixel.colors(NeoPixelColors.White))
        } else if (program == 5) {
            strip.clear()
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
        } else if (program == 6) {
            strip.clear()
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
            basic.pause(500)
            strip.showColor(neopixel.colors(NeoPixelColors.White))
            basic.pause(500)
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
            basic.pause(500)
            strip.showRainbow(1, 360)
            basic.pause(500)
            change = 1
        } else if (program == 7) {
            for (let index = 0; index < 11; index++) {
                strip.clear()
                strip.setPixelColor(blue_pos, neopixel.colors(NeoPixelColors.Blue))
                strip.setPixelColor(red_pos, neopixel.colors(NeoPixelColors.Red))
                blue_pos += -1
                red_pos += 1
                strip.show()
                basic.pause(200)
            }
            blue_pos = 0
            red_pos = 11
            for (let index = 0; index < 11; index++) {
                strip.clear()
                strip.setPixelColor(blue_pos, neopixel.colors(NeoPixelColors.Blue))
                strip.setPixelColor(red_pos, neopixel.colors(NeoPixelColors.Red))
                blue_pos += 1
                red_pos += -1
                strip.show()
                basic.pause(200)
            }
            change = 1
        } else if (program == 8) {
            strip.clear()
            strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Purple))
            strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Yellow))
            strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Green))
            strip.setPixelColor(3, neopixel.colors(NeoPixelColors.Purple))
            strip.setPixelColor(4, neopixel.colors(NeoPixelColors.Yellow))
            strip.setPixelColor(5, neopixel.colors(NeoPixelColors.Green))
            strip.setPixelColor(6, neopixel.colors(NeoPixelColors.Purple))
            strip.setPixelColor(7, neopixel.colors(NeoPixelColors.Yellow))
            strip.setPixelColor(8, neopixel.colors(NeoPixelColors.Green))
            strip.setPixelColor(9, neopixel.colors(NeoPixelColors.Purple))
            strip.setPixelColor(10, neopixel.colors(NeoPixelColors.Yellow))
            strip.setPixelColor(11, neopixel.colors(NeoPixelColors.Green))
        } else if (program == 9) {
            strip.clear()
            strip.setPixelColor(0, neopixel.colors(NeoPixelColors.White))
            strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
            strip.setPixelColor(2, neopixel.colors(NeoPixelColors.White))
            strip.setPixelColor(3, neopixel.colors(NeoPixelColors.Black))
            strip.setPixelColor(4, neopixel.colors(NeoPixelColors.White))
            strip.setPixelColor(5, neopixel.colors(NeoPixelColors.Black))
            strip.setPixelColor(6, neopixel.colors(NeoPixelColors.White))
            strip.setPixelColor(7, neopixel.colors(NeoPixelColors.Black))
            strip.setPixelColor(8, neopixel.colors(NeoPixelColors.White))
            strip.setPixelColor(9, neopixel.colors(NeoPixelColors.Black))
            strip.setPixelColor(10, neopixel.colors(NeoPixelColors.White))
            strip.setPixelColor(11, neopixel.colors(NeoPixelColors.Black))
        } else {
        	
        }
    }
})
