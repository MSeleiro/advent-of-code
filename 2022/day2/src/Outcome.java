public enum Outcome {
    LOSE("X"),
    DRAW("Y"),
    WIN("Z");

    private final String code;

    Outcome(String code) {
        this.code = code;
    }

    public static Outcome getOutcome(String code) {
        for(Outcome out : values()) {
            if (out.code.equals(code)) {
                return out;
            }
        }
        return null;
    }

    public Plays getPlayOutcome(Plays p) {
        return switch (this) {
            case LOSE -> Plays.getLose(p);
            case WIN -> Plays.getWin(p);
            case DRAW -> p;
        };
    }
}
