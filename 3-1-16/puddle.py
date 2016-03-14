def puddle(walls):
    Lmax = Rmax = left = volume = 0
    right = len(walls)-1
    while left < right:
        # Adjust max values
        Lmax = max(walls[left], Lmax)
        Rmax = max(walls[right], Rmax)
        # Calculate volume
        if Lmax < Rmax:
            volume += Lmax - walls[left]
            left+=1
        else:
            volume += Rmax - walls[right]
            right-=1
    return volume

print puddle([2,5,1,2,3,4,7,7,6])
