package de.maxjhfr.webSocket;

import java.net.URI;

import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import org.json.JSONObject;

public class MyWebSocketClient extends WebSocketClient {

  /**
   * @param serverUri
   */
  public MyWebSocketClient(URI serverUri) {
    super(serverUri);
  }

  public void connectToFlask() {
    try {
      System.out.println("trying to connect");
      connectBlocking();
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
    if (isOpen()) {
      System.out.println("connected");
    } else {
      System.out.println("connection didn't work");
    }
  }

  @Override
    public void onOpen(ServerHandshake handshakedata) {
      System.out.println("Connected to server");
    }

  @Override
  public void onMessage(String message) {
      System.out.println("Received message: " + message);
  }

  @Override
  public void onClose(int code, String reason, boolean remote) {
      System.out.println("Connection closed");
  }

  @Override
  public void onError(Exception ex) {
      ex.printStackTrace();
  }

  /**
   * @param type name of the game
   * @param value status
   *
   * Sends a JSON String to the Flask server 
   */
  public void sendMessage(String type, Object value) {

    // create JSON to send to server
    JSONObject jsonObject = new JSONObject();
    jsonObject.put("type", type);
    jsonObject.put("value", value);

    // send message
    if (isOpen()) {
        send(jsonObject.toString());
        System.out.println("Message sent: " + jsonObject.toString());
    } else {
        System.out.println("WebSocket connection is not open. Cannot send message.");
    }
  }
}
