package de.maxjhfr;

import org.bukkit.entity.Player;

public class ForceResourcePack {

  private String ulr = "https://www.dropbox.com/scl/fi/g4bypq0r2g87i1xu0h13y/exitGame.zip?rlkey=zg2jkcooxqz6elrkjucv9r8it&st=junviajn&dl=0";

  ForceResourcePack() {
    System.out.println("Resource pack force enabled!");
  }

  public void forcePlayer(Player p) {
    p.setResourcePack(this.ulr);
  }

}
