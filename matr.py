import spinn

#Function for create a new heardquartes
def create_heardquartes(lines, columns):
    heardquartes = []
    for _ in range(lines):
        heardquartes.append( [" "] * columns )
    return heardquartes

#Function for show heardquartes legible
def show_heardquartes(heardquartes):     
    for l in range(0, len(heardquartes)):
        for c in range(0, len(heardquartes[0])):
            print(f'[{heardquartes[l][c]}]', end='')
        print()
    print("\n")

#Function add spins over matrix
def addValue_heardquartes(heardquartes, value):
    for l in range(0, len(heardquartes)):
        for c in range(0, len(heardquartes[0])):
            if(heardquartes[l][c]== " "): 
                heardquartes[l][c] = value
                return 1
    return 0

def sumColumns_heardquartes(heardquartes):
    vectorAllocValues = []
    for l in range(0, len(heardquartes[0])):
        cBlack = 0
        cRed = 0
        cWhite = 0;
        for c in range(0, len(heardquartes)):
            if(heardquartes[c][l] == 'bla'): 
                cBlack += 1
            if(heardquartes[c][l] == 'red'): 
                cRed += 1   
            elif(heardquartes[c][l] == 'whi'):
                cWhite += 1
        vectorAllocValues.append(spinn.Spin(cBlack,cRed,cWhite))
    return vectorAllocValues

def seq_matrix(matrix, values):
  posMatrixActualSpinned = 0
  maxElementsMatrix = ((len(matrix) * len(matrix[0])) + len(matrix[0]))
  limitedSpinnedsAnalys = int(len(values) / maxElementsMatrix)
  for x in range(limitedSpinnedsAnalys):
    vArmzNextResults = []
    matrix = create_heardquartes(len(matrix), len(matrix[0]))
    for i in range(posMatrixActualSpinned, len(values)):
      if(addValue_heardquartes(matrix, values[i].color) == 0):
        while(len(vArmzNextResults) < len(matrix[0])):
          vArmzNextResults.append(values[i].color)
          break
    nextPositionSumMatrix = maxElementsMatrix
    posMatrixActualSpinned += nextPositionSumMatrix   
    
    sumSpinnedsPerColumn = sumColumns_heardquartes(matrix)
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