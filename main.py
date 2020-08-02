item = 0

def on_pin_pressed_p0():
    radio.set_group(1)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_received_number(receivedNumber):
    global item
    item = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    radio.set_group(3)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        """)
    radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    radio.set_group(2)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_forever():
    if 0 == 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            """)
basic.forever(on_forever)
