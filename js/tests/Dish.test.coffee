Dish = require '../coffee/Dish'

exports.basicCellTest =

    'test run without exception': (test) ->
        dish = new Dish(3,3)
        cell = dish.getCell(1,1)  # select middle cell

        test.done()