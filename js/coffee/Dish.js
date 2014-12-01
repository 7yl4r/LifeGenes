// Generated by CoffeeScript 1.4.0
(function() {
  var Dish;

  Dish = (function() {

    function Dish(rows, cols) {
      this.generation = 0;
      this.cell_states = (function() {
        var _i, _results;
        _results = [];
        for (_i = 1; 1 <= NUMBER_OF_ROWS ? _i <= NUMBER_OF_ROWS : _i >= NUMBER_OF_ROWS; 1 <= NUMBER_OF_ROWS ? _i++ : _i--) {
          _results.push((function() {
            var _j, _results1;
            _results1 = [];
            for (_j = 1; 1 <= NUMBER_OF_COLS ? _j <= NUMBER_OF_COLS : _j >= NUMBER_OF_COLS; 1 <= NUMBER_OF_COLS ? _j++ : _j--) {
              _results1.push(0);
            }
            return _results1;
          })());
        }
        return _results;
      })();
      console.log('number of cells =', this.cell_states.length, this.cell_states);
    }

    Dish.prototype.step = function() {
      console.log('generation ', this.generation, '->', this.generation + 1);
      this.generation += 1;
    };

    Dish.prototype.cellClick = function(evt) {
      console.log(evt);
    };

    return Dish;

  })();

  try {
    window.Dish = Dish;
  } catch (error) {
    module.exports = Dish;
  }

}).call(this);
