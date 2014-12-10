// Generated by CoffeeScript 1.4.0
(function() {
  var GUI,
    __indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  GUI = (function() {

    function GUI(dish, type) {
      if (type == null) {
        type = GUI.TYPE.master;
      }
      this.type = type;
      this.dish = dish;
      this.proteinsShowing = true;
    }

    GUI.TYPE = {
      master: "master"
    };

    GUI.prototype.setInterfaceType = function(type) {
      switch (type) {
        case this.type:
          break;
        case __indexOf.call(GUI.TYPE, type) >= 0:
          return console.log("switching interface type to ", type);
        default:
          throw Error("unkown interface type requested");
      }
    };

    GUI.prototype.cellClick = function(cellEl) {
      this.toggleCell(cellEl);
    };

    GUI.prototype.toggleCell = function(cellEl) {
      if (cellEl.getAttribute('data-state') === '1') {
        cellEl.setAttribute('data-state', 0);
        this.dish.setCellState(cellEl.getAttribute('data-cell-row'), cellEl.getAttribute('data-cell-col'), 0);
      } else {
        cellEl.setAttribute('data-state', 1);
        this.dish.setCellState(cellEl.getAttribute('data-cell-row'), cellEl.getAttribute('data-cell-col'), 1);
      }
    };

    GUI.prototype.proteinDisplayToggle = function() {
      switch (this.proteinsShowing) {
        case true:
          $('.protein').hide();
          return this.proteinsShowing = false;
        case false:
          $('.protein').show();
          return this.proteinsShowing = true;
        default:
          throw Error('@proteinsShowing flag is non-boolean');
      }
    };

    return GUI;

  })();

  module.exports = GUI;

}).call(this);