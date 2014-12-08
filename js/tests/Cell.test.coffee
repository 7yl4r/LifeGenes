Dish = require '../coffee/Dish'
Cell = require '../coffee/Cell'

exports.basicCellTest =

    'test run without exception': (test) ->
        dish = new Dish(3,3)

        cell = new Cell(1,1) # new cell @ position 1,1
        # cell = dish.getCell(1,1)  # select middle cell
        cell.run(dish)  # allows the cell to react to & produce proteins
        cell.step(dish)  # run environment rules on the cell to determine state change (e.g. live<->dead)

        test.done()