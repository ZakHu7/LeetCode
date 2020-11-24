def nextNumber(n):
  a = n
  i = 0
  big, small = -1, -1

  while a > 1:
    if(a ^ int('01',2)) & int('11',2) == int('11',2):
      big = i
    elif (a ^ int('10',2)) & int('11',2) == int('11',2):
      small = i
    
    if big > -1 and small > -1:
      break
    a //= 2
    i += 1
  
  bigNum = setBit(clearBit(n,big+1),big)
  smallNum = setBit(clearBit(n,small),small+1)
  
  print("big: {}".format(bigNum))
  print("small: {}".format(smallNum))

  print(bin(n), bin(bigNum), bin(smallNum))
  

def clearBit(n, i):
  return n & ~(1<<i)

def setBit(n, i):
  return n | (1<<i)


nextNumber(20)
a = 10
a //= 2

print((a ^ int('10',2)) & int('11',2) == int('11',2))

    