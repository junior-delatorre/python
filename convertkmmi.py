'''
unit converter: miles and kilometers
'''
#convertkmmi.py jd 
def print_menu():
	print('1. killometers to miles')
	print('2. miles to killometers')
	
def km_miles():
	km = float(input('enter distance in killometers: '))
	miles = km / 1.609 
	
	print('Distance in miles: {0}'.format(miles))
	
def miles_km(): 
	miles = float(input('Enter distance in miles: '))
	km = miles * 1.609 
	
	print('Distance in killometers: {0}'.format(km))
	
if __name__== '__main__':
	print_menu()
	choice = input('which conversion would you like to do?: ') 
	if choice == '1':
		km_miles()
	
	if choice == '2': 
		miles_km()
