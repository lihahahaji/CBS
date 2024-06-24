# CBS
Conflict-based search

## MAPF问题定义
#### 问题输入
- 有向图  $G(V, E)$ ，图中的顶点代表智能体可能的位置，边代表位置间的可能转移。
- 定义了 $k$ 个智能体，每个智能体 $a_i$ 都有一个起始顶点 $ start_i \in V $ 和一个目标顶点 $ goal_i \in V $。
- 将时间离散化为时间点。在时间点 $t_0$，智能体 $a_i$ 位于位置 $start_i$。

## 约束树（CT）
#### 树节点结构
- 约束：根节点为空约束，字节点继承父节点的约束。
- 解决方案： 每个智能体各自符合约束的路径。
- 总成本： 所有智能体的路径成本之和。
```python
class CTNode:
    def __init__(self):
        self.constraints = []
        self.solution = self.get_solution()
        self.cost = self.get_cost()

    # 根据约束，调用低层搜索方法来获取 solution
    def get_solution(self):
        self.solution = low_level_search(self.constraints)

    # 根据 solution，计算 cost
    def get_cost(self):
        self.cost = compute_cost(self.solution)
```

#### 约束树搜索流程（高层搜索）
- 初始化：构造一棵约束树（只包含根节点），根节点的约束为空集，根据该约束为每个机器人找到路径（解决方案），计算总成本。
- 冲突检测：对于当前节点，验证解决方案中的路径集合是否存在冲突，若没有发现冲突，则发现最优解，反之进入下一步。
- 冲突解决（分支）：检测到冲突时，生成新的字节点，对于两个智能体之间的冲突，会生成两个子节点，每个子节点添加一个新的约束来解决冲突。一个子节点添加约束以排除第一个智能体在冲突位置和时间的占用，另一个子节点添加约束以排除第二个智能体的占用。
- 递归搜索：子节点被加入搜索队列中，等待进一步处理，直到找到一个没有冲突的解决方案。
- 节点处理：一个未被处理的节点在初始状态下只有约束，缺少解决方案和总成本。节点处理的过程就是根据约束条件，调用低层的搜索算法来为每一个机器人找到路径，并且计算总成本。
- 搜索策略：约束树算法使用优先队列来作为搜索队列，根据节点的总成本来进行排序，从而保证最先找到的就是最优的解决方案。

```python
def high_level_search():
    openList = PriorityQueue()
    openList.enqueue(root)
    while openList.__len__(): 
        node = openList.dequeue()
        # 冲突检测
        if find_conflict(node.solution) == None:
            return node
        else:
            conflict = find_conflict(node.solution)
            for constrain in conflict.constrain_list:
                A_node = CTNode()
                A_node.constraints = node.constraints
                A_node.constraints.append(constrain)
                A_node.get_solution()
                A_node.get_cost()
                if A_node.cost != INF: openList.enqueue(A_node)
    return None  
```
## 低层搜索
#### Space-Time A*