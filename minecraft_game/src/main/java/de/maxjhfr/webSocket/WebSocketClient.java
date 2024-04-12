package de.maxjhfr.webSocket;

import java.net.URI;

import javax.websocket.*;

import org.glassfish.tyrus.client.ClientManager;

public class WebSocketClient {

    private Session session;

    public WebSocketClient() {
        try {
            ClientManager client = ClientManager.createClient();
            URI uri = new URI("ws://localhost:8765");
            client.connectToServer(new Endpoint() {

                @Override
                public void onOpen(Session session, EndpointConfig config) {
                    System.out.println("Connected to server");
                    WebSocketClient.this.session = session;
                    session.addMessageHandler(String.class, message -> {
                        System.out.println("Received message from server: " + message);
                    });
                }      
            }, uri);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void sendMessage(String message) {
        if (session != null && session.isOpen()) {
            session.getAsyncRemote().sendText(message);
            System.out.println("Sent message to server: " + message);
        } else {
            System.out.println("Session is not open or null. Message not sent.");
        }
    }



}
