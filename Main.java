import java.util.TreeMap;

public class Main {
    public static void main(String[] args) {
        RandomGenerator generator = new RandomGenerator();
        diceThrowRepartition(generator, 1000000);
    }

    public static void diceThrowRepartition(RandomGenerator generator, int throwNumber) {
        Dice dice = new Dice(generator);
        TreeMap<Integer, Integer> repartition = new TreeMap<>();
        for (int i = 0; i < throwNumber; i++) {
            int value = dice.rollNonUniform();
            if (repartition.containsKey(value)) {
                repartition.put(value, repartition.get(value) + 1);
            } else {
                repartition.put(value, 1);
            }
        }
        for (int i = 0; i < 6; i++) {
            System.out.println(i + ": " + repartition.get(i));
        }
    }
}


