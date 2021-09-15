valeur = 0

def on_button_pressed_a():
    images.icon_image(IconNames.HAPPY).show_image(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    images.icon_image(IconNames.GHOST).show_image(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    images.icon_image(IconNames.SAD).show_image(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global valeur
    valeur = randint(1, 6)
    if valeur == 1:
        basic.show_leds("""
            . . # . .
                        . # # . .
                        . . # . .
                        . . # . .
                        . # # # .
        """)
    elif valeur == 2:
        basic.show_leds("""
            # # # # .
                        . . . # .
                        # # # # .
                        # . . . .
                        # # # # .
        """)
    elif valeur == 3:
        basic.show_leds("""
            . . # # #
                        . . . . #
                        . . . # #
                        . . . . #
                        . . # # #
        """)
    elif valeur == 4:
        basic.show_leds("""
            . # . . #
                        . # . . #
                        . # # # #
                        . . . . #
                        . . . . #
        """)
    elif valeur == 5:
        basic.show_leds("""
            # # # # .
                        # . . . .
                        # # # # .
                        . . . # .
                        # # # # .
        """)
    else:
        basic.show_leds("""
            # # # . .
                        # . . . .
                        # # # # .
                        # . . # .
                        # # # # .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
