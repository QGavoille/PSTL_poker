
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class CardGame {
    private Card[] deck;
    private int current = 0;
    private RandomGenerator random;

    public CardGame(RandomGenerator rand){
        deck = new Card[52];
        for(int i = 0;i< 13; i++){
            deck[i] = new Card(i+1,Couleur.PIQUE);
        }
        for(int i = 0;i< 13; i++){
            deck[13+i] = new Card(i+1,Couleur.TREFLE);
        }
        for(int i = 0;i< 13; i++){
            deck[26+i] = new Card(i+1,Couleur.COEUR);
        }
        for(int i = 0;i< 13; i++){
            deck[39+i] = new Card(i+1,Couleur.CARREAU);
        }
        random = rand;

    }
    public String toString(){
        String toret = "";
        int i = 0;
        for(Card c: deck){
            toret += i+" : ";
            try {toret+= c.getValue()+" de "+ c.getCouleur().toString()+"\n";}
            catch(Exception e){
                toret+= "*\n";
            }
            i++;
        }

        return toret;

    }


    private double log2(int nb){
        return Math.max(Math.log(nb)/Math.log(2),0);
    }

    public void badShuffle() throws IOException {//TODO faire une stat dessus
        Card tmp;
        FileWriter fr = new FileWriter("trackShuffle.projet");
        BufferedWriter writer = new BufferedWriter(fr);
        writer.write("le melange");
        int translation = 0;
        for(int i = 0; i<52;i++){
            System.out.print(((int)log2(51-i))+1);
            System.out.println("   "+(51-i));
            int nextPos = translation+random.nextInt(((int)log2(51-i))+1)%(52-i);
            writer.write(deck[i].toString()+" <-> "+ deck[nextPos].toString());
            writer.newLine();
            tmp = deck[nextPos];
            deck[nextPos] = deck[i];
            deck[i] = tmp;
            translation++;

        }
        writer.close();
    }

    public void goodShuffle() throws IOException{
        System.out.println(" good Shuffle");
        Card tmp;
        FileWriter fr = new FileWriter("trackShuffle.projet");
        BufferedWriter writer = new BufferedWriter(fr);
        writer.write("le melange");
        int translation = 0;
        for(int i = 0; i<52; i++){
            System.out.print(((int)log2(51-i))+1);
            System.out.println("   "+(51-i));
            int nextPos = translation+random.nextInt(((int)log2(51-i))+1);
            while(nextPos>=52){
                System.out.println("rejet");
                nextPos = translation+random.nextInt(((int)log2(51-i))+1);
            }
            writer.write(deck[i].toString()+" <-> "+ deck[nextPos].toString());
            writer.newLine();
            tmp = deck[nextPos];
            deck[nextPos] = deck[i];
            deck[i] = tmp;
            translation++;
        }
        writer.close();
    }




    public Card pop(){
        Card ret = deck[current];
        deck[current] = null;
        current ++;

        return ret;
    }
    public Card[] multiPop(int hm){
        Card[] ret = new Card[hm];
        for(int i = 0; i<hm; i++){
            ret[i] = pop();
        }
        return ret;
    }




    public boolean checkInvariant(){
        List<Card> dejaVu = new ArrayList<>(54);
        Card[] save = deck;
        for (Card c: deck
             ) {
            if(dejaVu.contains(c)){
                System.out.println(c);
                return false;
            }
            dejaVu.add(c);
        }
        return true;
    }

    public RandomGenerator getRandom(){
        return random;
    }

    public Card[] getDeck() {
        return deck;
    }
}
