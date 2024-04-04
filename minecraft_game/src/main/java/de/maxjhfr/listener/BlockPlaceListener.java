package de.maxjhfr.listener;

import net.md_5.bungee.api.ChatColor;

import org.bukkit.Material;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.block.BlockPlaceEvent;

public class BlockPlaceListener implements Listener {


    @EventHandler
    public void onBlockPlace(BlockPlaceEvent e) {
        Player p = e.getPlayer();
        if (e.getBlock().getType() == Material.END_ROD && e.getBlock().getLocation().getY() >= 100) {
            e.setCancelled(false);
            p.sendMessage(ChatColor.GREEN + "Gut gemacht! Du hast jetzt wieder Empfang und du sendest auf Leitung "
                        + ChatColor.BLUE + '7');
        } else {
            e.setCancelled(true);
            p.sendMessage(ChatColor.RED + "Die Antenne ist nicht hoch genug");
        }
    }



}
