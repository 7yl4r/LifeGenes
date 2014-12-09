Cell = require './Cell'

class BoolArray
    # 2d array of booleans useful for storing cell states temporarily
    constructor: (rows, cols)->
        return ((0 for [1..cols]) for [1..rows])

class Dish
    # a digital petri dish full of cells
    # assumes space is toroidal

    constructor: (rows, cols, displayDiv='', computeType=Cell.COMPUTE.GoL)->
        @generation = 0
        @rowCount = rows
        @colCount = cols
        @cellCount = rows*cols
        @renderDivSelector = displayDiv
        @computeType = computeType

        @cells = []
        for row in [0..(@rowCount-1)]
            cellRow = []
            for col in [0..(@colCount-1)]
                cellRow.push(new Cell(row,col))
            @cells.push(cellRow)

        @_cell_states = new BoolArray(@rowCount, @colCount)  # convenience listing of states

        if document?
            $(document).on("set-environment-type", (evt, selection) ->
                switch selection
                    when "Game_of_Life"
                        $(document).on('click', '.cell', ( evt ) ->
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

        run = () =>
            if @running
                @step()
                setTimeout(run, @TIMER_DELAY)
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
        new_states = new BoolArray(@rowCount, @colCount)
        for rowN of @cells
            for colN of @cells[rowN]
                new_states[rowN][colN] = @getCell(rowN,colN).run(@, @computeType)  # TODO: isn't this REALLY inefficient?

        @_cell_states = new_states
        for rowN of @cells
            for colN of @cells[rowN]
                @setCellState(rowN, colN, new_states[rowN][colN])

        @generation += 1
        @render()
        return @generation

    getCellState: (row, col) ->
        # returns the state of the cell
        return @getCell(row, col).getState()

    getCell: (row, col) ->
        # returns cell object value for given cell row & column, works for negative & out-of-range values
        maxRow = @rowCount
        maxCol = @colCount

        # deal with huge indicies
        row %= maxRow
        col %= maxCol

        # loop boundaries for smaller spillover
        if col < 0 then col = maxCol+col
        if row < 0 then row = maxRow+row

        if col > maxCol then col -= maxCol
        if row > maxRow then row -= maxRow

        # use corrected indicies
        return @cells[row][col]

    getNeighborCount: (R, C) ->
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
                    neighbors += @getCellState(R+i, C+j)
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
            @setCellState(cellEl.getAttribute('data-cell-row'), cellEl.getAttribute('data-cell-col'), 0)
        else
            cellEl.setAttribute('data-state', 1)
            @setCellState(cellEl.getAttribute('data-cell-row'), cellEl.getAttribute('data-cell-col'), 1)
        return

    setCellState: (row, col, newState) ->
        #
        @getCell(row, col).setState(newState)

    render: (renderDivSelector=@renderDivSelector) ->
        # renders the dish if renderDiv is set
        if renderDivSelector?
            dust.render('cellDish',
                {
                    cell_states: main_dish._cell_states
                },
                (err, out) ->
                    # update the html
                    $(renderDivSelector).html(out)
                    if err
                        console.log(err)
            );
        else
            console.log('dish unrendered: no render div set')

module.exports = Dish