
public class Card {
    private int value;
    private Couleur couleur;
    private boolean visible = true;


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
