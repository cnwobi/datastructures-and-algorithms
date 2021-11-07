from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}"


def uni_tree_count(root: TreeNode):
    if not root:
        return 0
    count = 0

    def is_uni_tree(root: TreeNode):
        nonlocal count
        if root.right is None and root.left is None:
            count += 1
            return True
        is_uni = True
        if root.left:
            is_uni = is_uni and is_uni_tree(root.left) and root.left.val == root.val
        if root.right:
            is_uni = is_uni_tree(root.right) and root.right.val == root.val and is_uni
        if is_uni:
            count += 1
        return is_uni

    is_uni_tree(root)
    return count


def longestUnivaluePath(root: Optional[TreeNode]) -> int:
    longest = 0

    def longest_unival(root):
        nonlocal longest
        if not root.left and not root.right:
            longest = max(longest, 1)
            return 1
        left = 0
        right = 0
        if root.left:
            left = longest_unival(root.left)
        if root.right:
            right = longest_unival(root.right)
        left = left if root.left and root.left.val == root.val else 0
        right = right if root.right and root.right.val == root.val else 0

        longest = max(longest, left + right)
        return max(left, right) + 1

    longest_unival(root)
    return longest


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)

    print(root)

    print(longestUnivaluePath(root))
