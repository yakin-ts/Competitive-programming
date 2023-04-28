class ThroneInheritance:

    def __init__(self, kingName: str):
        self.family = defaultdict(list)
        self.king = kingName
        self.dead = defaultdict(bool)
        
    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead[name] = True

    def getInheritanceOrder(self) -> List[str]:
        visited = set()
        curOrder = [self.king] if not self.dead[self.king] else []

        def successor(parent, curOrder):
            if parent not in visited:
                visited.add(parent)
                for child in self.family[parent]:
                    if not self.dead[child]:
                        curOrder.append(child)
                    successor(child,curOrder)
            return curOrder
        
        return successor(self.king, curOrder)




        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()