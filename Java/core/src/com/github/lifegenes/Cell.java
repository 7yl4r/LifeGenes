package com.github.lifegenes;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.math.Vector2;

public class Cell {

    private Vector2 pos;
    private Color color;
    private String DNA;

    /**
     * Create a new Cell *
     */
    public Cell(Vector2 pos, Color color, String DNA) {
        this.pos = pos;
        this.color = color;
        this.DNA = DNA;
    }

    /**
     * Draws the cell. Ensure the ShapeRenderer has begun before using *
     */
    public void draw(ShapeRenderer renderer) {
        renderer.setColor(color);
        renderer.box(pos.x, pos.y, 0, 1, 1, 0);
    }

    Vector2 getPos() {
        return pos;
    }

    String getDNA() {
        return DNA;
    }

    /**
     * Compresses the cell for network transfer.
     *
     * @param delim The delimiter you wish to separate the values with (typically '&')
     * @return A string-ed cell ready for network transfer
     */
    public String compress(String delim) {
        String s = "";
        Vector2 pos = getPos();
        s = pos.x + delim +
                pos.y + delim +
                getDNA().replaceAll("[[,\\\\]]", "") + delim +
                Color.rgb565(color) + delim;

        return s;
    }

    /**
     * Decompresses a compressed Cell
     *
     * @param compCell The compressed cell
     * @return the decompressed cell
     */
    public static Cell decompress(String compCell) {
        String[] split = compCell.split("~");
        Vector2 pos = new Vector2(Float.parseFloat(split[0]), Float.parseFloat(split[1]));
        String DNA = split[2];
        // TODO: Check and see if the color conversion actually works right
        Color cellColor = Color.WHITE;
        Color.rgb565ToColor(cellColor, Integer.getInteger(split[3]));

        return new Cell(pos, cellColor, DNA);
    }
}
