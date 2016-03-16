def puddle(walls):
    maxL = maxR = left = volume = 0
    right = len(walls)-1
    while left < right:
        # Adjust max values
        maxL = max(walls[left], maxL)
        maxR = max(walls[right], maxR)
        # Calculate volume
        if maxL < maxR:
            volume += maxL - walls[left]
            left += 1
        else:
            volume += maxR - walls[right]
            right -= 1
    return volume

print puddle([2,5,1,2,3,4,7,7,6])

# Test Cases
assert puddle([]) == 0
assert puddle([5]) == 0
assert puddle([5, 5]) == 0
assert puddle([5, 0, 5]) == 5
assert puddle([2, 5, 1, 2, 3, 4, 7, 7, 6, 8]) == 11
assert puddle([2, 5, 1, 2, 3, 4, 7, 7, 6])  == 10
assert puddle([6, 7, 7, 4, 3, 2, 1, 5, 2])  == 10
assert puddle([2,5,1,2,3,4,7,7,6,3,5]) == 12
assert puddle([2, 5, 1, 3, 1, 2, 1, 7, 7, 6])  == 17
assert puddle([2, 7, 2, 7, 4, 7, 1, 7, 3, 7])  == 18
assert puddle([2, 5, 1, 2, 3, 4, 7, 7, 6, 2, 7, 1, 2, 3, 4, 5, 5, 4])  == 26
assert puddle([9,6,2,7,10,2,8,2,9,10]) == 31
