class Dish
    # a digital petri dish full of cells
    # assumes space is toroidal

    constructor: (rows, cols)->
        @generation = 0
        @cell_states = ((0 for [1..NUMBER_OF_COLS]) for [1..NUMBER_OF_ROWS])
        console.log('number of cells =', @cell_states.length, @cell_states)

    step: () ->
        # steps through one interation
        console.log('generation ', @generation, '->', @generation+1)
        @generation += 1
        return

    cellClick: (evt) ->
        # what to do when a cell is clicked
        console.log(evt)
        return
try
    window.Dish = Dish
catch error
    module.exports = Dish