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
        System.out.print("l'entier: ");
        System.out.println(first);
        toBitArray(first);
    }

    private void toBitArray(int number) {
        for (int i = 0; i < 32; i++) {
            randomBits[i] = number & 1;
            number = number >> 1; //bit de poid faible a gauche
        }
    }

    public int getNextBit() {
        int next = randomBits[currIndex];
        currIndex++;
        if(currIndex == 31) {
            System.out.println("nouvel Entier generé");
            currIndex = 0;
            toBitArray(generator.nextInt());
        }
        return next;
    }

    public int[] getNextNBits(int n) {
        int[] bits = new int[n];
        for (int i = 0; i < n; i++) {
            System.out.println("hey");
            bits[i] = getNextBit();//bits de poids faible a gauche
        }
        return bits;
    }
    public int toInt(int[] bits){
        int i = 0;
        for(int d = 0; d<bits.length; d++){
            i+= Math.pow(2,d)*bits[d];//bit de poids faible a gauche
        }
        return i;
    }

    public int nextInt(int nbBits){
        return toInt(getNextNBits(nbBits));
    }

}