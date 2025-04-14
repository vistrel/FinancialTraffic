import random

bal = 1000

bitcoin = 99000 # $
ethirium = 4900 # $

bitStabilisation = 3.2
ethStabilisation = 2.7

# меняется цена крипті каждую секунду
def changeTrafic(bitcoin, ethirium, bitStabilisation, ethStabilisation):
    BitRandNum = random.uniform(-10 + bitStabilisation,10)
    EthRandNum = random.randint(-10 + ethStabilisation,10)
    #print("rand num: ", randNum)
    BitRandNum = BitRandNum * 42
    EthRandNum = EthRandNum * 42
    #print("rand num * 42: ", randNum)

    bitcoin = (bitcoin + BitRandNum)
    ethirium = (ethirium + EthRandNum)
    print("- - - - - - - - -")
    print("1) Bitcoin: ", bitcoin)
    print("2) Ethirium: ", ethirium)
    return bitcoin, ethirium


# балик
def printBalance():
    print("Bal: ", bal)

for i in range(100):
    bitcoin, ethirium = changeTrafic(bitcoin, ethirium, bitStabilisation, ethStabilisation)

#printBalance()