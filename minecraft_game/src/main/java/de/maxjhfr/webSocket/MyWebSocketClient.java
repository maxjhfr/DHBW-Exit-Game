package de.maxjhfr.webSocket;

import java.net.URI;

import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import org.json.JSONObject;

public class MyWebSocketClient extends WebSocketClient {

  /**
   * @param serverUri
   * URI is "ws://localhost:5000"
   */
  public MyWebSocketClient(URI serverUri) {
    super(serverUri);
  }

  @Override
    public void onOpen(ServerHandshake handshakedata) {
      System.out.println("Connected to server");

      sendMessage("minecraft_connected", null);
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
   * @param type
   * @param value
   * 
   * Sends a JSON String to the Flask server 
   */
  public void sendMessage(String type, Object value) {

    // check if connection is established
    Boolean isConnected = false;
    if (isOpen()) isConnected = true;


    // create JSON to send to server
    JSONObject jsonObject = new JSONObject();
    jsonObject.put("type", type);
    jsonObject.put("connected", isConnected);
    jsonObject.put("value", value);

    // send message
    if (isOpen()) {
        send(jsonObject.toString());
        System.out.println("Message sent");
    } else {
        System.out.println("WebSocket connection is not open. Cannot send message.");
    }
}


}
