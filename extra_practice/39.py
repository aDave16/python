#Find item from list tuple e.g lst_tpl_item = [(12,23,56),(34,54,65),(45,65,78)]
#12 in (12,23,56) tuple
lst_tpl_item = [(12,23,56),(34,54,65),(45,65,78)]
find=12
ans=(i for i in lst_tpl_item if find in i)
a=list(ans)
b=tuple(a)
print(f"{find} in {b}")
#print(f"{find} in {list(ans)}")