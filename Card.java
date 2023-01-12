public class Card {
    private int value;
    private Couleur couleur;
    public Card(int v , Couleur c){
        value = v;
        couleur= c;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public Couleur getCouleur() {
        return couleur;
    }

    public void setCouleur(Couleur couleur) {
        this.couleur = couleur;
    }
}
