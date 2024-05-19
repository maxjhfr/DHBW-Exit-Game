package de.maxjhfr;

import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;

import de.maxjhfr.commands.TestCommand;
import de.maxjhfr.listener.BlockPlaceListener;
import de.maxjhfr.listener.JoinListener;


public class Main extends JavaPlugin {

    private ForceResourcePack forceResourcePack;

    @Override
    public void onEnable() {
        Bukkit.getLogger().info("Exit Game plugin started");
        super.onEnable();

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

    public ForceResourcePack getForceResourcePack() {
        return this.forceResourcePack;
    }



}
