from collections import Counter

class Solution(object):
    def findMode(self, root):
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        counts = Counter(inoder(root))
        max_freq = max(counts.values())
        return [val for val, freq in counts.items() if freq == max_freq]