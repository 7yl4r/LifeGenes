package com.github.lifegenes;

import com.badlogic.gdx.math.Vector2;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

interface Action {
    /**
     * Creates a new Action, which is used for socket communication for the client
     */

    static Map<String, Integer> ACTION_IDS = Collections.unmodifiableMap(new HashMap<String, Integer>() {
        {
            put("NewCell", 0);
            put("RemoveCell", 1);
            put("MoveCell", 2);
            put("ChangeCellColor", 3);
            put("Message", 10);
        }
    });

    public int getID();
}

interface CellAction extends Action {

    /**
     * Gets Cell ID from parent class, CellAction
     *
     * @return Returns Cell ID in question for manipulation
     */
    public int getCellID();
}

class NewCell implements Action {

    private final Cell cell;
    private final int ID;

    public NewCell(Cell cell) {
        this.ID = ACTION_IDS.get("NewCell");
        this.cell = cell;
    }

    public Cell getCell() {
        return cell;
    }

    @Override
    public int getID() {
        return ID;
    }
}

class RemoveCell implements CellAction {

    private final int cellID;
    private final int ID;

    public RemoveCell(int cellID) {
        this.ID = ACTION_IDS.get("RemoveCell");
        this.cellID = cellID;
    }

    @Override
    public int getID() {
        return ID;
    }

    @Override
    public int getCellID() {
        return cellID;
    }
}

class MoveCell implements CellAction {

    private final int ID;
    private final int cellID;
    private final Vector2 pos;

    public MoveCell(Vector2 pos, int cellID) {
        this.ID = ACTION_IDS.get("MoveCell");
        this.cellID = cellID;
        this.pos = pos;
    }

    public Vector2 getPos() {
        return pos;
    }

    @Override
    public int getID() {
        return ID;
    }

    @Override
    public int getCellID() {
        return cellID;
    }
}

class ChangeCellColor implements CellAction {

    private final int ID;
    private final int cellID;
    private final int color;

    /**
     * @param cellID The ID of the cell in question
     * @param color  The color of the cell expressed in 255-int RGB values
     */
    public ChangeCellColor(int cellID, int color) {
        this.ID = ACTION_IDS.get("ChangeCellColor");
        this.cellID = cellID;
        this.color = color;
    }

    public int getColor() {
        return color;
    }

    @Override
    public int getID() {
        return ID;
    }

    @Override
    public int getCellID() {
        return cellID;
    }
}

class Message implements Action {

    private int ID;
    private String message;

    /**
     * Creates a new Message, which is used to pass text strings to the server or possibly other players
     *
     * @param msg The message you would like to send
     */
    public Message(String msg) {
        this.ID = ACTION_IDS.get("Message");
        this.message = msg;
    }

    public String getMessage() {
        return this.message;
    }

    @Override
    public int getID() {
        return ID;
    }
}
