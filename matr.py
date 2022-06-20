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