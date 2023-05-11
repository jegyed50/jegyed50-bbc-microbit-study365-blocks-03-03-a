//  JEGYED50-BBC-MICROBIT-STUDY365-BLOCKS-03-03-A
//  Fish Animation with 5 frame
basic.forever(function on_forever() {
    basic.showLeds(`
        . . # . .
                . # # . #
                # # # # #
                . # # . #
                . . # . .
    `)
    basic.pause(100)
    basic.showLeds(`
        . # . . .
                # # . # .
                # # # # .
                # # . # .
                . # . . .
    `)
    basic.pause(100)
    basic.showLeds(`
        # . . . .
                # . # . .
                # # # . .
                # . # . .
                # . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                . # . . .
                # # . . .
                . # . . .
                . . . . .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
                # . . . .
                # . . . .
                # . . . .
                . . . . .
    `)
    basic.pause(100)
    basic.clearScreen()
    basic.pause(500)
})
