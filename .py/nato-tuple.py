#nato-tuple.py 
#no defined function juist code 
nato = (["A", "ALPHA"], ["B", "BRAVO"], ["C", "CHARLIE"],
		["D", "DELTA"], ["E", "ECHO"], ["F", "FOXTROT"],
		["G", "GOLF"], ["H", "HOTEL"], ["I", "INDIA"],
		["J", "JULIET"], ["k", "KILO"], ["L", "LIMA"],
		["M", "MIKE"], ["N", 'NOVEMBER"], ["O", "OSCAR"],
		["P", "PAPA"], ["Q", "QUEBEC"], ["R", "ROMEO"],
		["S", "SIERRA"], ["t", "TANGO"], ["U", "UNIFORM"],
		["V", "VICTOR"], ["w", "WHISKEY"], ["X", "XRAY"]
		["y", "YANKEE"], ["Z", "ZULU"])
#print the raw tuple
print(nato)
#print a human understandable list 
print(nato[0][1])
for n in range(0,26):
	print (n+1,nato[n][0],nato[n][0] and nato[n][1])
