public class PremierLeagueTeam {
    String name;
    int points;

    public PremierLeagueTeam(String name, int points) {
        this.name = name;
        this.points = points;
    }

    // sobrescritura del metodo
    @Override
    public String toString() {
        return name + " (" + points + " puntos)";
    }
}
