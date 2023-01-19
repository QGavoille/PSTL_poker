import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

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

        deck = new CardGame(new RandomGenerator());
        deck.badShuffle();
        table = new Card[5];
    }
    public void deal(){
        table = deck.multiPop(5);
        joueurs[3].setJeux(deck.multiPop(2));
        joueurs[2].setJeux(deck.multiPop(2));
        joueurs[1].setJeux(deck.multiPop(2));
        joueurs[0].setJeux(deck.multiPop(2));
        examine(2);
        examine(1);
        joueurs[0].cache();

    }
    public void nvGame(){
        deck = new CardGame(deck.getRandom());
        deck.badShuffle();
        deal();
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

    public void writeVisible(boolean append) throws IOException {
        FileWriter fr = new FileWriter("cards.projet",append);
        BufferedWriter writer = new BufferedWriter(fr);
        writer.write("mes cartes:"+joueurs[3].getJeux()[0].toString()+";"+joueurs[3].getJeux()[1].toString());
        writer.newLine();
        writer.write("table:");
        for (Card c:table
             ) {
            writer.write(c.toString()+";");
        }
        writer.newLine();
        writer.write("j2:"+joueurs[2].getJeux()[0].toString()+";"+joueurs[2].getJeux()[1].toString());
        writer.newLine();
        writer.write("j3:"+joueurs[1].getJeux()[0].toString()+";"+joueurs[1].getJeux()[1].toString());
        writer.newLine();
        writer.write("<>");
        writer.newLine();


        writer.close();

    }

}
