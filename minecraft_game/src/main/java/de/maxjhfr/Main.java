package de.maxjhfr;

import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;

import de.maxjhfr.listener.BlockPlaceListener;


public class Main extends JavaPlugin {

    @Override
    public void onEnable() {
        Bukkit.getLogger().info("Exit Game plugin started");
        super.onEnable();

        final BlockPlaceListener blockPlaceListener = new BlockPlaceListener();
        




        getServer().getPluginManager().registerEvents(blockPlaceListener, this);

    }

    @Override
    public void onDisable() {
        Bukkit.getLogger().info("Exit Game plugin stopped");
        super.onDisable();
    }



}
