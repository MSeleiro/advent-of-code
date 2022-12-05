import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 * --- Day 2: Rock Paper Scissors ---
 */

public class Main {
    private static int res1 = 0;
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
            print();
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void print() {
        System.out.println(res1);
        System.out.println(res2);
    }

    private static void solve(String line) {
        String[] plays = line.split(" ");
        Plays opp = Plays.getPlay(plays[0]);
        Plays us = Plays.getPlay(plays[1]);
        if (us != null && opp != null) {
            res1 += us.ordinal() + 1 + us.compare(opp);
        }
        Outcome o = Outcome.getOutcome(plays[1]);
        if (o != null && opp != null) {
            Plays us2 = o.getPlayOutcome(opp);
            res2 += us2.ordinal() + 1 + us2.compare(opp);
        }
    }
}