import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 * --- Day X: ... ---
 */

public class Main {
    private static int res = 0;
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
    }

    private static void solve(String line) {
        
    }
}
