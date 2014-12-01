class Dish
    # a digital petri dish full of cells
    # assumes space is toroidal

    constructor: (rows, cols)->
        @generation = 0
        @rowCount = rows
        @colCount = cols
        @cellCount = rows*cols
        @cell_states = ((0 for [1..@colCount]) for [1..@rowCount])

        $(document).on("set-environment-type", (evt, selection) ->
            switch selection
                when "Game_of_Life"
                    $('.cell').click( ( evt ) ->
                        main_dish.cellClick(@)
                    )
                else
                    console.log('unknown env type:', selection)
                    throw Error('unknown env type')
        )


    step: () ->
        # steps through one interation
        console.log('generation ', @generation, '->', @generation+1)
        @generation += 1
        return

    cellClick: (cellEl) ->
        # what to do when a cell is clicked
        @toggleCell(cellEl)
        return

    toggleCell: (cellEl) ->
        # turns a cell on/off
        if cellEl.classList.contains('live-cell')
            cellEl.classList.remove('live-cell')
        else
            cellEl.classList.add('live-cell')
        return

try
    window.Dish = Dish
catch error
    module.exports = Dish