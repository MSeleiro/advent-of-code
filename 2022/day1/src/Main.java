import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

/**
 * --- Day 1: Calorie Counting ---
 */

public class Main {
    public static void main(String[] args) {
        BufferedReader reader;
        List<Integer> calories = new LinkedList<>();
        try {
            reader = new BufferedReader(new FileReader("input.txt"));
            String line = reader.readLine();
            int acc = 0;
            while (line != null) {
                if (line.isBlank()) {
                    calories.add(acc);
                    acc = 0;
                } else {
                    acc += Integer.parseInt(line);
                }
                line = reader.readLine();
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        Collections.sort(calories);
        Collections.reverse(calories);
        System.out.println(calories.get(0));
        System.out.println(calories.get(0) + calories.get(1) + calories.get(2));
    }
}