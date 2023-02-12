public class JSONableGameData {
    JSONablePlayerData[] playerCards;
    JSONableCardData[] tableCards;

    public JSONableGameData(Partie p) {
        Player[] players = p.getJoueurs();
        this.playerCards = new JSONablePlayerData[players.length];
        for (int i = players.length-1; i >= 0; i--) {  // Les joueurs sont dans l'ordre inverse (j1 = nous)
            this.playerCards[3-i] = new JSONablePlayerData(players[i]);
        }
        this.tableCards = new JSONableCardData[p.getTable().length];
        for (int i = 0; i < p.getTable().length; i++) {
            this.tableCards[i] = new JSONableCardData(p.getTable()[i]);
        }
    }
}

