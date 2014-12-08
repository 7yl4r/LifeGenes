DNA = require("./coffee/DNA.js")
Cell = require("./coffee/Cell.js")
Dish = require("./coffee/Dish.js")

// global constants
window.NUMBER_OF_ROWS = 15;
window.NUMBER_OF_COLS = 40;
window.NUMBER_OF_CELLS = NUMBER_OF_ROWS*NUMBER_OF_COLS;

// settings objects
window.ENVIRONMENT_TYPE = Object.freeze({enum:["Game_of_Life", "Colorful_Life", "Moving_Life"]});

// global variables:
window.main_dish = new Dish(NUMBER_OF_ROWS, NUMBER_OF_COLS, '#cell-display-div');