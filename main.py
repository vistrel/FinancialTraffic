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
    return bitcoin, ethirium, litecoin

# покупка крипты
def buyCrypto(crypto, bal, liCryptoBal, liCryptoPrices):
    print("- - - - BUY - - - -") 
    #cryptoNum = int(input("\t1)Bitcoin\n\t2)Ethirium\n\t3)Litecoin\nType crypto for buy: "))
    cryptoNum = 3

    if cryptoNum > len(crypto) or cryptoNum < 1:
        print("Error cryptoNum")
        return

    #value = input("Type value $: ")
    value = "429"

    if value.isdigit():
        value = int(value)
        if value > bal:
            print("Not enough money")
            return
    else:
        print("Error")
        return

    cryptoNewNum = cryptoNum - 1
    #print("Choice crypto: ", crypto[cryptoNewNum])
    print(f"Buy {crypto[cryptoNewNum]} for: ", value, "$")
    bal = bal - value
    liCryptoBal[cryptoNewNum] = liCryptoBal[cryptoNewNum] + (value / liCryptoPrices[cryptoNewNum])
    print("\t! You have: ", liCryptoBal[cryptoNewNum], f"{crypto[cryptoNewNum]}")
        
    return bal


# продать крипту
def sellCrypto(bal, crypto, liCryptoBal, liCryptoPrices):
    print("- - - - SELL - - - -")

    #cryptoNum = int(input("\t1)Bitcoin\n\t2)Ethirium\n\t3)Litecoin\nType crypto for sell: "))
    cryptoNum = 3

    if cryptoNum > len(crypto) or cryptoNum < 1:
        print("Error cryptoNum")
        return
    cryptoNewNum = cryptoNum - 1
    if liCryptoBal[cryptoNewNum] <= 0:
        print("You don't have this crypto")
        return
    print("You have: ", liCryptoBal[cryptoNewNum], f"{crypto[cryptoNewNum]}")
    
    #value = input("Type value crypto: ")
    value = "0.15"
    value = float(value)
    if value > 0:
        #value = int(value)
        if value > liCryptoBal[cryptoNewNum]:
            print("Not enough crypto")
            return
        liCryptoBal[cryptoNewNum] = liCryptoBal[cryptoNewNum] - value
        bal = bal + (value * liCryptoPrices[cryptoNewNum])
        print(f"Sell {crypto[cryptoNewNum]} for: ", round(value * liCryptoPrices[cryptoNewNum], 2), "$")
        print("\t! You have: ", liCryptoBal[cryptoNewNum], f"{crypto[cryptoNewNum]}")
    else:
        print("Type value > 0")
        return

    return bal


# логика прибыльной торговли
def tradeLogic():
    print("trade")
    

# балик
def printBalance():
    print("- - - - - - - - - -")    
    print("Balance: ", bal, "$")

# крипто балик
def printCrypto(liCrypto, liCryptoBal, liCryptoPrices):
    print("- - - BALANCE - - -")
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

bal = buyCrypto(liCrypto, bal, liCryptoBal, liCryptoPrices)

bal = sellCrypto(bal, liCrypto, liCryptoBal, liCryptoPrices)

#printBalance()
#printCrypto(liCrypto, liCryptoBal, liCryptoPrices)

print("\n- Program end -")