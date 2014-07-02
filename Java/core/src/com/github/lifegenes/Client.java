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
				GameState gameState = this.recieve();
			} catch (IOException e) {e.printStackTrace();}
		}
	}

	public GameState recieve() throws IOException {
		// TODO: return data in a thread-safe way
		if (socket.isConnected()) {
			if (buffIn.ready()) {
				String data = buffIn.readLine();
				return parseInbound(data);
			}
		}
		return null;
	}
	
	public void send(Action action) throws IOException {
		if (socket.isConnected()) {
			byte[] data = this.parseOutbound(action);
			outStream.write(data);
			outStream.flush(); // Flush is needed to send data immediately
		}
	}
	
	
	private GameState parseInbound(String data) {
		// TODO: Implement
		
		return null;
	}
	
	private byte[] parseOutbound(Action action) {
		// TODO: Convert from python to Java
		
		/*
		 * # Parse actions
		payload = ''
		if isinstance(action, ClientAction):
			ID = action.getID()
			payload = payload + str(ID)
			raise Warning("Sending abstract action to client")
	
		if isinstance(action, ClientAction.Message):
			payload = payload + delim + action.getMsg()
		elif isinstance(action, ClientAction.NewCell):
			payload = payload + delim + action.getCell().compress()
		elif isinstance(action, ClientAction.RemoveCell):
			payload = payload + delim + action.getCellID()
		elif isinstance(action, ClientAction.MoveCell):
			payload = payload + delim + action.getCellID() + delim + action.getX() + delim + action.getY()
		elif isinstance(action, ClientAction.ChangeCellColor):
			payload = payload + delim + action.getCellID() + delim + action.getColor()
		else:
			raise Exception("Outbound parsing failed: unknown action passed to method")
	
		return payload
		 */
		
		
		
		return null;
	}

}
