def sequentialSearch(l, item):
    found = False
    if not found:
        for i in range(len(l)):
            if l[i] == item:
                found = True
                print(found, 'index:', i)
    if not found:
        print(found)

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
sequentialSearch(testlist, 32)
print(32 in testlist)
