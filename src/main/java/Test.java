import java.io.IOException;
import java.util.Scanner;

public class Test {
    public static  void print(Object i){
        System.out.println(i);
    }
   /* public static void main(String[] args) throws IOException {

        src.main.java.RandomGenerator r = new src.main.java.RandomGenerator();
      System.out.println( r.toInt(new int[]{1, 1,1}));
      src.main.java.CardGame c = new src.main.java.CardGame();


      c.goodShuffle();
      print(c);
      print(c.checkInvariant());
      src.main.java.Partie p = new src.main.java.Partie();
      p.deal();
      System.out.println(p);
      p.writeVisible();
    }*/
    public static void main(String[] args) throws IOException {
        System.out.println("je suis modifié");
        CardGame c = new CardGame(new RandomGenerator());
        System.out.println(c);
       Partie p = new Partie();
       p.deal();
       System.out.println(p);

       p.writeVisible(false);
       System.out.println(c.getRandom().toInt(new int[]{1, 0, 1, 1, 0, 0}));
       while(true){
           Scanner sc = new Scanner(System.in);
           System.out.println("continue/examine/exit");
           String saisie = sc.nextLine();
           if(saisie.equals("continue")){
               p.nvGame();
               System.out.println(p);
               p.writeVisible(true);
           }
           if(saisie.equals("examine")){

           }
           if(saisie.equals("exit")){
               break;
           }


       }
    }

}

