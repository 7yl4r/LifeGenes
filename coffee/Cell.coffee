DNA = require './DNA'

class Cell
    constructor: (row, col, parents) ->
        @state = 0
        @row = row
        @col = col
        @proteins = {}
        @proteins[Cell.PROTEIN_CODE.alwaysOn] =  {
            name: Cell.PROTEIN_CODE.alwaysOn,
            amount: 1
        }
        @proteins[Cell.PROTEIN_CODE.newCell] = {
            name: Cell.PROTEIN_CODE.newCell,
            amount: 1
        }

        @DNA = new DNA(parents)
        @setWatchedValues()

    # === static properties: ===
    # protein id strings
    @PROTEIN_CODE: {
                    alwaysOn:'awysOn',
                    newCell:'newCel'
                }

    # methods of computing the "run" function
    @COMPUTE: {
                    GoL: 0,
                    proteins: 1
                }
    # === === === === === === ===

    setWatchedValues: () ->
        # updates watched values p1, p2, p3, p4 with protein values
        # TODO: all values here should be editable via the GUI
        oneHundredPercent = 4  # what amount of protein = 100% opacity
        @p1 = @proteins['newCel'].amount/oneHundredPercent
        @p2 = @proteins['awysOn'].amount/oneHundredPercent
        @p3 = .5
        @p4 = .7

    setState: (newState) ->
        @state = newState

    getState: () ->
        return @state

    run: (dish, computeType) ->
        switch computeType
            when Cell.COMPUTE.GoL
                return @runGoL(dish)
            when Cell.COMPUTE.proteins
                return @runProteins(dish)
            else
                throw Error('computeType not recognized')

    runProteins: (dish) ->
        # responds to proteins which are present, and produces new proteins
        for inProtein of @proteins
            outputProteins = @DNA.getProteinResponse(@proteins[inProtein])
            for outProtein in outputProteins
                if not @DNA.connectionSilencedBy(@proteins[inProtein], outProtein, @proteins)
                    console.log(@proteins[inProtein], ' yields ', outProtein)
                    if outProtein not in @proteins
                        @proteins.push(outProtein)
                    else
                        @proteins[outProtein.name].amount += outProtein.amount
                # else connection is silenced, move along
        setWatchedValues()
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