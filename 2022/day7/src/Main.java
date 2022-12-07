import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 * --- Day 7: No Space Left On Device ---
 */

public class Main {
    private static Dir baseDir;
    private static Dir currDir;
    private static int res = 0;
    private static int res2 = Integer.MAX_VALUE;
    public static void main(String[] args) {
        baseDir = new Dir("/", null);
        BufferedReader reader;
        try {
            reader = new BufferedReader(new FileReader("input.txt"));
            String line = reader.readLine();
            while (line != null) {
                build(line);
                line = reader.readLine();
            }
            solve();
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

    private static void solve() {
        // part 1
        dive(baseDir);

        // part 2
        int neededSpace = 30_000_000 - (70_000_000 - baseDir.size);
        findNearestTo(neededSpace, baseDir);
    }

    private static void findNearestTo(int neededSpace, Dir d) {
        if (d.size > neededSpace && res2 > d.size)  {
            res2 = d.size;
        }
        for (Dir subD : d.subDir.values()) {
            findNearestTo(neededSpace, subD);
        }
    }

    private static void dive(Dir d) {
        for (Dir subD : d.subDir.values()) {
            dive(subD);
        }
        d.calcSize();
        if (d.size <= 100_000) {
            res += d.size;
        }
    }

    private static void build(String line) {
        String[] lineParts = line.split(" ");
        if (lineParts[0].equals("$")) {
            if (lineParts[1].equals("cd")) {
                currDir = switch (lineParts[2]) {
                    case ".." -> currDir.parent;
                    case "/"  -> baseDir;
                    default   -> currDir.subDir(lineParts[2]);
                };
            }
        } else {
            if (lineParts[0].equals("dir")) {
                currDir.addDir(lineParts[1], new Dir(lineParts[1], currDir));
            } else {
                currDir.addFile(Integer.parseInt(lineParts[0]), lineParts[1]);
            }
        }
    }
}
