import random

bal = 1000.0 # $
day = 1

liCryptoPrices = [bitcoin, ethirium, litecoin] = [99000.0, 4900.0, 800.0] # $

liStabilisation = [bitcoinStabilisation, ethiriumStabilisation, litecoinStabilisation] = [0.008, 0.006, 0.0]

liCrypto = ["bitcoin", "ethirium", "litecoin"]
liCryptoBal = [bitcoinBal, ethiriumBal, litecoinBal] = [0.2323, 1.1, 0]

liCryptoPriceWeek = [5451, 2232, 3989]
#print("Crypto prices: ", liCryptoPriceWeek[1])

# меняется цена крипті каждую секунду
def changeTrafic(liStabilisation, liCryptoPrices, liCryptoPriceWeek):
    RandNum = random.uniform(-4 ,4)
    #print(99000 + (99000 / 100 * (RandNum + liStabilisation[0])))
    for i in range(len(liCryptoPrices)):
        liCryptoPrices[i] = liCryptoPrices[i] + (liCryptoPrices[i] / 100 * (RandNum + liStabilisation[i]))
        #liStabilisation[i] = liStabilisation[i] - 0.01
    printCryptoPrice(liCrypto, liCryptoPrices)
    #print("bitcoin: ", bitcoin)
    liCryptoPriceWeek.append(liCryptoPrices[0])
    if len(liCryptoPriceWeek) > 7:
        liCryptoPriceWeek.pop(0)
    print("Bitcoin prices week: ", liCryptoPriceWeek)
    return liCryptoPrices

# покупка крипты
def buyCrypto(crypto, bal, liCryptoBal, liCryptoPrices):
    print("\n- - - - BUY - - - -") 
    cryptoNum = int(input("\t1)Bitcoin\n\t2)Ethirium\n\t3)Litecoin\nType crypto for buy: "))
    #cryptoNum = 3

    if cryptoNum > len(crypto) or cryptoNum < 1:
        print("Error cryptoNum")
        return

    value = input("Type value $: ")
    #value = "429"

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

    cryptoNum = int(input("\t1)Bitcoin\n\t2)Ethirium\n\t3)Litecoin\nType crypto for sell: "))
    #cryptoNum = 3

    if cryptoNum > len(crypto) or cryptoNum < 1:
        print("Error cryptoNum")
        return
    cryptoNewNum = cryptoNum - 1
    if liCryptoBal[cryptoNewNum] <= 0:
        print("You don't have this crypto")
        return
    print("You have: ", liCryptoBal[cryptoNewNum], f"{crypto[cryptoNewNum]}")
    
    value = input("Type value crypto: ")
    #value = "0.15"
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
def tradeLogic(crypto, bal, liCryptoPriceWeek):
    print("\n- - - TRADE - - -")  
    stopLoss = 0.05  # 5% stop loss
    takeProfit = 0.1  # 10% take profit

    #value = input("Type value $: ")
    value = "300"
    
    if value.isdigit():
        value = int(value)
        if value > bal:
            print("Not enough money")
            return
    else:
        print("Error")
        return
    print("bal before buy: ", bal)
    #cryptoNum = int(input("\t1)Bitcoin\n\t2)Ethirium\n\t3)Litecoin\nType crypto for buy: "))
    cryptoNum = 1
    cryptoNewNum = cryptoNum - 1
    print(f"Buy {crypto[cryptoNewNum]} for: ", value, "$")
    bal = bal - value
    liCryptoBal[cryptoNewNum] = liCryptoBal[cryptoNewNum] + (value / liCryptoPrices[cryptoNewNum])
    print("Balance after buy: ", bal)

    print("Trade money is: ", value, "$")
    print("Trade crypto is: ", liCrypto[0])
    print("Stop Loss: ", stopLoss * 100, "%")
    print("Take Profit: ", takeProfit * 100, "%")
    # Здесь должна быть логика торговли
    if liCryptoPriceWeek[-1] > liCryptoPriceWeek[0] * (1 + takeProfit):
        print(liCryptoPriceWeek[-1], liCryptoPriceWeek[0], (1 + takeProfit))
        print("Take Profit triggered!")
        bal += value * (1 + takeProfit)
    elif liCryptoPriceWeek[-1] < liCryptoPriceWeek[0] * (1 - stopLoss):
        print(liCryptoPriceWeek[-1], liCryptoPriceWeek[0], (1 - stopLoss))
        print("Stop Loss triggered!")
        bal -= value * stopLoss
    else:
        print("No trade action taken.")
    return bal
     
    
    

# балик
def printBalance(bal):
    print("\n- - - BALANCE - - -")   
    print("Balance: ", round(bal, 2), "$")

# крипто балик
def printCrypto(liCrypto, liCryptoBal, liCryptoPrices):
    print("- - - BALANCE - - -")
    for li in range(len(liCrypto)):
        if liCryptoBal[li] <= 0:
            continue
        if li < len(liCryptoBal):
            print("\tCrypto: ", liCrypto[li], "=", liCryptoBal[li], "колв.", 
                "Total: ", round(liCryptoBal[li] * liCryptoPrices[li], 2), "$")

#for i in range(10):
#    day += 1
#    liCryptoPrices = changeTrafic(liStabilisation, liCryptoPrices)
#    print("\tDay: ", day)

# menu
while True:
    print("\n- - - - MENU - - - -")
    print("1) Buy crypto")
    print("2) Sell crypto")
    print("3) Trade logic")
    print("4) Print balance")
    print("5) Print crypto balance")
    print("0) Exit")
    print("Enter) Press Enter for next day")
    print("\nDay: ", day)

    choice = input("Type number: ")

    if choice == "1":
        bal = buyCrypto(liCrypto, bal, liCryptoBal, liCryptoPrices)
        continue
    elif choice == "2":
        bal = sellCrypto(bal, liCrypto, liCryptoBal, liCryptoPrices)
        continue
    elif choice == "3":
        bal = tradeLogic(liCrypto, bal, liCryptoPriceWeek)
        continue
    elif choice == "4":
        printBalance(bal)
        continue
    elif choice == "5":
        printCrypto(liCrypto, liCryptoBal, liCryptoPrices)
        continue
    elif choice == "":
        day += 1
        liCryptoPrices = changeTrafic(liStabilisation, liCryptoPrices, liCryptoPriceWeek)
        continue
    elif choice == "0":
        break
    else:
        print("Error choice")
        continue


#printCrypto(liCrypto, liCryptoBal, liCryptoPrices)

print("\n- Program end -")