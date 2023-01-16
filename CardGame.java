import java.util.ArrayList;
import java.util.List;

public class CardGame {
    private Card[] deck;
    int current = 51;

    public CardGame(){
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

    }
    public String toString(){
        String toret = "";

        for(Card c: deck){
            try {toret+= c.getValue()+" de "+ c.getCouleur().toString()+"\n";}
            catch(Exception e){
                toret+= "*\n";
            }
        }

        return toret;

    }

    public void badShuffle(){
        Card tmp ;
        RandomGenerator r = new RandomGenerator();
        for(int i = 0; i< 52;i++){
            int nextPos = r.nextInt(6)%51;

            tmp = deck[nextPos];
            deck[nextPos] = deck[i];
            deck[i] = tmp;
        }


    }

    public Card pop(){
        Card ret = deck[current];
        deck[current] = null;
        current --;

        return ret;
    }
    public Card[] multiPop(int hm){
        Card[] ret = new Card[hm];
        for(int i = 0; i<hm; i++){
            ret[i] = pop();
        }
        return ret;
    }

   public void goodShuffle(){
        Card tmp;
        RandomGenerator r = new RandomGenerator();
        for(int i = 0; i<52;i++){
            int nextPos = r.nextInt(6);
            while (nextPos>=52){
                nextPos = r.nextInt(6);
            }
            tmp = deck[nextPos];
            deck[nextPos] = deck[i];
            deck[i] = tmp;
        }
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


}
