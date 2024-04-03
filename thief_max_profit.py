# Imagine a scenario where a thief is moving through a neighborhood at night,
# targeting houses in a row to steal valuable items. Each house has a certain
# amount of money stashed, represented by an array arr, where each element
# of the array indicates the amount of money in each house. The thief, 
# however, has a constraint to avoid detection: they cannot steal from two
# adjacent houses because of connected security systems. If the thief 
# triggers an alarm at one house, the neighboring houses will also be 
# alerted. Given this scenario, the thief wants to maximize their total 
# haul for the night.

def max_profit(arr):
    profit=[]
    cur,prev,sprev=0,0,0
    for i in range(len(arr)):
        cur=sprev+arr[i]
        profit.append(cur)
        sprev=prev
        prev=cur
        # print(cur,prev,sprev)
    return max(profit[-1],profit[-2])

print(max_profit([2,7,9,6,1]))