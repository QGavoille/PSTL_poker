import java.util.Random;

public class RandomGenerator {
    private Random generator;
    private int currIndex;
    private int[] randomBits;

    public RandomGenerator() {
        generator = new Random(System.currentTimeMillis());
        currIndex = 0;
        randomBits = new int[32];
        int first = generator.nextInt();
        toBitArray(first);
    }

    private void toBitArray(int number) {
        for (int i = 0; i < 32; i++) {
            randomBits[i] = number & 1;
            number = number >> 1;
        }
    }

    public int getNextBit() {
        int next = randomBits[currIndex];
        currIndex++;
        if(currIndex == 31) {
            currIndex = 0;
            toBitArray(generator.nextInt());
        }
        return next;
    }

    public int[] getNextNBits(int n) {
        int[] bits = new int[n];
        for (int i = 0; i < n; i++) {
            bits[i] = getNextBit();
        }
        return bits;
    }

}