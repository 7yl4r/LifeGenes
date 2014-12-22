DNA = require './DNA'

class Cell
    constructor: (row, col, parents) ->
        # TODO: add protein behaviors for each iteration: reset, decay, and usage
        #   reset: proteins reset each iteration
        #   decay: proteins decay 1 each iteration
        #   usage: proteins are removed as they are used (NOTE: one protein "unit" can be used to produce multiple others within the same iteration)
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
                    newCell:'newCel',
                    cellDeath: 'deathh',
                    cellEther: 'etherr'
                }
    # === === === === === === ===

    setWatchedValues: () ->
        # updates watched values p1, p2, p3, p4 with protein values
        # TODO: all values here should be editable via the GUI
        oneHundredPercent = 4  # what amount of protein = 100% opacity
        if @proteins[Cell.PROTEIN_CODE.alwaysOn]?
            @p1 = @proteins[Cell.PROTEIN_CODE.alwaysOn].amount  / oneHundredPercent
        else
            @p1 = 0

        if @proteins[Cell.PROTEIN_CODE.newCell]?
            @p2 = @proteins[Cell.PROTEIN_CODE.newCell].amount   / oneHundredPercent
        else
            @p2 = 0

        if @proteins[Cell.PROTEIN_CODE.cellDeath]?
            @p3 = @proteins[Cell.PROTEIN_CODE.cellDeath].amount / oneHundredPercent
        else
            @p3 = 0

        if @proteins[Cell.PROTEIN_CODE.cellEther]?
            @p4 = @proteins[Cell.PROTEIN_CODE.cellEther].amount / oneHundredPercent
        else
            @p4 = 0
        return

    setState: (newState) ->
        @state = newState

    getState: () ->
        return @state

    respond: () ->
        # perform hard-coded responses to proteins
        @setWatchedValues()
        @makeAlive() if @birthCondition()
        @die() if @deathCondition()

    birth: (parents) ->
        # cell is suddenly alive. inherits from parents if given
        throw Error('notImpErr')

    birthCondition: () ->
        # returns true if spontaneous birth condition met
        return false

    deathCondition: () ->
        #returns true if death condition is met
        return false

    getProteinOutputs: () ->
        # returns a list {{name:'p1', amount:2},...} of protiens output by this cell
        theOutputs = {}
        theOutputs[Cell.PROTEIN_CODE.alwaysOn] = {
            name: Cell.PROTEIN_CODE.alwaysOn,
            amount: 1
        }
        if @state > 0  # if cell is alive
            # responds to proteins which are present, and produces new proteins
            for inProtein of @proteins
                outputProteins = @DNA.getProteinResponse(@proteins[inProtein])
                for outProtein in outputProteins
                    if not @DNA.connectionSilencedBy(@proteins[inProtein], outProtein, @proteins)
                        #console.log(@proteins[inProtein], ' yields ', outProtein)
                        if outProtein not in theOutput
                            theOutputs[outProtein.name] = outProtein
                        else
                            theOutputs[outProtein.name].amount += outProtein.amount
                    # else connection is silenced, move along
        # else state is 0
        return theOutputs

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