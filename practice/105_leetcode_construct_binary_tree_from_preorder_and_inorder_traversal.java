// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

import java.util.Arrays;
import java.util.ArrayList;

class Solution {

    private int i = 0;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return subtree(preorder, inorder);
    }

    public TreeNode subtree(int[] preorder, int[] inorder) {
        if (preorder == null || preorder.length == 0)
            return null;
        TreeNode root = new TreeNode(preorder[i]);
        int j;
        for (j = 0; j < inorder.length; j++) {
            if (preorder[i] == inorder[j]) {
                break;
            }
        }
        if (j > 0) {
            i++;
            root.left = subtree(preorder, Arrays.copyOfRange(inorder, 0, j));
        }
        if (j < inorder.length - 1) {
            i++;
            root.right = subtree(preorder, Arrays.copyOfRange(inorder, j + 1, inorder.length));
        }

        return root;
    }

    // Definition for a binary tree node.
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

}