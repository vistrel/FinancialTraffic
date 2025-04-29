import random

bal = 1000 # $
day = 0

liCryptoPrices = [bitcoin, ethirium, litecoin] = [99000, 4900, 800] # $


bitStabilisation = 10
ethStabilisation = 5

# меняется цена крипті каждую секунду
def changeTrafic(bitcoin, ethirium, bitStabilisation, ethStabilisation):
    BitRandNum = random.randint(-2 ,2)
    EthRandNum = random.randint(-2 ,2)
    #print("rand num: ", randNum)
    #BitRandNum = BitRandNum * 42
    #EthRandNum = EthRandNum * 42
    #print("rand num * 42: ", randNum)

    bitcoin = (bitStabilisation + bitcoin + (bitcoin / 100 * BitRandNum))
    ethirium = (ethStabilisation + ethirium + (ethirium / 100 * EthRandNum))
    print("- - - - - - - - -")
    print("1) Bitcoin: ", bitcoin)
    print("2) Ethirium: ", ethirium)
    return bitcoin, ethirium

# покупка крипты
def buyCrypto(crypto, value, bal):
    print("- - - - - - - - - -") 
    if value.isdigit():
        value = int(value)
        if value > bal:
            print("Not enough money")
            return
    else:
        print("Error")
        return

    print("Choice crypto: ", crypto)
    if crypto == "bitcoin":
        print("buy bitcoin")

    elif crypto == "ethirium":
        print("buy ethirium")
    else:
        print("Error")
    return bal


# продать крипту
def sellCrypto():
    print("- - - - - - - - - -") 
    print("sell")

# логика прибыльной торговли
def tradeLogic():
    print("trade")
    

# балик
def printBalance():
    print("- - - - - - - - - -")    
    print("Balance: ", bal, "$")

# крипто балик
def printCrypto(liCrypto, liCryptoBal, liCryptoPrices):
    print("- - - - - - - - - -")
    for li in range(len(liCrypto)):
        if liCryptoBal[li] <= 0:
            continue
        if li < len(liCryptoBal):
            print("\tCrypto: ", liCrypto[li], "=", liCryptoBal[li], "колв.", 
                "Total: ", round(liCryptoBal[li] * liCryptoPrices[li], 2), "$")

for i in range(10):
    day += 1
    liCryptoPrices = changeTrafic(bitcoin, ethirium, bitStabilisation, ethStabilisation)
    print("Day: ", day)

liCrypto = ["bitcoin", "ethirium", "litecoin"]
liCryptoBal = [bitcoinBal, ethiriumBal, litecoinBal] = [0.2323, 1.1, 0]

#value = input("Type value: ")
value = "150"
bal = buyCrypto(liCrypto[0], value, bal)

#printBalance()
printCrypto(liCrypto, liCryptoBal, liCryptoPrices)

print("\n\t- Program end -")