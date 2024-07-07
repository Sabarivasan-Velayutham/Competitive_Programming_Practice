

# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/

# python
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/solutions/786364/python-iterative-recursive-explanation/

# c++
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/solutions/1167754/easy-recursive-iterative-solutions-w-comments-and-explanation/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def dfs(self,root, ans):
        if root == None:
            return 
        ans.append(root.val)
        for child in root.children:
            self.dfs(child,ans)

    def preorder(self, root):
        ans = []
        self.dfs(root,ans)
        return ans 
    

# c++ code 

'''
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    void dfs(Node* root ,vector<int> &output )
    {
        if (!root) return ;
        output.push_back(root->val);
        for (auto &child : root->children)
            dfs(child,output);
    }
    
    vector<int> preorder(Node* root) {
        vector<int> output;
        dfs(root,output);
        return output;
    }
};

'''