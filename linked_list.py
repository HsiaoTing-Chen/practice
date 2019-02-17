class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def sort(self):
        p1 = self.headval
        p2 = self.headval
        print("p1 ",p1)
        print("p2 ",self.headval.nextval)
        print("p3 ",self.headval.nextval.nextval)
        print("p4 ",self.headval.nextval.nextval.nextval)
        print("p5 ",self.headval.nextval.nextval.nextval.nextval)
        t = 0
        while p2 is not None:
            print("p1 ",p1)
            print("p2 ",p2)
            print("-----")
            if (p1 is None):
                print("p1 is none",p1)
                t = 1
                p1 = self.headval
            else:
                p1 = p1.nextval

            if (t == 1):
                p1.nextval = p2
            p1 = p1.nextval
            p2 = p2.nextval

            if (p1==p2):
               return


list = SLinkedList()
list.headval = Node("a1")
e2 = Node("a2")
e3 = Node("b1")
e4 = Node("b2")

list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
list.listprint()

print("-------after sort---------")
list.sort()
list.listprint()

