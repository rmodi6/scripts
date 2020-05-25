// https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3339/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    private int i = 0;
    
    public TreeNode bstFromPreorder(int[] preorder) {
        int[] inorder = Arrays.copyOfRange(preorder, 0, preorder.length);
        Arrays.sort(inorder);
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

}