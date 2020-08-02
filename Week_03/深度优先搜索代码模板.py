     

#dfs代码模板,递归版
def dfs(node):
    if node in visited:
    #already visited
        return
    visited.add(node)
    #process current node
    #...#logic here
    dfs(node.left)
    dfs(node.rihgt)


#多叉树的dfs
visited = set()
def dfs(node, visited):
    visited.add(node)
    #process current node here.
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next node, visited)
















