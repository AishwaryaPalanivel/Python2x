#strings-bunch of characters
#represented by''or""
name1="Yaagavi"
name2='Yaagavi'
print(type(name1))

dir="c://abc.txt"
dir2='c://abc.txt'
print(dir)
print(dir2)
dir="c:\abc\abc.txt"
dir2 ='c:\abc\abc.txt'
print(dir)
print(dir2)

dir="c:\\abc.txt"
dir2='c:\\abc.txt'
print(dir)
print(dir2)
dir="c:\\somedir\\some dir"
dir2='c:\\somedir\\some dir'
print(dir)
print(dir2)

dir="c:\nomedir\nomedir.txt"
dir2='c:\nsomedir\nomedir.txt'
print(dir)
print(dir2)

dir="c:\\nomedir\\nomedir.txt"
dir2='c:\\nsomedir\\nomedir.txt'
print(dir)
print(dir2)

#raw
dir=r"c:\\nomedir\\nomedir.txt"
dir2=r'c:\\nsomedir\\nomedir.txt'
print(dir)
print(dir2)

#format string
first_name ='Aishwarya'
last_name='Palanivel'
print(f"your name is : {first_name } and {last_name}")

first_name ='Aishwarya'
last_name='1996'
print(f"your name is : {first_name } {last_name}")

first_name ='Aishwarya'
last_name='1996'
age=27
isMarried='True'
print(f'your name is : {first_name } {last_name} your age is{age} and you are married{isMarried}')

#table of 5
num = 5
print(f'{num}*1={num}')
print(f'{num}*2={num}')
print(f'{num}*3={num}')

num=9
print("{}*{}+{}".format(2,3,4))