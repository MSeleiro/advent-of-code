import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

/**
 * --- Day 3: Rucksack Reorganization ---
 */

public class Main {
    private static int res = 0;
    private static int res2 = 0;
    public static void main(String[] args) {
        BufferedReader reader;
        try {
            reader = new BufferedReader(new FileReader("input.txt"));
            String line = reader.readLine();
            List<String> groups = new LinkedList<>();
            while (line != null) {
                solve(line);
                groups.add(line);
                if (groups.size() == 3) {
                    solve(groups);
                    groups.clear();
                }
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
        Set<Character> found = new HashSet<>();
        int mid = line.length() / 2;
        String[] sack = { line.substring(0, mid), line.substring(mid) };
        for(char c : sack[0].toCharArray()) {
            if (sack[1].contains("" + c)) {
                if (found.add(c)) {
                    res += letterValue(c);
                }
            }
        }
    }

    private static void solve(List<String> groups) {
        Set<Character> found = new HashSet<>();
        String sack2 = groups.get(1);
        String sack3 = groups.get(2);
        for(char c : groups.get(0).toCharArray()) {
            if (sack2.contains("" + c) && sack3.contains("" + c)) {
                if (found.add(c)) {
                    res2 += letterValue(c);
                }
            }
        }
    }

    private static int letterValue(char c) {
        return Character.isUpperCase(c) ? c - 'A' + 27 : c - 'a' + 1;
    }
}