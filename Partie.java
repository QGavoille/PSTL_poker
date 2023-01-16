public class Partie {

    private Player[] joueurs;
    private CardGame deck;
    public Card[] table;
    public Partie(){
        joueurs = new Player[4];
        joueurs[0] = new Player(0,"Rigobert",new Card[2]);

        joueurs[1] = new Player(1,"Beckam",new Card[2]);

        joueurs[2] = new Player(2,"Zoubir",new Card[2]);

        joueurs[3] = new Player(3,"Godefroy",new Card[2]);

        deck = new CardGame();
        deck.badShuffle();
        table = new Card[5];
    }
    public void deal(){
        for(Player p: joueurs){
            p.setJeux(deck.multiPop(2));
            if(p.getId()!=3){
                p.cache();
            }
        }
        table = deck.multiPop(5);

    }

    public String toString(){
        String s = "_______________________________________\n";
        for(Player p: joueurs){
            s+= p.getNom()+"\n";
            s+= p.getJeux()[0].toString()+"\n";
            s+= p.getJeux()[1].toString()+"\n";
            s+= "________________________\n";

        }
        s+="TABLE\n";
        for (Card c:
            table ) {
            s+= c.toString();
            s+= "\n";

        }
        s+="----------------------------------------\n";
        s+=deck.toString();
        return s;

    }
    public void examine(int id){
        joueurs[id].montre();
    }
}
