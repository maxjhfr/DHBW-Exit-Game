package de.maxjhfr;

import java.net.URI;
import java.net.URISyntaxException;

import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;

import de.maxjhfr.commands.TestCommand;
import de.maxjhfr.listener.BlockPlaceListener;
import de.maxjhfr.webSocket.MyWebSocketClient;


public class Main extends JavaPlugin {

    private MyWebSocketClient websocketClient;

    @Override
    public void onEnable() {
        Bukkit.getLogger().info("Exit Game plugin started");
        super.onEnable();

        // activate websocket
        try {
            this.websocketClient = new MyWebSocketClient(new URI("ws://127.0.0.1:5000"));
            this.websocketClient.connect();
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }

        // register listeners
        final BlockPlaceListener blockPlaceListener = new BlockPlaceListener(this);
        

        // register commands
        this.getCommand("test").setExecutor(new TestCommand(this));



        getServer().getPluginManager().registerEvents(blockPlaceListener, this);

    }

    @Override
    public void onDisable() {
        Bukkit.getLogger().info("Exit Game plugin stopped");
        super.onDisable();
    }


    public MyWebSocketClient getWebSocketClient() {
        return this.websocketClient;
    }



}
