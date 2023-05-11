# JEGYED50-BBC-MICROBIT-STUDY365-BLOCKS-03-03-A
# Fish Animation with 5 frame
def on_forever():
    basic.show_leds("""
        . . # . .
                . # # . #
                # # # # #
                . # # . #
                . . # . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . # . . .
                # # . # .
                # # # # .
                # # . # .
                . # . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        # . . . .
                # . # . .
                # # # . .
                # . # . .
                # . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . # . . .
                # # . . .
                . # . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                # . . . .
                # . . . .
                # . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.clear_screen()
    basic.pause(500)
basic.forever(on_forever)
