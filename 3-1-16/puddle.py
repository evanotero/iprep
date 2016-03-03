def puddle(walls):
    leftmax = 0
    rightmax = 0
    lIndex = 0
    rIndex = len(walls)-1
    volume = 0
    while lIndex < rIndex:
        # Adjust max values
        if walls[lIndex] > leftmax:
            leftmax = walls[lIndex]
        if walls[rIndex] > rightmax:
            rightmax = walls[rIndex]
        # Calculate volume
        if leftmax < rightmax:
            volume += leftmax - walls[lIndex]
            lIndex+=1
        else:
            volume += rightmax - walls[rIndex]
            rIndex-=1
    return volume

print puddle([2,5,1,2,3,4,7,7,6])
