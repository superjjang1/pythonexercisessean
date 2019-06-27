mylist = ["a", "b", "c", "c"]
res = []
for let in mylist:
    if let not in res:
        res.append(let)
print(res)

mylist2 = [4, 4, "another", "another", "guy", 4, 4]
results = []
for item in mylist2:
    if item not in results:
        results.append(item)
print(results)
