let valeur = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    images.iconImage(IconNames.Happy).showImage(0)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    images.iconImage(IconNames.Ghost).showImage(0)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    images.iconImage(IconNames.Sad).showImage(0)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    valeur = randint(1, 6)
    if (valeur == 1) {
        basic.showLeds(`
            . . # . .
                        . # # . .
                        . . # . .
                        . . # . .
                        . # # # .
        `)
    } else if (valeur == 2) {
        basic.showLeds(`
            # # # # .
                        . . . # .
                        # # # # .
                        # . . . .
                        # # # # .
        `)
    } else if (valeur == 3) {
        basic.showLeds(`
            . . # # #
                        . . . . #
                        . . . # #
                        . . . . #
                        . . # # #
        `)
    } else if (valeur == 4) {
        basic.showLeds(`
            . # . . #
                        . # . . #
                        . # # # #
                        . . . . #
                        . . . . #
        `)
    } else if (valeur == 5) {
        basic.showLeds(`
            # # # # .
                        # . . . .
                        # # # # .
                        . . . # .
                        # # # # .
        `)
    } else {
        basic.showLeds(`
            # # # . .
                        # . . . .
                        # # # # .
                        # . . # .
                        # # # # .
        `)
    }
    
})
