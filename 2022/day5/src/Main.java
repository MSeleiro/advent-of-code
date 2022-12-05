import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;

/**
 * --- Day 5: Supply Stacks ---
 */

public class Main {
    private static final LinkedList<LinkedList<Character>> stacks = new LinkedList<>();
    private static final LinkedList<LinkedList<Character>> stacks2 = new LinkedList<>();
    public static void main(String[] args) {
        BufferedReader reader;
        try {
            reader = new BufferedReader(new FileReader("input.txt"));
            String line = reader.readLine();
            while (line != null) {
                if (line.startsWith("move")) {
                    solve(line);
                    solve2(line);
                } else {
                    if (!line.equals("")) {
                        build(line);
                    }
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
        for(LinkedList<Character> stack : stacks) {
            System.out.print(stack.getLast());
        }
        System.out.println();
        for(LinkedList<Character> stack : stacks2) {
            System.out.print(stack.getLast());
        }
    }

    private static void build(String line) {
        int currentStack = 0;
        int i = 0;
        while(i < line.length()) {
            if (stacks.size() == currentStack) {
                stacks.add(new LinkedList<>());
                stacks2.add(new LinkedList<>());
            }
            if (line.charAt(i) == '[') {
                stacks.get(currentStack).addFirst(line.charAt(i + 1));
                stacks2.get(currentStack).addFirst(line.charAt(i + 1));
            }
            currentStack++;
            i += 4;
        }
    }

    private static void solve(String line) {
        String[] move = line.split(" ");
        int amount = Integer.parseInt(move[1]);
        int from = Integer.parseInt(move[3]) - 1;
        int to = Integer.parseInt(move[5]) - 1;
        for(int i = 0; i < amount; i++) {
            stacks.get(to).add(stacks.get(from).removeLast());
        }
    }

    private static void solve2(String line) {
        String[] move = line.split(" ");
        int amount = Integer.parseInt(move[1]);
        int from = Integer.parseInt(move[3]) - 1;
        int to = Integer.parseInt(move[5]) - 1;
        int toSize = stacks2.get(to).size();
        for(int i = 0; i < amount; i++) {
            stacks2.get(to).add(toSize, stacks2.get(from).removeLast());
        }
    }
}