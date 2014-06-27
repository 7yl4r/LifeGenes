package com.github.lifegenes;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.math.Vector2;

public class Cell {
	
	private Vector2 pos;
	private Color color;
	
	/** Create a new Cell **/
	public Cell(Vector2 pos, Color color) {
		this.pos = pos;
		this.color = color;
	}
	
	/** Draws the cell. Ensure the ShapeRenderer has begun before using **/
	public void draw(ShapeRenderer renderer) {
		renderer.setColor(color);
		renderer.box(pos.x, pos.y, 0, 1, 1, 0);
	}
	
	public Vector2 getPos() {
		return pos;
	}

}
