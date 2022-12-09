public enum Movement {
    // (line, column)
    LEFT("L", 0, -1),
    RIGHT("R", 0, 1),
    UP("U", -1, 0),
    DOWN("D", 1, 0),
    UP_R("UR", -1, 1),
    UP_L("UL", -1, -1),
    DOWN_R("DR", 1, 1),
    DOWN_L("DL", 1, -1);

    public final String id;
    public final int lineChange;
    public final int colChange;

    Movement(String d, int i, int i1) {
        id = d;
        lineChange = i;
        colChange = i1;
    }

    public static Movement getMovement(String id) {
        for (Movement m : values()) {
            if (id.equals(m.id)) {
                return m;
            }
        }
        return null;
    }
}
