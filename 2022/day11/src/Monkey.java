import java.util.List;

public class Monkey {
    final int number;
    final List<Long> items;
    final Operation opr;
    final int test, t, f;

    public int inspections = 0;

    public Monkey(int number, List<Long> items, String opr, int test, int t, int f) {
        this.number = number;
        this.items = items;

        final char symbol = opr.charAt(0);
        String s = opr.split(" ")[1];
        this.opr = (n -> {
            long operand = s.equals("old") ? n : Integer.parseInt(s);
            return symbol == '+' ? n + operand : n * operand;
        });

        this.test = test;
        this.t = t;
        this.f = f;
    }

    public long inspect() {
        inspections++;
        return opr.doOpr(items.remove(0));
    }

    public int test(long worry) {
        return worry % test == 0 ? t : f;
    }

    public static int sortInspections(Monkey c1, Monkey c2) {
        return c2.inspections - c1.inspections;
    }

    private interface Operation {
        long doOpr(long n);
    }
}
