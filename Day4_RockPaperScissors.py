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

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
options = [rock, paper, scissors]
cpuChoice = random.randint(0, 2)

if choice >= 3 or choice < 0:
  print('Invalid input. You Lose.')
else:
  print(f'\nYour choice:\n{options[choice]}')
  print(f'\nCPUs choice:\n{options[cpuChoice]}')

  if choice == 0 and cpuChoice == 2:
    print('You Win!')
  elif cpuChoice == 0 and choice == 2:
    print('You Lose')
  elif cpuChoice > choice:
    print('You Lose.')
  elif choice > cpuChoice:
    print('You Win!') 
  elif choice == cpuChoice:
    print('It\'s a Draw.')