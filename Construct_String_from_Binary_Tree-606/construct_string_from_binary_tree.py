class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t: return ""
        
        left, right = "", ""
        if t.left or t.right:
            left = f"({self.tree2str(t.left)})"
        if t.right:
            right = f"({self.tree2str(t.right)})"
        
        return f"{t.val}{left}{right}"

