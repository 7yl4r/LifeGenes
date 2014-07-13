package com.github.lifegenes;

import java.io.BufferedReader;
import java.io.IOException;
import java.net.ConnectException;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.UUID;
import java.util.concurrent.ConcurrentLinkedQueue;

class Client implements Runnable {

    private final ConcurrentLinkedQueue<byte[]> messageQueue;
    private Socket socket;
    private static String ID = UUID.randomUUID().toString();
    private BufferedReader buffIn;
    private final String host;
    private final int port;
    private static final String delim = "^&*";

    public Client(String host, int port, ConcurrentLinkedQueue<byte[]> messageQueue) {
        this.host = host;
        this.port = port;
        this.messageQueue = messageQueue;
    }

    public boolean attemptConnection() {
        boolean connected = false;
        try {
            socket = new Socket(host, port);
            socket.setTcpNoDelay(false);
        } catch (UnknownHostException e1) {
            System.out.println("Unknown host");
        } catch (ConnectException e1) {
            System.out.println("Connection refused");
        } catch (IOException e1) {
            System.out.println("I/O Exception");
        }
        finally {
            if (socket.isConnected()) {
                connected = true;
            }
        }
        return connected;
    }

    @Override
    public void run() {

        boolean connected = false;
        while (!connected) {
            connected = attemptConnection();

            if (!connected) System.out.println("Connection refused. Trying again in two seconds...");
            else {break;}

            long wait = 2000000000;
            try {
                this.wait(wait);
            } catch (InterruptedException e1) {
                e1.printStackTrace();
            }
        }
        // TODO: Implement a safe shutdown procedure initiated by user
        while (true) {
            try {
                GameState gameState = this.receive();
            } catch (IOException e) {
                e.printStackTrace();
            }

            // Send messages, if any
            if (!messageQueue.isEmpty()) {

                try {
                    while (!messageQueue.isEmpty()) {
                        // TODO: Include userID when implemented

                        socket.getOutputStream();
                        socket.getOutputStream().write(messageQueue.poll());
                    }
                    System.out.println("Socket flushing");
                    socket.getOutputStream().flush();

                } catch (IOException e) {e.printStackTrace();}
            }
        }
    }

    GameState receive() throws IOException {
        // TODO: return data in a thread-safe way
        if (socket.isConnected() && buffIn != null) {
            if (buffIn.ready()) {
                String data = buffIn.readLine();
                return parseInbound(data);
            }
        }
        return null;
    }

    public void send(Action action) throws IOException, NativeException {
        if (socket.isConnected()) {
            byte[] data = parseOutbound(action);
            socket.getOutputStream().write(data);
            socket.getOutputStream().flush(); // Flush is needed to send data immediately
        }
    }


    public GameState parseInbound(String data) {
        // TODO: Implement

        return null;
    }

    public static byte[] parseOutbound(Action action) throws NativeException {
        // Parse Actions
        int ID = action.getID();
        String payload = "" + ID;

        if (action.getID() == -1) {
            throw new NativeException("Trying to send abstract action to client");
        } else if (action instanceof Message) {
            Message act = (Message) action;
            payload = payload + delim + act.getMessage();
            System.out.println(payload);
        } else if (action instanceof NewCell) {
            NewCell act = (NewCell) action;
            // TODO: Create compress method in Cell class synonymous to Python's Cell compress
            //payload = payload + delim + act.getCell().compress();
        } else if (action instanceof RemoveCell) {
            RemoveCell act = (RemoveCell) action;
            payload = payload + delim + act.getCellID();
        } else if (action instanceof MoveCell) {
            MoveCell act = (MoveCell) action;
            payload = payload + delim + act.getCellID() + delim + act.getPos().x + delim + act.getPos().y;
        } else if (action instanceof ChangeCellColor) {
            ChangeCellColor act = (ChangeCellColor) action;
            payload = payload + delim + act.getCellID() + delim + act.getColor();
        } else {
            throw new NativeException("Outbound parsing failed: unknown action passed to method");
        }

        payload += "\n";

        return payload.getBytes();
    }
}
