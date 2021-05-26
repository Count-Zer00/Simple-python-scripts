ask = input("would you like to calulate Rectangle, cicle or square?: ")

def rect(l,b):
    return l*b

def circ(r):  
  area = round(22/7 * r**2)
  return area

def sq(s):
  area = s**2
  return area

while True:
  if ask == "Rectangle" or "rectangle":
    l = int(input("Length:"))
    b = int(input("bredth:"))
    print("area of rectangle =", rect(l, b))
    
  elif ask == "Circle" or "circle":
    r = int(input("radius: "))
    print("area of circle =", circ())
    
  elif ask == "Square" or "square":
    s = int(input('side:')) 
    print("area of Square =", sq())

  else:
    print('invalid')

  b = input('do you want to continue?')
  if b != 'n':
    continue
  else:
    break

