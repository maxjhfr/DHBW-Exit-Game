package de.maxjhfr.webSocket;

import java.net.URI;

import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;

public class MyWebSocketClient extends WebSocketClient {

  /**
   * @param serverUri
   * URI is "ws://localhost:8765"
   */
  public MyWebSocketClient(URI serverUri) {
    super(serverUri);
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

  public void connectAndSend(String message) {
    	this.connect();
      while(!this.isOpen()) {
        try {
          Thread.sleep(10);
        } catch (InterruptedException e) {
          e.printStackTrace();
        }
      }
      this.send(message);
      this.close();

  }


}
