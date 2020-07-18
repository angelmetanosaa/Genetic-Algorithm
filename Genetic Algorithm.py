from random import randint

gen = 6
kromosom = 6
individu = []
def populasi ():
	tampung = []
	for i in range(kromosom) :
			y = randint(0,1)
			tampung.append(y)
	individu.append(tampung)
	return individu

prob = 0
a = 0.000000000000000000000000000000000000000000000000000001
kromosomlist = []
fitlist = []
problist = []
best = []
for i in range(kromosom):
	populasi()
biner = populasi()
print("Populasi = ", biner)

for i in range (kromosom):
	print("\nKromosom Urutan ke - ", i+1, "=", biner[i])
	x1 = -3 + ((6/0.9375)*((biner[i][0]*0.5)+(biner[i][1]*0.25)+(biner[i][2]*0.125)))
	x2 = -2 + ((4/0.9375)*((biner[i][3]*0.5)+(biner[i][4]*0.25)+(biner[i][5]*0.125)))
	x = (((4-(2*(x1*x1))+((x1*x1*x1*x1)/3))*(x1*x1))+(x1*x2)+(-4+(4*(x2*x2)))*(x2*x2));
	f = (1/(x+a))
	print("Phenotype X1 Urutan ke - ", i+1, "=", x1)
	print("Phenotype X2 Urutan ke - ", i+1, "=", x2)
	print("Fitness Urutan ke - ", i+1, "=", f)
	kromosomlist.append(biner)
	
	prob = prob+f
	fitlist.append(f)

for i in range (len(kromosomlist)) :
	peluang = fitlist[i]/prob
	problist.append(peluang)
print("\nTotal Probabilitas = ", prob*100, "%")
print("\nProbabibilitas/Kromosom = ", problist)

#mencari orang tua dari fitness terbaik
posisiparent1 = 0
posisiparent2 = 0
binerparent1 = []
binerparent2 = []

#mencari nilai dan posisi parent1
parent1 =  max(problist)
for i in range (len(problist)) :
	if problist[i] == parent1 :
		posisiparent1 = i+1
		binerparent1 = biner[posisiparent1-1]
	if kromosomlist [i] == binerparent1:
		binerparent1 = kromosomlist[i]
		
#mencari nilai dan posisi parent2
problist.remove(parent1)
parent2 = max(problist)
for i in range (len(problist)) :
	if problist[i] == parent2 :
		posisiparent2 = i+1
		binerparent2 = biner[posisiparent2-1]
	if kromosomlist [i] == binerparent2 :
		binerparent2 = kromosomlist[i]

print ("\nValue Parent 1 = ", parent1)
print ("Posisi Parent 1 ada pada list ke - ", posisiparent1)
print ("Biner Parent 1 = ", binerparent1)
print ("\nValue Parent 2 = ", parent2)
print ("Posisi Parent 2 ada pada list ke - ", posisiparent2)
print ("Biner Parent 2 = ", binerparent2)

#mencari anak dengan crossover
#displit kemudian ditukar

a = (binerparent1[:3])
b = (binerparent1[3:])
c = (binerparent2[:3])
d = (binerparent2[3:])

child1 = a + d
child2 = c + b
print("\nChild 1 = ", child1)
print("Child 2 = ", child2)

#mencari mutasi
probmutasi = 1/6
for i in range (gen) :
	import random
	z = random.random()
	if (z>=0) and (z<=probmutasi):
		if child1[i] == 0 :
			child1[i] = 1;
		else :
			child1[i] = 1;

for i in range (gen) :
	import random
	z = random.random()
	if (z>=0) and (z<=probmutasi):
		if child2[i] == 0 :
			child2[i] = 1;
		else :
			child2[i] = 1;

print("\nMutasi yang terjadi pada Child 1 = ", child1)
print("Mutasi yang terjadi pada Child 2 = ", child2)

#regenerasi

def generasi () :
	for i in range (1,4):
		newgen = biner + [child1] + [child2];
		#print("\nGenerasi Baru = ", newgen)
		genbaru1 =  min(newgen)
		q = newgen.remove(genbaru1)
		genbaru2 = min(newgen)
		p = newgen.remove(genbaru2)
	print("\nGenerasi Terbaik = ", newgen)
generasi()

print("======================================================================== S E L E S A I =================================================================================")




