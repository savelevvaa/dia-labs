class Unique(object):
    def __init__(self, items, **kwargs):
        self.i = 0
        for k, v in kwargs.items():
            self.iCase = v
            break
        self.uniqueItems = set()
        self.temp = []
        self.items = items

    def __next__(self):
        if self.iCase == False:
            for i in self.items:
                self.temp.append(str(i).upper())
        else:
            self.temp = self.items
        while True:
            if self.i >= len(self.items):
                raise StopIteration
            else:
                item = self.temp[self.i]
                self.i = self.i + 1
                if item not in self.uniqueItems:
                    self.uniqueItems.add(item)
                    return item

    def __iter__(self):
        return self

# list1 = [1,2,3,4,4,3,2,4,5,3,6,7,8]
# list2 = ['a','B','c','d','c','e','a','B','C','A','b']
# list3 = ['a','B',1,'c','d',3,'c','e',3,'a','B',2,'C',5,'A',5,'b']
#
# for i in Unique(list3, ignore=False):
#     print(i)

