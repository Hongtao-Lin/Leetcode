/** Ideas: Use recursive structure.
 *  If the node for deletion has right child, 
 *  then we can copy the left-most val from right subtree and recursively delete from right substree
 */ 

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;
        if (root->val == key) {
            if (!root->right) return root->left;
            // find right min
            TreeNode *p = root->right;
            while (p->left) p = p->left;
            root->val = p->val;
            root->right = deleteNode(root->right, p->val);
        }
        if (root->val > key) root->left = deleteNode(root->left, key);
        if (root->val < key) root->right = deleteNode(root->right, key);
        return root;
    }
};