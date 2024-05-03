package de.maxjhfr;

import java.net.URI;
import java.net.URISyntaxException;

import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;

import de.maxjhfr.commands.TestCommand;
import de.maxjhfr.listener.BlockPlaceListener;
import de.maxjhfr.listener.JoinListener;
import de.maxjhfr.webSocket.MyWebSocketClient;


public class Main extends JavaPlugin {

    private MyWebSocketClient websocketClient;
    private ForceResourcePack forceResourcePack;

    @Override
    public void onEnable() {
        Bukkit.getLogger().info("Exit Game plugin started");
        super.onEnable();

        // activate websocket
        try {
            this.websocketClient = new MyWebSocketClient(new URI("ws://192.168.178.84:5000"));
            this.websocketClient.connect();
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }

        // register commands
        this.getCommand("test").setExecutor(new TestCommand(this));

        // register listeners
        final BlockPlaceListener blockPlaceListener = new BlockPlaceListener(this);
        final JoinListener joinListener = new JoinListener(this);
        getServer().getPluginManager().registerEvents(blockPlaceListener, this);
        getServer().getPluginManager().registerEvents(joinListener, this);

        //register force resource pack
        this.forceResourcePack = new ForceResourcePack();
    
        
    }

    @Override
    public void onDisable() {
        Bukkit.getLogger().info("Exit Game plugin stopped");
        super.onDisable();
    }


    public MyWebSocketClient getWebSocketClient() {
        return this.websocketClient;
    }

    public ForceResourcePack getForceResourcePack() {
        return this.forceResourcePack;
    }



}
