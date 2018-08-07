# Max Ranieri
#
# Pingala algorithm for 2^n
# Based on Pingala's algorithm from Chandahsutra (pre-200 BC)
# And "The Power of Two...in Poetry?" by Amy Shell-Gellasch and J.B. Thoo


# check whether n is even or odd
def is_even(n):
    return n % 2 == 0

# subtract 1 from n
def subtract_one(n):
    return n-1

# halve n
def halve(n):
    return n/2

# Steps
def pingala_sequencer(n):
    pingala_sequence = []
    
    while(n>-1):
        if(n==0):
            print("Goose egg")
            break
        elif(is_even(n)):
            print("%d is even, so this step is SQUARE" %n)
            print("Now we halve %d to get..." % n)
            n = halve(n)
            pingala_sequence.append("square")
        else:
            print("%d is odd, so so this step is DOUBLE" %n)
            print("Now we subtract 1 from %d to get..." %n)
            n = subtract_one(n)
            pingala_sequence.append("double")
    print("Now we have our steps:")
    print(pingala_sequence)
    pingala_sequence.reverse()
    print("Which we reverse to get:")
    print(pingala_sequence)
    return pingala_sequence

def solve_2_to(n):
    pingala_sequence = pingala_sequencer(n)
    solution = 1
    print()
    print("Starting with a value of 1, let's follow the steps:")
    for entry in pingala_sequence:
        if(entry=="double"):
            print("multiplying %d by 2" % solution)
            solution = solution*2
            print("yielded %d" % solution)
        else:
            print("squaring %d" % solution)
            solution = solution**2
            print("yielded %d" % solution)
    print("2^%d is %d" % (n, solution))
    return solution

def main():
    n = int(input("Please enter a number: "))
    solve_2_to(n)

main()
