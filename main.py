import random

bal = 1000 # $
day = 0

liCryptoPrices = [bitcoin, ethirium, litecoin] = [99000.0, 4900.0, 800.0] # $

liStabilisation = [bitcoinStabilisation, ethiriumStabilisation, litecoinStabilisation] = [0.008, 0.006, 0.0]

liCrypto = ["bitcoin", "ethirium", "litecoin"]
liCryptoBal = [bitcoinBal, ethiriumBal, litecoinBal] = [0.2323, 1.1, 0]

# меняется цена крипті каждую секунду
def changeTrafic(liStabilisation, liCryptoPrices):
    RandNum = random.uniform(-4 ,4)
    #print(99000 + (99000 / 100 * (RandNum + liStabilisation[0])))
    for i in range(len(liCryptoPrices)):
        liCryptoPrices[i] = liCryptoPrices[i] + (liCryptoPrices[i] / 100 * (RandNum + liStabilisation[i]))
        #liStabilisation[i] = liStabilisation[i] - 0.01
    printCryptoPrice(liCrypto, liCryptoPrices)
    #print("bitcoin: ", bitcoin)
    return liCryptoPrices

# покупка крипты
def buyCrypto(crypto, bal, liCryptoBal, liCryptoPrices):
    print("\n- - - - BUY - - - -") 
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

# цены крипты
def printCryptoPrice(liCrypto, liCryptoPrices):
    print("\n- - - CRYPTO PRICE - - -")
    for li in range(len(liCryptoPrices)):
        if li < len(liCryptoPrices):
            print("\t" + liCrypto[li], "=", liCryptoPrices[li], "$")


# продать крипту
def sellCrypto(bal, crypto, liCryptoBal, liCryptoPrices):
    print("\n- - - - SELL - - - -")

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
    print("\n- - - BALANCE - - -")    
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
    liCryptoPrices = changeTrafic(liStabilisation, liCryptoPrices)
    print("\tDay: ", day)


#bal = buyCrypto(liCrypto, bal, liCryptoBal, liCryptoPrices)

#bal = sellCrypto(bal, liCrypto, liCryptoBal, liCryptoPrices)

#printBalance()
#printCrypto(liCrypto, liCryptoBal, liCryptoPrices)

print("\n- Program end -")