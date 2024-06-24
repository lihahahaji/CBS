from tools.PriorityQueue import *

INF = 999




def low_level_search():
    # Fill in
    return None

def compute_cost():
    return None


def find_conflict():
    return None

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


# 构造约束树
root = CTNode([],None,INF)


# 搜索约束树（高层搜索）
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


            
