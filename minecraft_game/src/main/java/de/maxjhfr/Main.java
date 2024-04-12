package de.maxjhfr;

import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;

import de.maxjhfr.commands.TestCommand;
import de.maxjhfr.listener.BlockPlaceListener;
import de.maxjhfr.webSocket.WebSocketClient;


public class Main extends JavaPlugin {

    private WebSocketClient websocketClient;

    @Override
    public void onEnable() {
        Bukkit.getLogger().info("Exit Game plugin started");
        super.onEnable();

        // activate websocket
        this.websocketClient = new WebSocketClient();

        // register listeners
        final BlockPlaceListener blockPlaceListener = new BlockPlaceListener();
        

        // register commands
        this.getCommand("test").setExecutor(new TestCommand(this));



        getServer().getPluginManager().registerEvents(blockPlaceListener, this);

    }

    @Override
    public void onDisable() {
        Bukkit.getLogger().info("Exit Game plugin stopped");
        super.onDisable();
    }


    public WebSocketClient getWebSocketClient() {
        return this.websocketClient;
    }



}
