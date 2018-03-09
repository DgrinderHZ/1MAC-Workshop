"""
ATM manager!
Money papers available:
100, 50, 10, 5, and the rest of client's request

1) Inputs:
request : the money needed by the client
2) Output:
for a request = 277 return
give 100
give 100
give 50
give 10
give 10
give 5
give 2

"""

allowed_papers = [100, 50, 10, 5]
money_in_bank = 500

def GetRequest():
    """ Asks the client to input the request """
    request = int(input("Put the requested amount of money!\n"))
    while request <= 0 or request >= money_in_bank:
        if request <= 0:
            print ("Try more than that amount!")
            request = int(input("Put the requested amount of money!\n"))
        elif request > money_in_bank:
            print ("Try less than that amount!")
            request = int(input("Put the requested amount of money!\n"))
    return request


def Give(request):
    for paper in allowed_papers:
        while request > paper:
                print ("give "+ str(paper))
                request -= paper
    print ("give " + str(request))

request = GetRequest()
Give(request)

