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
