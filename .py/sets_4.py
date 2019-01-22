bravo = {"z","y","x","w","v"}
charlie = alpha.union(bravo)
charlie.update("g","h","i","j","k")
for x in charlie:
  print(x," ",end="")
print()
#pop all the records 
for i in range(len(charlie)):
	print("pop ",i," ",end="")
	thepop = charlie.pop()
	print (thepop)
	
	

"""
the union method combiones two sets and
updates itself.
notice the update function.
you can not pop from an empty setself.
the concept of "pop" is an important
function in data structurest that resemble. 
