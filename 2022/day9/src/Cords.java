import java.util.LinkedList;
import java.util.List;

public class Cords {
    // line
    int x;
    // column
    int y;

    public Cords(int i, int j){
        this.x = i;
        this.y = j;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + x;
        result = prime * result + y;
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Cords other = (Cords) obj;
        if (x != other.x)
            return false;
        if (y != other.y)
            return false;
        return true;
    }

    public Cords move(Movement m) {
        return new Cords(this.x + m.lineChange, this.y + m.colChange);
    }

    private static List<Cords> applyAllMovements(Cords c) {
        List<Cords> cords = new LinkedList<>();
        for (Movement m : Movement.values()) {
            cords.add(c.move(m));
        }
        cords.add(c);
        return cords;
    }

    public static boolean isInRange(Cords c, Cords c1) {
        return applyAllMovements(c).contains(c1);
    }

    public List<Cords> getPossCords(Cords c) {
        List<Cords> possCords = new LinkedList<>();
        for (Movement m : Movement.values()) {
            Cords tmp = this.move(m);
            if (Cords.isInRange(tmp, c)) {
                possCords.add(tmp);
            }
        }
        return possCords;
    }

    public static int compareTo(Cords c1, Cords c2, Cords dest) {
        if (c1.x == dest.x || c1.y == dest.y) {
            return -1;
        }
        if (c2.x == dest.x || c2.y == dest.y) {
            return 1;
        }
        return 0;
    }
}
