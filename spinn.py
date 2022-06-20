class Last_spinPlayed:
   'Common base class for all results'
   victory = 0
   loser = 0
   matrix = []
   def __init__(self, victory, loser, matrix):
      self.victory = victory
      self.loser = loser
      self.matrix = matrix

class Spin:
   'Common base class for count quantity old played'
   black = 0
   red = 0
   white = 0
   def __init__(self, black, red, white):
      self.black = black
      self.red = red
      self.white = white

class Bool_spinned:
   'Common base class for old spinneds'
   number = 0
   hour = ''
   color = ''
   def __init__(self, number, hour, color):
      self.number = number
      self.hour = hour
      self.color = color
