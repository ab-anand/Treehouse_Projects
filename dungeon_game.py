import random
import os

# create a grid
# pick a random location for the player
# pick a random location for the monster
# pick a random location for the exit door
# draw the player
# take input for the movement
# move player, unless invalid move(past grid)
# check for win/loss
# redraw the grid

CELLS = [(0,0), (1,0), (2, 0), (3, 0), (4, 0),
         (0,1), (1,1), (2, 1), (3, 1), (4, 1),
         (0,2), (1,2), (2, 2), (3, 2), (4, 2),
         (0,3), (1,3), (2, 3), (3, 3), (4, 3),
         (0,4), (1,4), (2, 4), (3, 4), (4, 4)     
        ]

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
  return random.sample(CELLS, 3)

def move_player(player, move):
  x, y = player
  if move == "LEFT":
    x -= 1
  elif move == "RIGHT":
    x+=1
  elif move == "UP":
    y -=1
  elif move == "DOWN":
    y +=1
  return x, y
    
 
def get_moves(move):
  moves = ["LEFT", "RIGHT", "UP", "DOWN"]
  x, y = move
  if y == 0:
    moves.remove("UP")
  if y == 4:
    moves.remove("DOWN")
  if x == 0:
    moves.remove("LEFT")
  if x == 4:
    moves.remove("RIGHT")
  return moves

def draw_map(player):
  clear()
  print(' _'*5)
  tile = '|{}'
  
  for cell in CELLS:
    x, y = cell
    if x < 4:
      line_end = ""
      if cell == player:
        output = tile.format("X")
      else:
        output = tile.format("_")
    else:
      line_end = '\n'
      if cell == player:
        output = tile.format("X|")
      else:
        output = tile.format("_|")
    print(output, end = line_end)
        

def game_loop():
  clear()  
  monster, door, player = get_locations()
  playing = True
  
  while playing:
      draw_map(player)
      valid_moves = get_moves(player)
      print('You\'re in the room {}'.format(player)) # fill with the current position
      print('You can move {}'.format(", ".join(valid_moves))) # fill with the available moves
      print('Press QUIT to quit.')
      
      move = input('> ').upper()
      
      if move == 'QUIT':
        print('\n ** See you next time **\n')
        break
      if move in valid_moves:
        player = move_player(player, move)
        if player == monster:
          print('\n ** Oh no! The monster got you. **\n')
          playing = False
        elif player == door:
          print('\n ** You escaped! Congratulations **\n')
          playing = False
      else:
        input("\n ** Walls are hard! Don't run into them. ** \n")
  else:
    if input("Wanna play again? [Y/n] ").lower() != 'n':
      game_loop()
      
      # Good move? Change the position of the player
      # Bad move? Do nothing
      # On the door? They win!
      # On the monster? They lose
      # Otherwise, loop back around


print('Welcome to the Dungeon!')
input("Press Enter/return to start ")
clear()
game_loop()

  
