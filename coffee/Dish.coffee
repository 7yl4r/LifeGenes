class Dish
    # a digital petri dish full of cells
    # assumes space is toroidal

    constructor: (rows, cols)->
        @generation = 0
        @rowCount = rows
        @colCount = cols
        @cellCount = rows*cols
        @cell_states = ((0 for [1..@colCount]) for [1..@rowCount])

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