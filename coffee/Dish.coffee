class Dish
    # a digital petri dish full of cells
    # assumes space is toroidal

    constructor: (rows, cols, displayDiv='')->
        @generation = 0
        @rowCount = rows
        @colCount = cols
        @cellCount = rows*cols
        @cell_states = ((0 for [1..@colCount]) for [1..@rowCount])
        @renderDivSelector = displayDiv

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

        # constants:
        @TIMER_DELAY = 10  # ms delay between updates while running
        @NEIGHBORHOOD_SIZE = 1  # size of cell neighborhood (i.e. how far the cell can "see") 1 = 8 neighbors [[aa,ab,ac][ba,ME,bc],[ca,cb,cc]]

    start: () ->
        # starts running iterations of update() until stopped
        @running = true

        run = () ->
            if @running
                @step()
                setTimeout(@step, @TIMER_DELAY)
                return true
            else
                return false

        run()

    stop: () ->
        # stops running iterations of update() which have been start()ed
        @running = false

    step: () ->
        # steps through one interation on the dish, computing for every cell and updating the state and generation

        console.log('generation ', @generation, '->', @generation+1)
        new_states = @cell_states.slice(0)
        for rowN of @cell_states
            for colN of @cell_states[rowN]
                new_states[rowN][colN] = @runCell(rowN, colN, @cell_states)  # TODO: isn't this REALLY inefficient?
                #console.log(@cell_states[rowN][colN], '->', new_states[rowN][colN])


        @cell_states = new_states

        @generation += 1
        @render()
        return @generation

    runCell: (row, col, cellStates) ->
        # computes for cell @ (row,col) in given cellStates array and returns the resulting array
        newCells = cellStates.slice(0)
        neighbors = @getNeighborCount(row, col, cellStates)
        if neighbors < 2  # underpopulation
            return 0
        else if neighbors > 3  # overpopulation
            return 0
        else if neighbors == 3
            return 1  # reproduction
        # else 2 or 3 neighbors, no change
        else return cellStates[row][col]

    getCell: (row, col, cells=@cell_states) ->
        # returns cell value for given cell row & column, works for negative & out-of-range values
        maxRow = @rowCount-1
        maxCol = @colCount-1

        # deal with huge indicies
        row %= maxRow
        col %= maxCol

        # loop boundaries for smaller spillover
        if col < 0 then col = maxCol+col
        if row < 0 then row = maxRow+row

        if col > maxCol then col -= maxCol
        if row > maxRow then row -= maxRow

        # use corrected indicies
        return cells[row][col]

    getNeighborCount: (R, C, S) ->
        # returns number of live neighbors for given cell @ (r,c) in state array s
        R = parseInt(R)
        C = parseInt(C)
        neighbors = 0
        i = -@NEIGHBORHOOD_SIZE
        while i <= @NEIGHBORHOOD_SIZE
            j = -@NEIGHBORHOOD_SIZE
            while j <= @NEIGHBORHOOD_SIZE
                if i == 0 and j == 0
                    # don't count yourself
                    j += 1
                else
                    neighbors += @getCell(R+i, C+j, S)
                    j += 1
            i += 1
        return neighbors

    cellClick: (cellEl) ->
        # what to do when a cell is clicked
        @toggleCell(cellEl)
        return

    toggleCell: (cellEl) ->
        # turns a cell on/off
        if cellEl.getAttribute('data-state') == '1'
            cellEl.setAttribute('data-state', 0)
            @cell_states[cellEl.getAttribute('data-cell-row')][cellEl.getAttribute('data-cell-col')] = 0
        else
            cellEl.setAttribute('data-state', 1)
            @cell_states[cellEl.getAttribute('data-cell-row')][cellEl.getAttribute('data-cell-col')] = 1
        return

    render: (renderDivSelector=@renderDivSelector) ->
        #renders the dish if renderDiv is set
        if renderDivSelector?
            dust.render('cellDish',
                {
                    cell_states: main_dish.cell_states
                },
                (err, out) ->
                    # update the html
                    $(renderDivSelector).html(out)
                    if err
                        console.log(err)
            );
        else
            console.log('dish unrendered: no render div set')

try
    window.Dish = Dish
catch error
    module.exports = Dish