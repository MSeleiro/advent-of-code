import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 * --- Day 4: Camp Cleanup ---
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
        String[] sections = line.split(",");
        String[] elf1 = sections[0].split("-");
        String[] elf2 = sections[1].split("-");
        int start1 = Integer.parseInt(elf1[0]);
        int start2 = Integer.parseInt(elf2[0]);
        int end1 = Integer.parseInt(elf1[1]);
        int end2 = Integer.parseInt(elf2[1]);
        if(start1 <= start2 && end2 <= end1 || start1 >= start2 && end2 >= end1) {
            res++;
            res2++;
        } else if (start1 <= end2 && end1 >= start2) {
            res2++;
        }
    }
}