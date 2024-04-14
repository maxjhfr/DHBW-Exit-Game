package de.maxjhfr.commands;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

import de.maxjhfr.Main;
import de.maxjhfr.webSocket.MyWebSocketClient;

public class TestCommand implements CommandExecutor {

    private MyWebSocketClient webSocketClient;

    public TestCommand(Main plugin) {
        this.webSocketClient = plugin.getWebSocketClient();
    }

    @Override
    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
        if (!(sender instanceof Player)) {
            return false;
        }
        this.webSocketClient.connect();

        while(!this.webSocketClient.isOpen()) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        this.webSocketClient.send("HI");

        this.webSocketClient.close();
        

        return true;
    }

}
