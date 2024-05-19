package de.maxjhfr.commands;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;

import de.maxjhfr.Main;
import de.maxjhfr.webSocket.MinecraftToFlask;
import de.maxjhfr.webSocket.MyWebSocketClient;

public class TestCommand implements CommandExecutor {

    private MyWebSocketClient webSocketClient;

    public TestCommand(Main plugin) {
    }

    @Override
    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
        new MinecraftToFlask().sendPostRequest("minecraft", "done");
        

        return true;
    }

}
