import spinn
import matr

def seq_matrix(matrix, values):
  posMatrixActualSpinned = 0
  maxElementsMatrix = ((len(matrix) * len(matrix[0])) + len(matrix[0]))
  limitedSpinnedsAnalys = int(len(values) / maxElementsMatrix)
  for x in range(limitedSpinnedsAnalys):
    vArmzNextResults = []
    matrix = matr.create_heardquartes(len(matrix), len(matrix[0]))
    for i in range(posMatrixActualSpinned, len(values)):
      if(matr.addValue_heardquartes(matrix, values[i].color) == 0):
        while(len(vArmzNextResults) < len(matrix[0])):
          vArmzNextResults.append(values[i].color)
          break
    nextPositionSumMatrix = maxElementsMatrix
    posMatrixActualSpinned += nextPositionSumMatrix   
    
    sumSpinnedsPerColumn = matr.sumColumns_heardquartes(matrix)
    for spinned in sumSpinnedsPerColumn:
      if(spinned.black > spinned.red):
        color = 'bla'
      elif(spinned.red > spinned.black):
        color = 'red'
      else:
        color = 'whi'

    resultsPlayed = spinn.Last_spinPlayed(0,0, matrix)
    countElement = 0  
    while(countElement < len(vArmzNextResults)):
      win = color == vArmzNextResults[countElement]
      if(win):
        resultsPlayed.victory +=  1
      else:
        resultsPlayed.loser +=  1
      countElement += 1
  print('Terminated checked! Next array:', values[posMatrixActualSpinned].color)
  resultsPlayed.matrix = matrix
  return resultsPlayed