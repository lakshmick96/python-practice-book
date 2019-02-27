#Write a function count_change to count the number of ways to change any given amount. Available coins are also passed as argument to the function.

def count_change(amount, change):
    if amount == 0:
        return 1
    elif change == []:
        return 0
    elif amount < 0:
        return 0
    else:
        return count_change(amount-change[0], change) + count_change(amount, change[1:])

    
