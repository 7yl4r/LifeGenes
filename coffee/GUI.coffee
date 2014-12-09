
class GUI
    constructor: (dish, type=GUI.TYPE.master) ->
        @type = type
        @dish = dish

    # type of interface, allows for different views of the same thing
    # TODO: add beginner, painter interface, statistics, artistic, etc...
    @TYPE: {
        master: "master"
    }


    setInterfaceType: (type) ->
        switch type
            when @type  # don't bother changing into what you're already wearing
                return
            when type in GUI.TYPE
                console.log("switching interface type to ", type)
                # TODO
            else
                throw Error("unkown interface type requested")


    cellClick: (cellEl) ->
        # what to do when a cell is clicked
        @toggleCell(cellEl)
        return

    toggleCell: (cellEl) ->
        # turns a cell on/off
        if cellEl.getAttribute('data-state') == '1'
            cellEl.setAttribute('data-state', 0)
            @dish.setCellState(cellEl.getAttribute('data-cell-row'), cellEl.getAttribute('data-cell-col'), 0)
        else
            cellEl.setAttribute('data-state', 1)
            @dish.setCellState(cellEl.getAttribute('data-cell-row'), cellEl.getAttribute('data-cell-col'), 1)
        return


module.exports = GUI