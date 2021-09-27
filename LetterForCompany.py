letter = (''' hello dear customer,
i am taimoor from microsoft. I am very to tell you that you have been selected.
Date : date ''')

name = input('enter name: ')
date = input('enter date: ')
# a = int(date)
letter = letter.replace('customer', name)
letter = letter.replace('date', date)

print(letter)