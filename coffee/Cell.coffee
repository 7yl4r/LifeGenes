
class Cell
    constructor: (parent1, parent2)->
        @state = 0
        if parent1? and parent2?
            return true
        else
            return false

    setState: (newState) ->
        @state = newState

    getState: () ->
        return @state

try
    window.Cell = Cell
catch error
    module.exports = Cell