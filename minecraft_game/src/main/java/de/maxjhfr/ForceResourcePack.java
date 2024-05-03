package de.maxjhfr;

import org.bukkit.entity.Player;

public class ForceResourcePack {

  private String ulr = "https://www.dropbox.com/scl/fi/kg4f0oe20vzmxrr6nqjvl/exitGame.zip?rlkey=uu2oq8uy4zo0i7fe6chhcr7pr&st=30zp7jym&dl=1";

  ForceResourcePack() {
    System.out.println("Resource pack force enabled!");
  }

  public void forcePlayer(Player p) {
    p.setResourcePack(this.ulr);
  }

}
