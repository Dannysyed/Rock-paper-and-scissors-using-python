import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
rcp = [rock, paper, scissors]
leng = len(rcp)-1
# print(leng)
result = random.randint(0, leng)
comp = rcp[result]
# print(comp)
user = int(input(
    'enter rock paper scissors! 0 for rock 1 for papaer 2 for scissors'))
if user == 0:
    print(rock)
    if result == 1:
        print(comp)
        print('comp wins')
    if result == 2:
        print(comp)
        print('user wins')
    if result == 0:
        print(comp)
        print('draw')
elif user == 1:
    print(paper)
    if result == 2:
        print(comp)
        print('comp wins')
    if result == 1:
        print(comp)
        print('draw')
    if result == 0:
        print(comp)
        print('user wins')
elif user == 2:
    print(scissors)
    if result == 0:
        print(comp)
        print('user wins')
    if result == 1:
        print(comp)
        print('user wins')
    if result == 2:
        print(comp)
        print('draw')
