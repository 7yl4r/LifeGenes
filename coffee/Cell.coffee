DNA = require './DNA'

PROTEINS = {
                alwaysOn:'awysOn',
                newCell:'newCel'
            }

class Cell
    constructor: (parent1, parent2) ->
        @state = 0
        @proteins = [PROTEINS.alwaysOn, PROTEINS.newCell]
        @DNA = new DNA(parent1, parent2)

    setState: (newState) ->
        @state = newState

    getState: () ->
        return @state

    run: (dish) ->
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

    step: (dish) ->
        # steps through one interation of the cell, computing state change on the cell
        # and returning the new cell state
        # TODO
        return 0

module.exports = Cell