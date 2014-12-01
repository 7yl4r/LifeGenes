class Dish
    # a digital petri dish full of cells
    # assumes space is toroidal

    constructor: (rows, cols)->
        @cell_states = ((0 for [1..NUMBER_OF_COLS]) for [1..NUMBER_OF_ROWS])
        console.log('number of cells =', @cell_states.length, @cell_states)

try
    window.Dish = Dish
catch error
    module.exports = Dish