public enum Plays {
    ROCK("AX"),
    PAPER("BY"),
    SCISSORS("CZ");

    private final String code;

    Plays(String code) {
        this.code = code;
    }

    public int compare(Plays p) {
        if (this.ordinal() == p.ordinal()) return 3;
        if (this.ordinal() - 1 == p.ordinal() || this.ordinal() == 0 && p.ordinal() == 2) { return 6; }
        return 0;
    }

    public static Plays getLose(Plays p) {
        return values()[p.ordinal() - 1 < 0 ? values().length - 1 : p.ordinal() - 1];
    }

    public static Plays getWin(Plays p) {
        return values()[p.ordinal() + 1 == values().length ? 0 : p.ordinal() + 1];
    }

    public static Plays getPlay(String play) {
        for (Plays name : values()) {
            if (name.code.contains(play)) {
                return name;
            }
        }
        return null;
    }
}
