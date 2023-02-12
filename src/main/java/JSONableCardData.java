public class JSONableCardData {
    Couleur couleur;
    int valeur;

    public JSONableCardData(Card c) {
        this.couleur = c.getCouleur();
        this.valeur = c.getValue();
    }
}
