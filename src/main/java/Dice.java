public class Dice {
    private RandomGenerator generator;

    public Dice(RandomGenerator generator) {
        this.generator = generator;
    }
    public Dice() {
        this(new RandomGenerator());
    }

    public int rollNonUniform() {
        int[] bits = generator.getNextNBits(3);
        int value = 0;
        for (int i = 0; i < 3; i++) {
            value += bits[i] * Math.pow(2, i);
        }
        return value % 6;
    }
}
