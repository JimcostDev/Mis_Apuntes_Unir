public class Main {
    public static void main(String[] args) {
        BinarySearchTree premierLeagueTree = new BinarySearchTree();

        // Insertar equipos
        premierLeagueTree.insert(new PremierLeagueTeam("Manchester City", 76));
        premierLeagueTree.insert(new PremierLeagueTeam("Liverpool", 74));
        premierLeagueTree.insert(new PremierLeagueTeam("Chelsea", 70));
        premierLeagueTree.insert(new PremierLeagueTeam("Manchester United", 68));
        premierLeagueTree.insert(new PremierLeagueTeam("Arsenal", 66));

        // Realizar recorridos
        System.out.println("Recorrido en preorden:");
        premierLeagueTree.preOrderTraversal();

        System.out.println("\nRecorrido en inorden:");
        premierLeagueTree.inOrderTraversal();

        System.out.println("\nRecorrido en posorden:");
        premierLeagueTree.postOrderTraversal();
        System.out.println();
      

        // Borrar un equipo
        premierLeagueTree.delete(new PremierLeagueTeam("Chelsea", 70));

        // Imprimir el árbol después de borrar
        System.out.println("\nEquipo borrado:");
        premierLeagueTree.printTree();
    }
}
