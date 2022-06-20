import requests
import matr
import spinn
from bs4 import BeautifulSoup

#Target URL
URL = "<LINK_WEB_FONT>"
r = requests.get(URL)

#Technology inspect
soup = BeautifulSoup(r.content, 'html5lib')

#Filter all spins played the day
all_spins_played = soup.find("div", {"class": "content-giros"}).findAll("div", {"class": "pdi"})

#Alloc heardquartes for statics spins (3x15)
quan_lines = 15
quan_columns = 3

#Base input
vectorInputData = []

#Show all spins played during the day ::-1 (last per recently)
for spin_played in all_spins_played[::-1]:
  spin = str(spin_played)
  posHour = (spin.find('-hora')) + 7
  posNumber = (spin.find('numero-span')) + 13
  posCol = (spin.find('assets/images/')) + 14

  #Alloc our data-font actual
  vectorInputData.append(
    spinn.Bool_spinned(
        spin[posNumber:posNumber+1],
        spin[posHour:posHour+5], 
        spin[posCol:posCol+3]
    ))

last_spinned= matr.seq_matrix(matr.create_heardquartes(quan_lines, quan_columns), vectorInputData)
print(last_spinned.victory, last_spinned.loser)
matr.show_heardquartes(last_spinned.matrix)
