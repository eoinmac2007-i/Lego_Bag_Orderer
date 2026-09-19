class LegoSet:
    def __init__(self, name, bags, numList):
        self.name = name
        self.bags_tot = bags
        self.bags_remain = bags
        self.numList = numList
        self.bags_used = 0
        self.frac = 0
    
    def __lt__(self, other):
        if self == other:
            if self.frac < 0.5:
                return self.bags_tot > other.bags_tot
            else:
                return self.bags_tot < other.bags_tot
        else:
            return self.frac <= other.frac
        
        
    def __eq__(self, other):
        return self.frac == other.frac
        
    def incrementBag(self, count):
        if self.frac <= 1:
            print(f"{count}. Build '{self.name}' Bag #{self.numList[self.bags_used]} Fraction: {self.frac}")
            self.bags_used += 1
            self.bags_remain -= 1
            self.frac = self.bags_used / (self.bags_tot - 1)
    
    def __str__(self):
        return self.name

def printBagOrder(setList):
    count = 0
    while not allDone(setList):
        count += 1
        nextSet = setList[0]
        for lego_set in setList:
            if lego_set < nextSet:
                nextSet = lego_set
        nextSet.incrementBag(count)
    
def allDone(setList):
    for lego_set in setList:
        if lego_set.bags_remain != 0:
            return False
    return True

def printList(setList):
    returnStr = "["
    for elem in setList:
        returnStr += str(elem) + ", "
    returnStr = "]"
    return(returnStr)
        

setList = []
setList.append(LegoSet("Luigi Kart", 22, list(range(1,23))))
setList.append(LegoSet("Mighty Bowser", 18, list(range(5,23))))
setList.append(LegoSet("Mario Kart", 17, list(range(1,18))))
setList.append(LegoSet("Atari", 16, [3,4,2,5,6,7,1,9,10,8,11,12,13,16,14,15]))
setList.append(LegoSet("Mario & Yoshi", 15, list(range(1,16))))
setList.append(LegoSet("? Block", 13,list(range(1,14))))
setList.append(LegoSet("NES TV", 13,list(range(9,22))))
setList.append(LegoSet("Lego NES", 8,list(range(1,9))))
setList.append(LegoSet("Piranha Plant", 6,list(range(1,7))))
setList.append(LegoSet("Game Boy", 5,list(range(1,6))))
setList.append(LegoSet("Bowser Stand", 4,list(range(1,5))))
setList.sort(reverse = True)
printList(setList)
printBagOrder(setList)
