DNA = require("./coffee/DNA.js")
Cell = require("./coffee/Cell.js")
Dish = require("./coffee/Dish.js")
GUI = require("./coffee/GUI.js")

// global constants
window.NUMBER_OF_ROWS = 15;
window.NUMBER_OF_COLS = 40;
window.NUMBER_OF_CELLS = NUMBER_OF_ROWS*NUMBER_OF_COLS;

// settings objects
window.ENVIRONMENT_TYPE = Object.freeze({enum:["Game_of_Life", "Protein_Life"]});

// global variables:
window.main_dish = new Dish(NUMBER_OF_ROWS, NUMBER_OF_COLS, '#cell-display-div');
window.gui = new GUI(main_dish);

$(document).ready(function(){
    // connect jquery event listeners to (mutable) GUI methods
    $(document).on('click', '.cell', function(evt) {
        return gui.cellClick(this);  // TODO: UI.cellClick
    });

    // TODO: rework this, multiple environment types (and UIs) not needed, perhaps should be "preset" or "demo" selector
    //$(document).on("set-environment-type", function(evt, selection){
    //    GUI.setEnvironmentType(selection)
    //});
});