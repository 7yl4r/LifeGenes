DNA = require './DNA'

class Cell
    constructor: (row, col, parent1, parent2) ->
        @state = 0
        @row = row
        @col = col
        @proteins = [Cell.PROTEINS.alwaysOn, Cell.PROTEINS.newCell]
        @DNA = new DNA(parent1, parent2)

    # === static properties: ===
    # protein id strings
    @PROTEINS: {
                    alwaysOn:'awysOn',
                    newCell:'newCel'
                }

    # methods of computing the "run" function
    @COMPUTE: {
                    GoL: 0,
                    proteins: 1
                }
    # === === === === === === ===

    setState: (newState) ->
        @state = newState

    getState: () ->
        return @state

    run: (dish, computeType=Cell.COMPUTE.GoL) ->
        switch computeType
            when Cell.COMPUTE.GoL
                return @runGoL(dish)
            when Cell.COMPUTE.proteins
                return @runProteins(dish)
            else
                throw Error('computeType not recognized')

    runProteins: (dish) ->
        # responds to proteins which are present, and produces new proteins
        for inProtein in @proteins
            outputProteins = @DNA.getProteinResponse(inProtein)
            for outProtein in outputProteins
                if not @DNA.connectionSilencedBy(inProtein, outProtein, @proteins)
                    console.log(inProtein, ' yields ', outProtein)
                    if outProtein not in @proteins
                        @proteins.push(outProtein)
                    else
                        console.log('protein already here')
                # else connection is silenced, move along
        return true

    runGoL: (dish) ->
        neighbors = dish.getNeighborCount(@row, @col)
        #console.log(neighbors)
        if neighbors < 2  # underpopulation
            #console.log('under')
            return 0
        else if neighbors > 3  # overpopulation
            #console.log('over')
            return 0
        else if neighbors == 3
            #console.log('reproduce')
            return 1  # reproduction
        # else 2 or 3 neighbors, no change
        else
            #console.log('stay')
            return dish.getCellState(@row, @col)

    step: (dish) ->
        # steps through one interation of the cell, computing state change on the cell
        # and returning the new cell state
        # TODO
        return 0

module.exports = Cell