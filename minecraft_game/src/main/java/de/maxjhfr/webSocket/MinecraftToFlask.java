package de.maxjhfr.webSocket;

import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class MinecraftToFlask {

    public void sendPostRequest(String type, String value) {
        try {
            URL url = new URL("http://127.0.0.1:5000/hub");

            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setDoOutput(true);

            String jsonInputString = "{\"type\": \"minecraft\", \"value\": \"done\"}";

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            int resposeCode = connection.getResponseCode();
            System.out.println("Response Code: " + resposeCode);
            connection.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }



}
