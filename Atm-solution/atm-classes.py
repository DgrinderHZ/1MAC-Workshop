class ATM:

    def __init__(self, balance, bank_name):
        self.withdrawals_list = []
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        print ("Welcome to "+ self.bank_name)
        print ("The current balance is : " + str(self.balance))
        print ("==============================")

        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.withdrawals_list.append(request)
            while request > 0:

                if request >= 100:
                    request -= 100
                    self.balance -= 100
                    print("give 100")

                elif request >= 50:
                    request -= 50
                    self.balance -= 50
                    print("give 50")

                elif request >= 10:
                    request -= 10
                    self.balance -= 10
                    print("give 10")

                elif request >= 5:
                    request -= 5
                    self.balance -= 5
                    print("give 5")

                elif request < 5:
                    print("give " + str(request))
                    self.balance -= request
                    request = 0
        print ("==============================")
    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print(withdrawal)


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

print ("=" * 10 + "withdrawals" + "=" * 10)
atm1.show_withdrawals()

atm1.withdraw(277)
atm1.withdraw(800)

print ("=" * 10 + "withdrawals" + "=" * 10)
atm1.show_withdrawals()
print ("=" * 31)

atm2.withdraw(100)
atm2.withdraw(2000)

print ("=" * 10 + "withdrawals" + "=" * 10)
atm2.show_withdrawals()
print ("=" * 31)