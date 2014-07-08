import ClientAction


def handleActions(universe, *actions):
    """
    Pass actions to this function to commit them into the universe
    :param universe: The game manager that is calling this function
    :param actions: array of actions to be committed to memory
    :return: None
    """

    for action in actions:
        print "getting action"
        if isinstance(action, ClientAction.Message):
            # TODO: Do something useful with this message
            print "Printing message"
            print action.getMsg()

        elif isinstance(action, ClientAction.NewCell):
            universe.addCell(action.getCell())

        elif isinstance(action, ClientAction.RemoveCell):
            result = universe.removeCell(action.getCellID())
            if result is False:
                raise Exception("Could not remove cell %s: Cell does not exist" % action.getCellID())

        elif isinstance(action, ClientAction.MoveCell):
            # TODO: Is this a useful action?
            print "Moving cell %s by X:" % action.getCellID() + action.getX() + " Y:" + action.getY()

        elif isinstance(action, ClientAction.ChangeCellColor):
            result = universe.setCellColor(action.getCellID(), action.getColor())
            if result is False:
                raise Exception("Could not change color to %s on cell %s: Cell does not exist"
                                % action.getCellID(),
                                action.getColor())

        else:
            raise Exception("Inbound parsing failed: Unknown action ID '%s' acquired" % action.getID)