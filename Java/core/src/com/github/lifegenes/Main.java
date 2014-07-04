package com.github.lifegenes;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer.ShapeType;
import com.badlogic.gdx.math.Vector2;

import java.util.ArrayList;

public class Main extends ApplicationAdapter {

    private ShapeRenderer renderer;
    private OrthographicCamera camera;
    private ArrayList<Cell> cells;

    @Override
    public void create() {
        String host = "127.0.0.1";
        int port = 7070;

        Client client = null;
        Thread cThread = null;

        client = new Client(host, port);
        cThread = new Thread(client);
        cThread.start();

        renderer = new ShapeRenderer();
        cells = new ArrayList<Cell>();

        // TODO: Import gamestate from sockets somehow


        // new camera for view projections (20 cells wide, 20 cells tall)
        float vWidth = 1f;
        float vHeight = 1f;
        camera = new OrthographicCamera(vWidth, vHeight);

        // This is required for proper display
        camera.setToOrtho(false);
        camera.position.set(vWidth / 2 + 3, vHeight / 2, 0);
        camera.zoom = 0.02f;
        camera.update();
        renderer.setProjectionMatrix(camera.combined);


        // Creating a few cells for testing
        Vector2 pos = new Vector2(vWidth / 2, vHeight / 2);
        for (int i = 0; i < 4; i++) {
            cells.add(new Cell(pos.cpy(), Color.BLUE, ""));
            pos.x += 2;
        }

        pos.x = vWidth / 2 - 1;
        for (int i = 0; i < 4; i++) {
            cells.add(new Cell(pos.cpy(), Color.NAVY, ""));
            pos.x += 2;
        }
    }

    @Override
    public void render() {
        Gdx.gl.glClearColor(0, 0, 0, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);


        // TODO: Get input

        // Start draw
        renderer.begin(ShapeType.Filled);
        // Draw all cells
        for (Cell cell : cells) {
            cell.draw(renderer);
        }
        renderer.end();


        // TODO: Get info from the python > java text file
    }
}
