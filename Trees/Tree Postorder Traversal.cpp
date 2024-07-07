

// https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

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

    void traverse(Node* root,vector<int> &ans){
        if (!root) return ;
        // traverse the children first 
        for (auto &child : root->children) traverse(child,ans);
        // after traversing children , go for root
        ans.push_back(root->val);
    }

    vector<int> postorder(Node* root) {
        vector<int> ans;       
        traverse(root,ans);
        return ans ;
    }
};
