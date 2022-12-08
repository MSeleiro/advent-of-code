import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;

/**
 * --- Day 8: Treetop Tree House ---
 */

public class Main {
    private static List<List<Integer>> patch = new LinkedList<>();
    private static int res = 0;
    private static int res2 = 0;
    public static void main(String[] args) {
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
        for (int i = 0; i < patch.size(); ++i) {
            List<Integer> column = patch.get(i);
            for (int k = 0; k < column.size(); ++k) {
                if (checkVisible(i, k)) {
                    res += 1;
                }

                int value = getTreeValue(i, k);
                if (value > res2) {
                    res2 = value;
                }
            }
        }
    }

    private static boolean checkVisible(int i, int k) {
        return checkLoop(i, k, 1, 0) || checkLoop(i, k, -1, 0) ||
                checkLoop(i, k, 0, 1) || checkLoop(i, k, 0, -1);
    }

    private static int getTreeValue(int i, int k) {
        return checkLoop2(i, k, 1, 0) * checkLoop2(i, k, -1, 0) *
                checkLoop2(i, k, 0, 1) * checkLoop2(i, k, 0, -1);
    }

    private static boolean checkLoop(int i, int k, int i1, int k1) {
        int height = patch.get(i).get(k);
        i = i + i1;
        k = k + k1;
        while (i >= 0 && k >= 0 && i < patch.size() && k < patch.get(i).size()) {
            if (height <= patch.get(i).get(k)) {
                return false;
            }
            i = i + i1;
            k = k + k1;
        }
        return true;
    }

    private static int checkLoop2(int i, int k, int i1, int k1) {
        int height = patch.get(i).get(k);
        i = i + i1;
        k = k + k1;
        int count = 0;
        while (i >= 0 && k >= 0 && i < patch.size() && k < patch.get(i).size()) {
            if (height <= patch.get(i).get(k)) {
                return ++count;
            } else {
                ++count;
                i = i + i1;
                k = k + k1;
            }
        }
        return count;
    }

    private static void build(String line) {
        char[] heights = line.toCharArray();
        for (int i = 0; i < heights.length; ++i) {
            if (patch.size() == i) {
                patch.add(new LinkedList<>());
            }
            patch.get(i).add(Integer.parseInt("" + heights[i]));
        }
    }
}
