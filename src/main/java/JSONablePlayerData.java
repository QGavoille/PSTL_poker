public class JSONablePlayerData {
    String name;
    JSONableCardData[] cards;

    public JSONablePlayerData(Player p) {
        this.name = p.getNom();
        if(p.getJeux()[0].isVisible() && p.getJeux()[1].isVisible()) {
            this.cards = new JSONableCardData[2];
            this.cards[0] = new JSONableCardData(p.getJeux()[0]);
            this.cards[1] = new JSONableCardData(p.getJeux()[1]);
        } else {
            this.cards = new JSONableCardData[2];
            this.cards[0] = null;
            this.cards[1] = null;
        }
    }
}
