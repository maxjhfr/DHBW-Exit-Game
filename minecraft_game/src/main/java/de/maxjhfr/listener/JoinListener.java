package de.maxjhfr.listener;

import java.util.ArrayList;

import org.bukkit.Material;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.entity.ItemMergeEvent;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.inventory.EquipmentSlot;
import org.bukkit.inventory.ItemFlag;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ArmorMeta;
import org.bukkit.inventory.meta.ItemMeta;

import de.maxjhfr.Main;
import net.md_5.bungee.api.chat.hover.content.Item;

public class JoinListener implements Listener {

    private Main plugin;

    public JoinListener(Main plugin) {
        this.plugin = plugin;
    }

    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent e) {
        Player p = e.getPlayer();
        //plugin.getForceResourcePack().forcePlayer(p);

        p.getInventory().clear();

        ItemStack stack = new ItemStack(Material.ARMOR_STAND);
        ItemMeta meta = stack.getItemMeta();
        meta.setDisplayName("Funkturm");
        ArrayList<String> list = new ArrayList<>();
        list.add("5G kompatibel");
        meta.setLore(list);
        meta.addItemFlags(ItemFlag.HIDE_ATTRIBUTES);
        stack.setItemMeta(meta);
        
        p.getInventory().setItem(0, stack);

        ItemStack glass = new ItemStack(Material.GLASS);
        ItemMeta meta2 = stack.getItemMeta();
        meta2.setDisplayName("Space Helmet");
        meta2.addItemFlags(ItemFlag.HIDE_ATTRIBUTES);
        glass.setItemMeta(meta2);
        p.getInventory().setItem(EquipmentSlot.HEAD, glass);

        ItemStack space1 = new ItemStack(Material.IRON_CHESTPLATE);
        ArmorMeta meta3 = (ArmorMeta) space1.getItemMeta();
        meta3.setDisplayName("Space suit");
        meta3.addItemFlags(ItemFlag.HIDE_ATTRIBUTES);
        space1.setItemMeta(meta3);
        p.getInventory().setItem(EquipmentSlot.CHEST, space1);

        ItemStack space2 = new ItemStack(Material.IRON_LEGGINGS);
        ArmorMeta meta4 = (ArmorMeta) space2.getItemMeta();
        meta4.setDisplayName("Space suit");
        meta4.addItemFlags(ItemFlag.HIDE_ATTRIBUTES);
        space2.setItemMeta(meta4);
        p.getInventory().setItem(EquipmentSlot.LEGS, space2);

        ItemStack space3 = new ItemStack(Material.IRON_BOOTS);
        ArmorMeta meta5 = (ArmorMeta) space3.getItemMeta();
        meta5.setDisplayName("Space suit");
        meta5.addItemFlags(ItemFlag.HIDE_ATTRIBUTES);
        space3.setItemMeta(meta5);
        p.getInventory().setItem(EquipmentSlot.FEET, space3);


    }
}
