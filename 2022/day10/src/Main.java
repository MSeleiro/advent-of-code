import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

/**
 * --- Day 10: Cathode-Ray Tube ---
 */

public class Main {
    public static final int LENGTH = 40;
    private static final int[] CHECKPOINTS = new int[] { 20, 60, 100, 140, 180, 220 };

    private static int X = 1;
    private static int cycles = 0;

    private static int res = 0;
    private static String res2 = "";

    public static void main(String[] args) {
        BufferedReader reader;
        try {
            reader = new BufferedReader(new FileReader("input.txt"));
            String line = reader.readLine();
            while (line != null) {
                solve(line);
                line = reader.readLine();
            }
            end();
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void end() {
        System.out.println(res);
        int i = 0;
        for (char c : res2.toCharArray()) {
            System.out.print(c);
            ++i;
            if (i % LENGTH == 0) {
                System.out.println();
            }
        }
    }

    private static void solve(String line) {
        compute(line);
    }

    private static void compute(String line) {
        String[] instruct = line.split(" ");
        switch (instruct[0]) {
            case "noop" -> completeCycle();
            case "addx" -> {
                completeCycle();
                completeCycle();
                X += Integer.parseInt(instruct[1]);
            }
        }
    }

    private static void completeCycle() {
        res2 += cycles % LENGTH <= X + 1 && cycles % LENGTH >= X - 1 ? "#" :  ".";
        cycles++;
        res += Arrays.stream(CHECKPOINTS).anyMatch(i -> i == cycles) ? cycles * X : 0;
    }
}
