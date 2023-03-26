
public class Card {
    private int value;
    private Couleur couleur;
    private boolean visible = true;


    public Card(int v , Couleur c){
        value = v;
        couleur= c;


    }
    public int toInt(){
        if(couleur == Couleur.PIQUE) {
            return value;
        } else if (couleur == Couleur.TREFLE) {
            return value+12;

        } else if (couleur == Couleur.COEUR) {
            return value+25;

        }else {
            return value+38;
        }
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
    public String toString(){
        if(!this.visible){
            return "cachee";
        }
        return (this.value) + " de "+ this.couleur.toString();
    }

    public boolean isVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }


}
