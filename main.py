sk = int(input("Ievadi veselus skaitlus: "))
a = 1
para = 0
nepara = 0
poz = 0
neg = 0
div = 0
tris = 0
b = int (input("Ierakstiet 1, ja vēlaties salīdzināt nepāra un pāra, ierakstiet 2, ja vēlaties salīdzināt pozitīvo un negatīvo, ierakstiet 3, ja vēlaties salīdzināt divciparus un trīsciparus: "))
if b ==1:
  while a<=sk:
    sk1 = int(input("Ievadi skaitlu: "))
    if sk1%2==0:
      para=para+1
    else:
      nepara=nepara+1
    a=a+1
  if para>nepara:
    print("Paraskaitli vairak")
  elif para==nepara:
    print("Draw!")
  else:
    print("Neparaskaitli vairak")
elif b ==2:
  while a<=sk:
    sk1 = int(input("Ievadi skaitlu: "))
    if sk1>0:
      poz=poz+1
    else:
      neg=neg+1
    a=a+1
  if poz>neg:
    print("Pozitivi vairak")
  elif poz==neg:
    print("Draw!")
  else:
    print("Negativi vairak")
else:
  while a<=sk:
    sk1 = int(input("Ievadi skaitlu: "))
    if sk1>=10 and sk1<=99:
      div=div+1
    elif sk1>=100 and sk1<=999:
      tris=tris+1
    a=a+1
  if div>tris:
    print("Divcipari vairak")
  elif div==tris:
    print("Draw!")
  else:
    print("Triscipari vairak")