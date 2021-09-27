_author_ = "taimoor"

print("what is your name?")

user_name = input()

print("hello, "+ user_name)

print("what is your age?")

user_age = input()

user_age = int(user_age)

if user_age > 18:
    print("fine")
else:
    print("tusi mera puttar bao raam mout maro ge!!!")

print("what is your father name?")

user_father = input()

print("oh!" + user_name + "bin" + user_father)

print("now i am going to ask you some question, are you ready!!!")

user_ans = input()

if user_ans == "yes":
  print("ok lets start")
else:
  print("go away!!!")
  exit()

print("Q#1: who is the prime minister of paksitan?")
print('imran khan/nawaz sharif')

user_ans1 = input("Ans: ")

if user_ans1 == "imran khan":
  print("correct")

else:
  print("wrong")
  print('bhola record')
  "break"

while user_ans1 == 'imran khan':
    continue


