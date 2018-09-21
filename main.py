import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

db = sqlite3.connect(".\db.db")
c = db.cursor()


c.execute("SELECT * FROM tbl_multi ORDER BY ID ASC LIMIT 500")

#History of bets..
data = c.fetchall()

c.close()


#make bet array 1.01 -> 10x

bets = np.arange(1.00,10.00,0.01)

print(bets)

#print(bets)


biggest_bank = {}


for bet in bets:

    bank = 10000
    bet_value = 10

    for i in data:
        if float(i[1]) >= round(bet,2):
            bank = bank + (bet_value * bet)
        else:
            bank = bank - bet_value
            if bank <= bet:
                break


    biggest_bank[round(bank, 1)]=round((bet),2)



x = []
y = []

for item in biggest_bank:
    y.append(item)
    x.append(biggest_bank[item])


num_bins = 5

plt.show()
print(biggest_bank)

print(max(biggest_bank))

print(biggest_bank[max(biggest_bank)])

