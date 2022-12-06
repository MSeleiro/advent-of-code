import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;

/**
 * --- Day 6: Tuning Trouble ---
 */

public class Main {
    private static int res = 0;
    private static int res2 = 0;
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
        System.out.println(res2);
    }

    private static void solve(String line) {
        res = findWhen(line, 4);
        res2 = findWhen(line, 14);
    }

    private static int findWhen(String line, int num) {
        for (int i = 0; i < line.length() - num; ++i) {
            final int in = i;
            if (new HashSet<>(){{ for (char c : line.substring(in, in + num).toCharArray()) add(c); }}.size() == num) {
                return i + num;
            }
        }
        return -1;
    }
}
