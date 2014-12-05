// global constants
NUMBER_OF_ROWS = 15;
NUMBER_OF_COLS = 40;
NUMBER_OF_CELLS = NUMBER_OF_ROWS*NUMBER_OF_COLS;

// settings objects
ENVIRONMENT_TYPE = Object.freeze({enum:["Game_of_Life", "Colorful_Life", "Moving_Life"]});

// global variables
main_dish = new Dish(NUMBER_OF_ROWS, NUMBER_OF_COLS, '#cell-display-div');