package com.github.lifegenes;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.UUID;

public class Client implements Runnable {

	private Socket socket;
	private static String ID = UUID.randomUUID().toString();
	private BufferedReader buffIn;
	private OutputStream outStream;
	private String host;
	private int port;
	
	public Client(String host, int port) throws UnknownHostException, IOException {
		
		this.host = host;
		this.port = port;
	}
	
	@Override
	public void run() {
		
		try {
			socket = new Socket(host, port);
			buffIn = new BufferedReader( new InputStreamReader(socket.getInputStream()));
			outStream = socket.getOutputStream();
		} catch (UnknownHostException e1) {e1.printStackTrace();
		} catch (IOException e1) {e1.printStackTrace();}
		
		// TODO: Implement a safe shutdown procedure initiated by user
		while (true) {
			try {
				GameState gameState = this.receive();
			} catch (IOException e) {e.printStackTrace();}
		}
	}

	public GameState receive() throws IOException {
		// TODO: return data in a thread-safe way
		if (socket.isConnected()) {
			if (buffIn.ready()) {
				String data = buffIn.readLine();
				return parseInbound(data);
			}
		}
		return null;
	}
	
	public void send(Action action) throws IOException, NativeException {
		if (socket.isConnected()) {
			byte[] data = this.parseOutbound(action, "~");
			outStream.write(data);
			outStream.flush(); // Flush is needed to send data immediately
		}
	}
	
	
	private GameState parseInbound(String data) {
		// TODO: Implement
		
		return null;
	}
	
	private byte[] parseOutbound(Action action, String delim) throws NativeException {
		// TODO: Convert from python to Java
		// Parse Actions
		String payload = "";

		if (action.getID() == -1) {
			int ID = action.getID();
			payload = payload + ID;
			throw new NativeException("Sending abstract action to client");
	    }
        else if (action instanceof Message) {
            Message act = (Message) action;
			payload = payload + delim + act.getMessage();
        }
        else if (action instanceof NewCell) {
            NewCell act = (NewCell) action;
            // TODO: Create compress method in Cell class synonymous to Python's Cell compress
			//payload = payload + delim + act.getCell().compress();
        }
        else if (action instanceof RemoveCell) {
            RemoveCell act = (RemoveCell) action;
			payload = payload + delim + act.getCellID();
        }
        else if (action instanceof MoveCell) {
            MoveCell act = (MoveCell) action;
			payload = payload + delim + act.getCellID() + delim + act.getPos().x + delim + act.getPos().y;
        }
        else if (action instanceof ChangeCellColor) {
            ChangeCellColor act = (ChangeCellColor) action;
			payload = payload + delim + act.getCellID() + delim + act.getColor();
        }
		else {
            throw new NativeException("Outbound parsing failed: unknown action passed to method");
        }

		return payload.getBytes();
	}
}
