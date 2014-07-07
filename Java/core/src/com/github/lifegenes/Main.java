package com.github.lifegenes;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.assets.AssetManager;
import com.badlogic.gdx.assets.loaders.resolvers.InternalFileHandleResolver;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer.ShapeType;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.scenes.scene2d.ui.Skin;
import com.badlogic.gdx.scenes.scene2d.ui.TextField;
import com.badlogic.gdx.scenes.scene2d.utils.Drawable;

import java.util.ArrayList;
import java.util.concurrent.ConcurrentLinkedDeque;
import java.util.concurrent.ConcurrentLinkedQueue;

public class Main extends ApplicationAdapter {

    private ShapeRenderer renderer;
    private OrthographicCamera camera;
    private ArrayList<Cell> cells;
    private TextField messageField;
    private Stage stage;
    private SpriteBatch batch;
    private ConcurrentLinkedQueue<Message> messageQueue;

    @Override
    public void create() {
        String host = "127.0.0.1";
        int port = 7070;

        Client client = null;
        Thread cThread = null;

        messageQueue = new ConcurrentLinkedQueue<Message>();

        client = new Client(host, port, messageQueue);
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
        stage = new Stage();
        camera.setToOrtho(false);
        camera.position.set(vWidth / 2 + 3, vHeight / 2, 0);
        camera.zoom = 0.02f;
        camera.update();
        renderer.setProjectionMatrix(camera.combined);

        // Create a text field for testing messages sent to the server
        Gdx.input.setInputProcessor(stage);
        batch = new SpriteBatch();
        AssetManager manager = new AssetManager();
        manager.load("html/war/Assets/uiskin.json", Skin.class);
        manager.finishLoading();
        Skin skin = manager.get("html/war/Assets/uiskin.json", Skin.class);
        messageField = new TextField("", skin);
        messageField.setWidth(Gdx.graphics.getWidth());
        messageField.setPosition(0,0);
        messageField.setTextFieldListener(new TextField.TextFieldListener() {
            public void keyTyped (TextField textField, char key) {
                if (key == '\r') {
                    messageQueue.add(new Message(messageField.getText()));
                    messageField.setText("");
                }
            }
        });
        stage.addActor(messageField);
        stage.setKeyboardFocus(messageField);

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

        // textfield drawing
        stage.draw();
    }
}
