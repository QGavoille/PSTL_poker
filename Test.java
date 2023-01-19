import java.io.IOException;
import java.util.Scanner;

public class Test {
    public static  void print(Object i){
        System.out.println(i);
    }
   /* public static void main(String[] args) throws IOException {

        RandomGenerator r = new RandomGenerator();
      System.out.println( r.toInt(new int[]{1, 1,1}));
      CardGame c = new CardGame();


      c.goodShuffle();
      print(c);
      print(c.checkInvariant());
      Partie p = new Partie();
      p.deal();
      System.out.println(p);
      p.writeVisible();
    }*/
    public static void main(String[] args) throws IOException {
        CardGame c = new CardGame(new RandomGenerator());
        System.out.println(c);
       Partie p = new Partie();
       p.deal();
       System.out.println(p);

       p.writeVisible(false);
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

