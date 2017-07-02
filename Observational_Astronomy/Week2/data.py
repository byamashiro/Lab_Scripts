import numpy as np
import matplotlib.pyplot as plt

afont = {'fontname':'Comic Sans MS'}

#anna
anna_h = np.array([161.0,165.0,163.0,174.0,171.0,169.0])
anna_h_d = np.array([5.0,5.0,5.0,5.0,5.0,5.0])

anna_w = np.array([165.0,177.0,157.0,173.0,175.0,183.0])
anna_w_d = np.array([5.0,5.0,5.0,5.0,5.0,5.0])

#randy
randy_h = np.array([176.0,172.5,172.1,161.3,174.0,162.5,171.2,161.5])
randy_h_d = np.array([0.1,0.2,0.2,0.1,0.2,0.1,0.2,0.1])

randy_w = np.array([179.2,184.0,175.7,160.5,174.0,158.0,169.8,164.0])
randy_w_d = np.array([0.2,0.1,0.2,0.1,0.2,0.2,0.2,0.2])

#james
james_h = np.array([171.6,176.0,176.7,161.3])
james_h_d = np.array([0.2,0.2,0.2,0.2])

james_w = np.array([174.7,177.8,174.1,166.1])
james_w_d = np.array([3.5,3.5,3.5,3.3])

#bryan
bryan_h = np.array([161.0,172.0,163.0])
bryan_h_d = np.array([1.0,1.0,1.0])

bryan_w = np.array([167.0,185.0,161.0])
bryan_w_d = np.array([1.0,1.0,1.0])

#jacob
jacob_h = np.array([171.9,163.7,176.3,162.4,177.8,161.2])
jacob_h_d = np.array([0.1,0.1,0.1,0.1,0.1,0.1])

jacob_w = np.array([183.6,160.3,178.6,161.3,172.9,165.2])
jacob_w_d = np.array([0.1,0.1,0.1,0.1,0.1,0.1])

#gabster
gabster_h = np.array([175.5,173.1,163.5])
gabster_h_d = np.array([0.1,0.1,0.1])

gabster_w = np.array([171.6,183.9,162.1])
gabster_w_d = np.array([0.2,0.2,0.2])




#plot
fig = plt.figure()
plt.errorbar(anna_h, anna_w, xerr=anna_h_d, yerr=anna_w_d, fmt='rs', color='Red', ecolor='Red')
plt.errorbar(randy_h, randy_w, xerr=randy_h_d, yerr=randy_w_d, fmt='rs', color='Orange', ecolor='Orange')
plt.errorbar(james_h, james_w, xerr=james_h_d, yerr=james_w_d, fmt='rs', color='Yellow', ecolor='Yellow')
plt.errorbar(bryan_h, bryan_w, xerr=bryan_h_d, yerr=bryan_w_d, fmt='rs', color='Blue', ecolor='Blue')
plt.errorbar(jacob_h, jacob_w, xerr=jacob_h_d, yerr=jacob_w_d, fmt='rs', color='Purple', ecolor='Purple')
plt.errorbar(gabster_h, gabster_w, xerr=gabster_h_d, yerr=gabster_w_d, fmt='rs', color='Green', ecolor='Green')



plt.xlabel('Height (m)', fontname="Arial", fontsize=14)
plt.ylabel('Arm Length (m)', fontname="Arial", fontsize=14)
plt.grid(b=True, which='both', color='black',linestyle='-.')


fig.savefig('hvw.eps')
plt.show()




