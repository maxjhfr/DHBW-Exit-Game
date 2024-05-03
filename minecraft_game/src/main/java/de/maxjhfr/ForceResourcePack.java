package de.maxjhfr;

import org.bukkit.entity.Player;

public class ForceResourcePack {

  private String ulr = "https://google.com";

  ForceResourcePack() {
    System.out.println("Resource pack force enabled!");
  }

  public void forcePlayer(Player p) {
    p.setResourcePack(this.ulr);
  }

}
