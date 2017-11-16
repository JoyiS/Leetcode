class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        stack = []
        for item in path.split("/"):
            if item not in [".", "..", ""]:
                stack.append(item)
            if item == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)