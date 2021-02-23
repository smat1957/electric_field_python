import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# 電位分布の実験より、等電位面（線）の作図
vx, vy = np.linspace(0, 120, 7), np.arange(0, 130, 20, dtype=float)
X, Y = np.meshgrid(vx, vy)
Z1 = np.array([[3.52,3.48,3.32,3.12,2.76,2.54,2.43],
  [3.58,3.51,3.30,2.90,2.52,2.31,2.22],[3.78,3.85,3.47,2.97,2.36,1.92,1.97],
  [3.91,5.00,3.56,2.95,2.21,0.00,1.80],[3.77,3.85,3.47,2.96,2.45,1.96,2.00],
  [3.56,3.50,3.28,2.96,2.62,2.32,2.23],[3.44,3.33,3.20,2.99,2.75,2.54,2.44]])
Z2 = np.array([[4.47,4.65,4.14,2.90,1.60,0.87,1.08],
  [4.45,4.65,4.11,2.93,1.64,0.88,1.10],[4.39,4.63,4.14,2.89,1.65,0.96,1.21],
  [4.24,4.40,4.04,2.90,1.85,1.24,1.42],[3.99,3.96,3.56,2.83,2.15,1.77,1.66],
  [3.78,3.62,3.30,2.83,2.37,2.06,1.92],[3.57,3.44,3.16,2.85,2.46,2.18,2.01]])
Z3 = np.array([[0.76,0.52,0.31,0.065,-0.19,-0.41,-0.58],
  [0.88,0.61,0.36,0.0,-0.24,-0.52,-0.68],
  [1.1,0.87,0.53,0.081,-0.039,-0.013,-0.96],
  [1.66,1.46,0.93,0.17,-0.54,-1.06,-1.23],
  [2.24,2.31,1.35,1.49,-1.02,-2.06,-1.83],
  [2.72,5.00,1.84,1.61,-1.42,-5.0,-2.14],
  [2.3,2.35,1.46,0.3,-0.78,-1.62,-1.65]])
Z=Z1
cont = plt.contour(X,Y,Z,levels=20,linestyles='dashed',linewidths=3)
cont.clabel(fmt='%1.1f', fontsize=14)
plt.title('Potential Energy(1)', size=14)
plt.xlabel('X', fontsize=14)
plt.ylabel('Y', fontsize=14)
plt.grid()
plt.savefig('contr1.png')
plt.show()

# X, Y, Zをワイヤフレーム(あるいはサーフェス)で表示
ax = Axes3D( plt.figure() ) # Axes3D のオブジェクトを ax に取得
#ax.plot_wireframe(X, Y, Z)
ax.plot_surface(X, Y, Z, cmap='bone', antialiased=True)
#ax.plot_trisurf(X, Y, Z, cmap = "bwr")
ax.set_title('Potential Energy(1)', size=14)
ax.set_xlabel("x[mm]", size = 14)
ax.set_ylabel("y[mm]", size = 14)
ax.set_zlabel("z[V]", size = 14)
#ax.contour(X, Y, Z, colors = "black", offset = -3)
#ax.view_init(45, 45)  # 視点の設定（仰角＝水平0〜垂直90）（回転角＝0〜360）
plt.grid()
plt.savefig('contr2.png')
plt.show()

