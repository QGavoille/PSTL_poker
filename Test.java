public class Test {
    public static  void print(Object i){
        System.out.println(i);
    }
    public static void main(String[] args){
        RandomGenerator r = new RandomGenerator();
      System.out.println( r.toInt(new int[]{1, 1,1}));
      CardGame c = new CardGame();
      c.goodShuffle();
      print(c);
      print(c.checkInvariant());
      Partie p = new Partie();
      p.deal();
      System.out.println(p);
    }
}