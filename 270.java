/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int closestValue(TreeNode root, double target) {
        int closest = root.val;
        if (root.val < target) {
            if (root.right != null) {
                int right = closestValue(root.right, target);
                if (Math.abs(right - target) < Math.abs(closest - target)) {
                    closest = right;
                }
            }
        } else {
            if (root.left != null) {
                int left = closestValue(root.left, target);
                if (Math.abs(left - target) < Math.abs(closest - target)) {
                    closest = left;
                }
            }
        }
        return closest;
    }
}
