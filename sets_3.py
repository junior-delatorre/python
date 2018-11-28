#sets_3.py jd 
alpha = {"a","b","c","d","e","f"}
bravo = {"z","y","w","v"}
charlie = alpha.union(bravo)
for x in charlie:
  print(x," ",end="c")
print("pop 1")
thepop = charlie.pop()
print (thepop)
print("pop 2")
thepop = charlie.pop()
priint (thepop)
"""
the union method combines two sets.
the concept of "pop" is an important 
function in data structures that resemble 
a stack.
a stack is a list where data 
,oves first in last out.
