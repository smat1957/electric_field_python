import numpy as np
import matplotlib.pyplot as plt

def solv(CX, CY, IE, JE, CT, boundary):
    def cvol():
        return CX*(CT[j][i-1]+CT[j][i+1])+CY*(CT[j-1][i]+CT[j+1][i])
    for j in range(1,JE+1):
        for i in range(1,IE+1):
            CT[j][i] = cvol()
    boundary(IE,JE,CT)
    for j in reversed(range(1,JE+1)):
        for i in reversed(range(1,IE+1)):
            CT[j][i] = cvol()
    boundary(IE,JE,CT)
    for i in range(1,IE+1):
        for j in reversed(range(1,JE+1)):
            CT[j][i] = cvol()
    boundary(IE,JE,CT)
    for i in reversed(range(1,IE+1)):
        for j in range(1,JE+1):
            CT[j][i] = cvol()
    boundary(IE,JE,CT)

def fixedb3(IE,JE,CT,CTH,CTC):
    for i in range(0,IE+2):
        CT[1][i] = 0.5
    CT[6][2] = 1.0
    CT[6][6] = 0.0

def fixedb2(IE,JE,CT,CTH,CTC):
    for j in range(5):
        CT[j][3]=1.0
        CT[j][5]=0.0

def fixedb1(IE,JE,CT,CTH,CTC):
    CT[4][2] = 1.0
    CT[4][6] = 0.0

def fixedb0(IE,JE,CT,CTH,CTC):
    for i in range(0,IE+2):
        CT[0][i] = CTH
        CT[JE+1][i] = CTC
    for j in range(0,JE+1):
        CT[j][0] = CTC
        CT[j][IE+1] = CTC

def bound3(IE,JE,CT):
    for i in range(0,IE+2):
        CT[1][i] = 0.5
        CT[JE+1][i] = CT[JE][i]
    for j in range(0,JE+1):
        CT[j][0] = CT[j][1]
        CT[j][IE+1] = CT[j][IE]
    fixedb3(IE,JE,CT,CTH,CTC)

def bound2(IE,JE,CT):
    for i in range(0,IE+2):
        CT[0][i] = CT[1][i]
        CT[JE+1][i] = CT[JE][i]
    for j in range(0,JE+1):
        CT[j][0] = CT[j][1]
        CT[j][IE+1] = CT[j][IE]
    fixedb2(IE,JE,CT,CTH,CTC)

def bound1(IE,JE,CT):
    for i in range(0,IE+2):
        CT[0][i] = CT[1][i]
        CT[JE+1][i] = CT[JE][i]
    for j in range(0,JE+1):
        CT[j][0] = CT[j][1]
        CT[j][IE+1] = CT[j][IE]
    fixedb1(IE,JE,CT,CTH,CTC)

def bound0(IE,JE,CT):
    fixedb0(IE,JE,CT,CTH,CTC)

def init(IE,JE,CT,WK,fixedb):
    for j in range(0,JE+2):
        for i in range(0,IE+2):
            CT[j][i] = WK
    fixedb(IE,JE,CT,CTH,CTC)

def debug(IE,JE,CT):
    for j in range(0,JE+2):
        print( j,CT[j] )

CTH = 1.0
CTC = 0.0
AR = 1.0/1.0
IE = 7
JE = 7
LAST = 15
CT = np.array([[0.0]*(IE+2)]*(JE+2))

DX = 1.0/float(IE)
DY = 1.0/float(JE)
DX2 = DX * DX
DY2 = DY * DY * AR * AR
CX = 0.5 * DY2 / (DX2 + DY2)
CY = 0.5 * DX2 / (DX2 + DY2)
WK = 0.5 * (CTH + CTC)

model = 1 # 0 or 1 or 2 or 3
if model==1:
    bound = bound1
    fixedb = fixedb1
elif model==2:
    bound = bound2
    fixedb = fixedb2
elif model==3:
    bound = bound3
    fixedb = fixedb3
else:
    bound = bound0
    fixedb = fixedb0

init(IE,JE,CT,WK,fixedb)
# debug(IE,JE,CT)

iter = 0
while iter<LAST:
    solv(CX, CY, IE, JE, CT, bound)
    # debug(IE,JE,CT)
    iter = iter + 1

X,Y=np.meshgrid(np.linspace(0.0,1.0,IE+2),np.linspace(0.0,1.0,JE+2))
#cont = plt.pcolormesh(X, Y, CT, cmap = "Blues")
cont=plt.contour(X,Y,CT,levels=20,linestyles='dashed',linewidths=3)
#cont.clabel(fmt='%1.1f', fontsize=12)
#plt.colorbar(cont)
plt.title('Simulation (Model '+str(model)+')')
plt.xlim(1.0/(IE+2),1.0-1.0/(IE+2))
plt.ylim(1.0/(JE+2),1.0-1.0/(JE+2))
plt.grid()
plt.savefig('simu'+str(model)+'.png')
plt.show()

