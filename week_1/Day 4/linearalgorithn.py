import math
math.pi
N = "enter upper limit"
def volume():
    volume = math.pi*(r**2)*h
    return volume
print(volume(1,1))
def cone_volume(h,r):
    volume = (h/3)*math.pi*(r**2)
    return volume


print(cone_volume)
print("1/3 =")
area = pi*(r**2)
for r in range(1,N+1):
    print(area)
