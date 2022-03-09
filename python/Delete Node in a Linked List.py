class Solution:
    def deleteNode(self, node):
        tmp = node.next
        node.val = tmp.val
        node.next = tmp.next