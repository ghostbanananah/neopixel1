def on_received_number(receivedNumber):
    global program, change
    program = receivedNumber
    change = 1
    basic.show_number(program)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global program, change
    if program < 11:
        program += 1
    basic.show_number(program)
    change = 1
    radio.send_number(program)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global program, change
    if program >= 1:
        program += -1
    basic.show_number(program)
    change = 1
    radio.send_number(program)
input.on_button_pressed(Button.B, on_button_pressed_b)

red_pos = 0
blue_pos = 0
change = 0
program = 0
strip = neopixel.create(DigitalPin.P0, 12, NeoPixelMode.RGB)
program = 10
change = 1
basic.show_number(program)
radio.set_group(42)
my_orange = neopixel.rgb(255, 70, 0)

def on_forever():
    global change, blue_pos, red_pos
    if program == 0:
        for index in range(11):
            strip.shift(1)
            strip.show()
            basic.pause(200)
        for index2 in range(11):
            strip.shift(-1)
            strip.show()
            basic.pause(200)
    elif program == 7 or program == 6:
        pass
    else:
        strip.rotate(-1)
        strip.show()
        basic.pause(200)
    if change == 1:
        change = 0
        if program == 0:
            strip.clear()
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
        elif program == 1:
            strip.clear()
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.VIOLET))
            strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.ORANGE))
            strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.BLUE))
            strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.VIOLET))
            strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.ORANGE))
            strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.BLUE))
            strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.VIOLET))
            strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.ORANGE))
            strip.set_pixel_color(8, neopixel.colors(NeoPixelColors.BLUE))
            strip.set_pixel_color(9, neopixel.colors(NeoPixelColors.VIOLET))
            strip.set_pixel_color(10, neopixel.colors(NeoPixelColors.ORANGE))
            strip.set_pixel_color(11, neopixel.colors(NeoPixelColors.BLUE))
        elif program == 2:
            strip.clear()
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.ORANGE))
            strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.GREEN))
            strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.INDIGO))
        elif program == 3:
            strip.clear()
            strip.show_rainbow(1, 360)
        elif program == 4:
            strip.clear()
            strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        elif program == 5:
            strip.clear()
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        elif program == 6:
            strip.clear()
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
            basic.pause(500)
            strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
            basic.pause(500)
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
            basic.pause(500)
            strip.show_rainbow(1, 360)
            basic.pause(500)
            change = 1
        elif program == 7:
            for index3 in range(11):
                strip.clear()
                strip.set_pixel_color(blue_pos, neopixel.colors(NeoPixelColors.BLUE))
                strip.set_pixel_color(red_pos, neopixel.colors(NeoPixelColors.RED))
                blue_pos += -1
                red_pos += 1
                strip.show()
                basic.pause(200)
            blue_pos = 0
            red_pos = 11
            for index4 in range(11):
                strip.clear()
                strip.set_pixel_color(blue_pos, neopixel.colors(NeoPixelColors.BLUE))
                strip.set_pixel_color(red_pos, neopixel.colors(NeoPixelColors.RED))
                blue_pos += 1
                red_pos += -1
                strip.show()
                basic.pause(200)
            change = 1
        elif program == 8:
            strip.clear()
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.PURPLE))
            strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.YELLOW))
            strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.GREEN))
            strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.PURPLE))
            strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.YELLOW))
            strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.GREEN))
            strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.PURPLE))
            strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.YELLOW))
            strip.set_pixel_color(8, neopixel.colors(NeoPixelColors.GREEN))
            strip.set_pixel_color(9, neopixel.colors(NeoPixelColors.PURPLE))
            strip.set_pixel_color(10, neopixel.colors(NeoPixelColors.YELLOW))
            strip.set_pixel_color(11, neopixel.colors(NeoPixelColors.GREEN))
        elif program == 9:
            strip.clear()
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.WHITE))
            strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLACK))
            strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.WHITE))
            strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.BLACK))
            strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.WHITE))
            strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.BLACK))
            strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.WHITE))
            strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.BLACK))
            strip.set_pixel_color(8, neopixel.colors(NeoPixelColors.WHITE))
            strip.set_pixel_color(9, neopixel.colors(NeoPixelColors.BLACK))
            strip.set_pixel_color(10, neopixel.colors(NeoPixelColors.WHITE))
            strip.set_pixel_color(11, neopixel.colors(NeoPixelColors.BLACK))
        elif program == 10:
            strip.clear()
            strip.set_pixel_color(0, my_orange)
            strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.INDIGO))
            strip.set_pixel_color(2, my_orange)
            strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.INDIGO))
            strip.set_pixel_color(4, my_orange)
            strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.INDIGO))
            strip.set_pixel_color(6, my_orange)
            strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.INDIGO))
            strip.set_pixel_color(8, my_orange)
            strip.set_pixel_color(9, neopixel.colors(NeoPixelColors.INDIGO))
            strip.set_pixel_color(10, my_orange)
            strip.set_pixel_color(11, neopixel.colors(NeoPixelColors.INDIGO))
        elif program == 11:
            strip.clear()
            strip.set_pixel_color(0, my_orange)
            strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.INDIGO))
            strip.set_pixel_color(2, my_orange)
            strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.INDIGO))
            strip.set_pixel_color(4, my_orange)
            strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.INDIGO))
            strip.set_pixel_color(6, my_orange)
            strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.INDIGO))
            strip.set_pixel_color(8, my_orange)
            strip.set_pixel_color(9, neopixel.colors(NeoPixelColors.INDIGO))
            strip.set_pixel_color(10, my_orange)
            strip.set_pixel_color(11, neopixel.colors(NeoPixelColors.INDIGO))
        else:
            pass
basic.forever(on_forever)
