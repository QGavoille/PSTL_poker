
public class Player {
    private int id;
    private String nom;
    private Card[] jeux;

    public Player(int id, String name, Card[] jeux){
        this.id = id;
        this.nom = name;
        this.jeux = jeux;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public void cache(){
        this.jeux[0].setVisible(false);
        this.jeux[1].setVisible(false);
    }
    public void montre(){
        this.jeux[0].setVisible(true);
        this.jeux[1].setVisible(true);
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public Card[] getJeux() {
        return jeux;
    }

    public void setJeux(Card[] jeux) {
        this.jeux = jeux;
    }
}
