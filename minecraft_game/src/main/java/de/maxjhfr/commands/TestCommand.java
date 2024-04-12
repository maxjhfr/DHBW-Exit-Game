package de.maxjhfr.commands;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

import de.maxjhfr.Main;
import de.maxjhfr.webSocket.WebSocketClient;

public class TestCommand implements CommandExecutor {

    private WebSocketClient webSocketClient;

    public TestCommand(Main plugin) {
        this.webSocketClient = plugin.getWebSocketClient();
    }

    @Override
    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
        if (!(sender instanceof Player)) {
            return false;
        }

        webSocketClient.sendMessage("HI");

        

        




        


        return true;
    }

}
