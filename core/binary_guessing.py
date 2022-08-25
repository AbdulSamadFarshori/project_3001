data = {
    1: {0:{ "pos":"root", "question":"your name starts with a", "yes":2, "no":3}},
    2: {1:{ "pos":"yes", "question":"you are elder?", "yes":4, "no":5}},
    3: {1:{ "pos":"no", "question":"your Name start with s?","yes":6, "no":7}},
    4: {2:{ "pos":"yes", "question": "your are aleem", "yes":None, "no":None}},
    5: {2:{ "pos":"no", "question": "your are three brothers elder brother name start with a","yes":None, "no":None}},
    6: {3:{ "pos":"yes", "question":"your height is about 6 feets?","yes":8, "no":9}},
    7: {3:{ "pos":"no", "question":"you are a liar", "yes":None, "no":None}},
    8: {6: { "pos":"yes", "question":"you are sami", "yes":None, "no":None}},
    9: {6: { "pos":"no", "question":"you are sumir", "yes":None, "no":None}}
}

class Node(object):
    
    def __init__(self, ids , parent, pos, question, yesnode, nonode):
        self.ids = ids
        self.parent = parent
        self.pos = pos
        self.question = question
        self.yesnode = yesnode
        self.nonode = nonode
    
class ShowCurrentNode(object):
    def __init__(self, data):
        self.root = None
        self.yesnode = None
        self.nonode = None
        self.start = 1
        self.data = data
        
    def getparent(self):
        parent = list(self.data[self.start].keys())[0]
        return parent
        
    def getchildren(self):
        yeschildpos = self.data[self.start][self.getparent()]["yes"]
        nochildpos = self.data[self.start][self.getparent()]["no"]
        return yeschildpos, nochildpos
        
    def getroot(self):
        root_data = self.data[self.start][self.getparent()]
        yes, no = self.getchildren()
        self.root = Node(self.start, self.getparent(), root_data["pos"], root_data["question"], yes, no)
        return self.root
    
    def getyesnode(self):
        yes, no = self.getchildren()
        get_parent = list(self.data[yes].keys())[0]
        root_data = self.data[yes][get_parent]
        
        self.yesnode = Node(self.start, get_parent, root_data["pos"], root_data["question"], root_data["yes"], root_data["no"])
        return self.yesnode
    
    def getnonode(self):
        yes, no = self.getchildren()
        get_parent = list(self.data[yes].keys())[0]
        root_data = self.data[no][self.start]
        
        self.nonode = Node(self.start, get_parent, root_data["pos"], root_data["question"], root_data["yes"], root_data["no"])
        return self.nonode
        
    def gettree(self):
        r = self.getroot()
        y = self.getyesnode()
        n = self.getnonode()
        print(f"root : {r.question}")
        print()
        print(f"No-node: - {n.question}   Yes-node: - {y.question}")
        pass
    
    def reply(self):
        foo = True
        while foo:
            if self.getroot().yesnode == None and self.getroot().nonode == None:
                foo = False
            r = self.getroot()
            print(f"root : {r.question}")
            print()
            print(" yes or no")
            print()
            x = input("type here: ")
            if x == "yes":
                self.start = r.yesnode
            if x == "no":
                self.start = r.nonode

    
print(ShowCurrentNode(data).reply())