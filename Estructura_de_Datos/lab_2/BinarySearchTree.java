class TreeNode {
    PremierLeagueTeam team;
    TreeNode left;
    TreeNode right;

    public TreeNode(PremierLeagueTeam team) {
        this.team = team;
        this.left = null;
        this.right = null;
    }
}

public class BinarySearchTree {
    private TreeNode root;

    public BinarySearchTree() {
        root = null;
    }

    // Métodos para insertar un equipo en el árbol
    public void insert(PremierLeagueTeam team) {
        root = insertRec(root, team);
    }

    private TreeNode insertRec(TreeNode root, PremierLeagueTeam team) {
        if (root == null) {
            root = new TreeNode(team);
            return root;
        }

        if (team.points < root.team.points) {
            root.left = insertRec(root.left, team);
        } else if (team.points > root.team.points) {
            root.right = insertRec(root.right, team);
        }

        return root;
    }

    // Método para realizar un recorrido en preorden
    public void preOrderTraversal() {
        preOrderTraversalRec(root);
    }

    private void preOrderTraversalRec(TreeNode root) {
        if (root != null) {
            System.out.println(root.team);
            preOrderTraversalRec(root.left);
            preOrderTraversalRec(root.right);
        }
    }

    // Método para realizar un recorrido en inorden
    public void inOrderTraversal() {
        inOrderTraversalRec(root);
    }

    private void inOrderTraversalRec(TreeNode root) {
        if (root != null) {
            inOrderTraversalRec(root.left);
            System.out.println(root.team);
            inOrderTraversalRec(root.right);
        }
    }

    // Método para realizar un recorrido en posorden
    public void postOrderTraversal() {
        postOrderTraversalRec(root);
    }

    private void postOrderTraversalRec(TreeNode root) {
        if (root != null) {
            postOrderTraversalRec(root.left);
            postOrderTraversalRec(root.right);
            System.out.println(root.team);
        }
    }

    // Método para imprimir los elementos del árbol
    public void printTree() {
        System.out.println("Árbol binario de búsqueda (inorden):");
        inOrderTraversal();
    }

    // Método para borrar un equipo del árbol
    public void delete(PremierLeagueTeam team) {
        root = deleteRec(root, team);
    }

    private TreeNode deleteRec(TreeNode root, PremierLeagueTeam team) {
        if (root == null) {
            return root;
        }

        if (team.points < root.team.points) {
            root.left = deleteRec(root.left, team);
        } else if (team.points > root.team.points) {
            root.right = deleteRec(root.right, team);
        } else {
            // Nodo con un solo hijo o sin hijos
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }

            // Nodo con dos hijos, encontrar el sucesor inorden (el menor en el subárbol derecho)
            root.team = minValue(root.right);

            // Borrar el sucesor inorden
            root.right = deleteRec(root.right, root.team);
        }

        return root;
    }

    private PremierLeagueTeam minValue(TreeNode root) {
        PremierLeagueTeam minValue = root.team;
        while (root.left != null) {
            minValue = root.left.team;
            root = root.left;
        }
        return minValue;
    }
}
