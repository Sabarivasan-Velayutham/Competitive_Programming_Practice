

// https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=study-plan&id=level-1

// https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/3196962/c-bfs-dfs-o-n-explained/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution
{
public:
    vector<vector<int>> levelOrder(TreeNode *root)
    {

        vector<vector<int>> ans;
        if (!root)
            return ans;

        queue<TreeNode *> que;
        que.push(root);

        while (!que.empty())
        {
            int tmp_size = que.size();
            vector<int> tmp;
            while (tmp_size--)
            {
                TreeNode *node = que.front();
                tmp.push_back(node->val);
                que.pop();
                if (node->left)
                    que.push(node->left);
                if (node->right)
                    que.push(node->right);
            }
            ans.push_back(tmp);
        }
        return ans;
    }
};
