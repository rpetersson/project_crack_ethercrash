import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

db = sqlite3.connect(".\db.db")
c = db.cursor()


c.execute("SELECT * FROM tbl_multi ORDER BY ID ASC LIMIT 5000")

data = c.fetchall() #History of bets..
c.close()

bets = np.arange(1.00,20.00,0.01) # make bet array 1.01 -> 10x

print(bets)

biggest_bank = {}

# for bet in bets:

bank = 10000
bet_value = 10

lostNr = 0

for bet in bets:

    for i in data:

        #if float(i[1]) != 0:
        bank = bank - bet_value

        if float(i[1]) >= round(bet, 2):

            bank = bank + (bet_value * bet)
        else:
            lostNr = lostNr + 1
            #print("Lost again! Bank = " + str(bank) + " lost times = " + str(lostNr))
            if bank <= 0:
                break

    biggest_bank[round(bank, 1)]=round((bet),2) #Adds value of bank as index with bet as value


print(max(biggest_bank))

print(biggest_bank[max(biggest_bank)])
