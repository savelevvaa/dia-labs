class Unique():
    def __init__(self, items, **kwargs):
        ignore = kwargs["ignore"] if "ignore" in kwargs else False
        self.uniqueItems = set()
        for i in items:
            if isinstance(i, str) and ignore:
                self.uniqueItems.add(i.lower())
            else:
                self.uniqueItems.add(i)

    def __next__(self):
        if len(self.uniqueItems) > 0:
            return self.uniqueItems.pop()
        raise StopIteration()

    def __iter__(self):
        return self

def main():
    print("\033[33mlist1\033[0m:        ", list1)
    print("\033[36mUnique list1\033[0m: ", sorted(list(Unique(list1))), "\n")

    print("\033[33mlist2\033[0m:        ", list2)
    print("\033[36mUnique list2\033[0m: ", sorted(list(Unique(list2, ignore=False))), "\n")
    print("\033[33mlist2\033[0m:                        ", list2)
    print("\033[36mUnique list2\033[0m(\033[31mignore = True\033[0m):  ", sorted(list(Unique(list2, ignore=True))), "\n")

    print("\033[33mlist3\033[0m:        ", list3)
    print("\033[36mUnique list3\033[0m: ", list(Unique(list3, ignore=False)), "\n")
    print("\033[33mlist3\033[0m:                        ", list3)
    print("\033[36mUnique list3\033[0m(\033[31mignore = True\033[0m):  ", list(Unique(list3, ignore=True)),
          "\n")


list1 = [1,2,3,4,4,3,2,4,5,3,6,7,8]
list2 = ['a','B','c','d','c','e','a','B','C','A','b']
list3 = ['a','B',1,'c','d',3,'c','e',3,'a','B',2,'C',5,'A',5,'b']


if __name__ == "__main__":
    main()


