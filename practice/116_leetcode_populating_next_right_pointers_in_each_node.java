// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

class Solution {
    
    public Node connect(Node root) {
        return subSolution(root, null);
    }
    
    public Node subSolution(Node node, Node parent) {
        if (node == null) return null;
        if (parent != null) {
            if (parent.right != null && node != parent.right) {
                node.next = parent.right;
            } else if (parent.next != null) {
                node.next = parent.next.left;
            }
        }
        subSolution(node.left, node);
        subSolution(node.right, node);
        return node;
    }

    // Definition for a Node.
    class Node {
        public int val;
        public Node left;
        public Node right;
        public Node next;

        public Node() {}

        public Node(int _val,Node _left,Node _right,Node _next) {
            val = _val;
            left = _left;
            right = _right;
            next = _next;
        }
    }
}