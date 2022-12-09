import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;

/**
 * --- Day 9: Rope Bridge ---
 */

public class Main {
    private static final int ROPE_SIZE = 10;
    private static HashSet<Cords> tailVisited = new HashSet<>();
    private static HashSet<Cords> tailVisited2 = new HashSet<>();
    private static LinkedList<Cords> rope2 = new LinkedList<>(); // Index 0 is head, all rest are tails
    private static Cords tail;
    private static Cords head;
    public static void main(String[] args) {
        head = tail = new Cords(0,0);
        tailVisited.add(tail);
        for (int i = 0; i < ROPE_SIZE; ++i) {
            rope2.add(new Cords(0,0));
        }
        tailVisited2.add(new Cords(0,0));
        BufferedReader reader;
        try {
            reader = new BufferedReader(new FileReader("input.txt"));
            String line = reader.readLine();
            while (line != null) {
                solve(line);
                solve2(line);
                line = reader.readLine();
            }
            end();
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void end() {
        System.out.println(tailVisited.size());
        System.out.println(tailVisited2.size());
    }

    private static void solve(String line) {
        String[] move = line.split(" ");
        Movement m = Movement.getMovement(move[0]); assert m != null;
        int times = Integer.parseInt(move[1]);
        for (int i = 0; i < times; ++i) {
            Cords lastHead = head;
            head = head.move(m);
            if (!Cords.isInRange(tail, head)) {
                tail = lastHead;
                tailVisited.add(tail);
            }
        }
    }


    private static void solve2(String line) {
        String[] move = line.split(" ");
        int times = Integer.parseInt(move[1]);
        Movement m = Movement.getMovement(move[0]); assert m != null;
        for (int i = 0; i < times; ++i) {
            rope2.addFirst(rope2.removeFirst().move(m));
            Cords currHead = rope2.get(0);
            if (!Cords.isInRange(rope2.get(1), currHead)) {
                for (int k = 1; k < ROPE_SIZE; ++k) {
                    if (!Cords.isInRange(rope2.get(k), rope2.get(k - 1))) {
                        final Cords dest = rope2.get(k - 1);
                        List<Cords> possCords = rope2.get(k).getPossCords(rope2.get(k - 1));
                        possCords.sort( (c1, c2) -> Cords.compareTo(c1, c2, dest) );
                        rope2.remove(k);
                        rope2.add(k, possCords.get(0));
                        if (k == ROPE_SIZE - 1) {
                            tailVisited2.add(rope2.get(k));
                        }
                    } else {
                        break;
                    }
                }
            }
        }
    }
}
