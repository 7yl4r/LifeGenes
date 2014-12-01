// global constants
NUMBER_OF_ROWS = 15;
NUMBER_OF_COLS = 40;
NUMBER_OF_CELLS = NUMBER_OF_ROWS*NUMBER_OF_COLS;

// enumerated global constants
ENVIRONMENT_TYPES = Object.freeze({"Game_of_Life":1, "Colorful_Life":2, "Moving_Life":3})

// global variables
main_dish = new Dish(NUMBER_OF_ROWS, NUMBER_OF_COLS);