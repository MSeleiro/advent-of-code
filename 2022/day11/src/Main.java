import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;

/**
 * --- Day 11: Monkey in the Middle ---
 */

public class Main {
    private static final int ROUNDS = 20;
    private static final int ROUNDS2 = 10_000;
    private static final LinkedList<Monkey> monkeys = new LinkedList<>();
    private static final LinkedList<Monkey> monkeys2 = new LinkedList<>();
    public static void main(String[] args) {
        BufferedReader reader;
        try {
            reader = new BufferedReader(new FileReader("input.txt"));
            String line = reader.readLine();
            while (line != null) {
                if (line.startsWith("Monkey"))
                    build(line, reader);
                line = reader.readLine();
            }
            solve();
            solve2();
            end();
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void end() {
        System.out.print("part 1: ");

        monkeys.sort(Monkey::sortInspections);
        System.out.println(monkeys.get(0).inspections * monkeys.get(1).inspections);

        System.out.print("part 2 (WRONG): ");

        monkeys2.sort(Monkey::sortInspections);
        System.out.println(monkeys2.get(0).inspections + "*" + monkeys2.get(1).inspections);
    }

    private static void solve() {
        for (int i = 0; i < ROUNDS; i++) {
            for (Monkey m : monkeys) {
                while (m.items.size() > 0) {
                    long worry = (int) (m.inspect() / 3);
                    monkeys.get(m.test(worry)).items.add(worry);
                }
            }
        }
    }

    // coded correctly, but wrong results after many attempts for unknown reasons, don't use
    private static void solve2() {
        int mod = 1;
        for (Monkey m : monkeys2) {
            mod = mod * m.test;
        }
        for (int i = 0; i < ROUNDS2; i++) {
            for (Monkey m : monkeys2) {
                while (m.items.size() > 0) {
                    long worry = m.inspect() % mod;
                    monkeys2.get(m.test(worry)).items.add(worry);
                }
            }
        }
    }

    private static void build(String line, BufferedReader reader) throws IOException {
        int num = Integer.parseInt("" + line.charAt(line.length() - 2));
        LinkedList<Long> items = new LinkedList<>() {{
            String[] items = reader.readLine().trim().split(", ");
            items[0] = items[0].replace("Starting items: ", "");
            for (String s : items) {
                add(Long.parseLong(s));
            }
        }};
        String opr = reader.readLine().trim().replace("Operation: new = old ", "");
        int test = Integer.parseInt(reader.readLine().trim().replace("Test: divisible by ", ""));
        int t = Integer.parseInt(reader.readLine().trim().replace("If true: throw to monkey ", ""));
        int f = Integer.parseInt(reader.readLine().trim().replace("If false: throw to monkey ", ""));
        monkeys.add(new Monkey(num, items, opr, test, t, f));
        monkeys2.add(new Monkey(num, items, opr, test, t, f));
    }
}
