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

    run: (dish, computeType) ->
        switch computeType
            when Cell.COMPUTE.GoL
                return @runGoL(dish)
            when Cell.COMPUTE.proteins
                # 1. compute protein outputs for each cell
                return @runProteins(dish)
                # 2. diffuse proteins to neighboring cells, perform hard-coded responses (death/birth)


                # 3. reset proteins
                # ITERATION 1
                # 0 1 1 1 0     before (live/dead 1/0)
                # step 1: compute protein outs
                # 0 2 2 2 0     p outputs (cellEther amount before diffusing)
                # step 2: diffuse
                # 1 2 3 2 1     diffuse (cellEther concentration after diffusing)
                # step 3: perform hard-coded protein responses
                # 0 0 1 0 0     new state (kill/birth criterion applied: 2 < cellEther < 4 to stay alive)
                # step 4: reset proteins

            else
                throw Error('computeType not recognized')

    runProteins: (dish) ->
        if @state > 0
            # responds to proteins which are present, and produces new proteins
            for inProtein of @proteins
                outputProteins = @DNA.getProteinResponse(@proteins[inProtein])
                for outProtein in outputProteins
                    if not @DNA.connectionSilencedBy(@proteins[inProtein], outProtein, @proteins)
                        #console.log(@proteins[inProtein], ' yields ', outProtein)
                        if outProtein not in @proteins
                            @proteins[outProtein.name] = outProtein
                        else
                            @proteins[outProtein.name].amount += outProtein.amount
                    # else connection is silenced, move along
            @setWatchedValues()
            if Cell.PROTEIN_CODE.cellDeath in @proteins
                return 0
            else
                return 1
        # else state is 0

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