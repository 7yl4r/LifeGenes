package com.github.lifegenes.desktop;

import com.badlogic.gdx.backends.lwjgl.LwjglApplication;
import com.badlogic.gdx.backends.lwjgl.LwjglApplicationConfiguration;
import com.github.lifegenes.Main;

public class DesktopLauncher {
	public static void main (String[] arg) {
		LwjglApplicationConfiguration config = new LwjglApplicationConfiguration();
		
		config.title = "LifeGenes";
		
		// Adjust desktop resolution here
		config.fullscreen = false;
		config.width = 800;
		config.height = 600;
		
		new LwjglApplication(new Main(), config);
	}
}
