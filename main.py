import sqlite3
import numpy as np

db = sqlite3.connect(".\db.db")
c = db.cursor()


c.execute("SELECT * FROM tbl_multi ORDER BY ID ASC LIMIT 5000")

db_data = c.fetchall() #History of bets..
c.close()

array_of_mutipliers = np.arange(1.00,5.00,0.01) # make bet array 1.01 -> 10x

biggest_bank = {}

# for bet in bets:

bank = 50000
bet_value = 1000

lostNr = 0

def simple_betting_algo1():
    db = sqlite3.connect(".\db.db")
    c = db.cursor()

    c.execute("SELECT * FROM tbl_multi ORDER BY ID ASC LIMIT 3")

    db_data = c.fetchall()  # History of bets..
    c.close()

    low_streak = 0

    for i in db_data:
        if float(i[1]) >= float(1.5):
            low_streak = low_streak + 1

    if low_streak >=3:

        return True
    else:
        return False



for multiplier in array_of_mutipliers: #För varje värde i array of multipliers.

    print(multiplier)

    for i in db_data: #För varje värde i db_data

        if simple_betting_algo1():
            bank = bank - bet_value
        else:
            bank = bank

        if float(i[1]) >= round(multiplier, 2):
            bank = bank + (bet_value * multiplier)
        else:
            if bank <= 0:
                break

    biggest_bank[round(bank, 1)]=round((multiplier),2) #Adds value of bank as index with bet as value


print(max(biggest_bank))

print(biggest_bank[max(biggest_bank)])
