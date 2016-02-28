# G.E. Ranieri
#
# Pingala algorithm for 2^n
# Based on Pingala's algorithm from Chandahsutra (pre-200 BC)
# And "The Power of Two...in Poetry?" by Amy Shell-Gellasch and J.B. Thoo


# check whether n is even or odd
# if n is even, returns 0
# if n is odd, returns 1
def checkParity(n):
    return n % 2

# subtract 1 from n
def subtractOne(n):
    return n-1

# halve n
def halve(n):
    return n/2

# make a sequence of 0's and 2's
def pingalaSequencer(n):
    pingalaSequence = []
    while(n):
        if(n==0):
            pingalaSequence.append(0)
            break
        elif(checkParity(n)==0):
            n = halve(n)
            pingalaSequence.append(2)
        else:
            n = subtractOne(n)
            pingalaSequence.append(0)
    pingalaSequence.reverse()
    return pingalaSequence

# use the sequence to solve 2^n
def solve2toNthPower(n):
    pingalaSequence = pingalaSequencer(n)
    solution = 1
    for entry in pingalaSequence:
        if(entry==0):
            print("multiplying %s by 2 " % solution, end="")
            solution = solution*2
            print("yielded %s" % solution)
        else:
            print("squaring %s " % solution, end="")
            solution = solution**2
            print("yielded %s" % solution)
    print("2^%s is %s" % (n, solution))
    return solution

def main():
    n = int(input("Please enter a number: "))
    solve2toNthPower(n)

main()
