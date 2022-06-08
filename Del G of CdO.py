#............ import of libraries………….
import matplotlib.pyplot as plt
import numpy as np
#............ defining constants from literature…………
del_G0= -228.4464 # in KJ/mol
R= 0.00831447 # in KJ/K mol
T= 423 # (actual reaction temperature in K)
#............ defining a range of Q…………
Q= np.linspace(0.1,60,10000000)
# …….defining a function which is gibbs equation…………
del_G=del_G0+R*T*2.303*np.log(Q)
# ……….Q for CdO reaction conditions………
#Q =([𝑪𝑯𝟑𝑪𝑶𝑶𝑲]**𝟐)/[𝑪𝒅(𝑪𝑯𝟑𝑪𝑶𝑶)𝟐.𝟐𝑯𝟐𝑶][𝑲𝑶𝑯]**𝟐
#[𝑪𝑯𝟑𝑪𝑶𝑶𝑲]= C_1
#[𝑪𝒅(𝑪𝑯𝟑𝑪𝑶𝑶)𝟐.𝟐𝑯𝟐𝑶]= C_2
#[𝑲𝑶𝑯]= C_3
# ……..for stellated octahedron c_1=0.04, C_2=0.02, C_3=0.04
Q_St_OC =(0.04**2) / (0.02 * 0.04**2)
print('Reaction quotient for stellated octahedron is:',Q_St_OC)
# …….for octahedron C_1=0.14, C_2=0.07, C_3=0.14
Q_OC =(0.14**2) / (0.07 * 0.14**2)
print('Reaction quotient for octahedron is:',Q_OC)
# ……...for truncated octahedron C_1=0.18, C_2=0.09 C_3=0.18
Q_TOC =(0.18**2) / (0.09 * 0.18**2)
print('Reaction quotient for truncated octahedron is:',Q_TOC)
# ………for CdOH2 hexagonal plates C_1=0.24, C_2=0.12, C_3=0.24
Q_HP =(0.24**2) / (0.12 * 0.24**2)
print('Reaction quotient for cadmium hydroxide hexagonal plates is:',Q_HP)
# …….conditional Q values that is Q_C
Q_C= Q_St_OC,Q_OC,Q_TOC,Q_HP
# ……….conditional del_G that is del_G_C
del_G_C =del_G0+R*T*2.303*np.log(Q_C)
print('Gibbs free energy for stellated octahedron, octahedron,\n'
      'truncated octahedron and cadmium hydroxide plates are respectivly:\n', del_G_C)
#........plot of functions
plt.figure(1)
plot_1= plt.plot(Q,del_G,color='red')
plot_2= plt.scatter(Q_C,del_G_C,color='black')
plt.xlabel('Reaction Quotient (M**-1)',fontsize=12,weight='bold')
plt.ylabel('\u0394G (KJ/mol)',fontsize=12,weight='bold')
plt.xticks(fontsize=8,weight='bold')
plt.yticks(fontsize=8,weight='bold')
plt.show()