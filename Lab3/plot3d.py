import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re
import numpy as np

fin_num_orig = [1,1,1,1,1,1,1,1,1,1,1]
cap_orig =  [1.0, 2.950509385, 8.705505633,25.68567607,75.78582833,223.6067977,689.7539554,1946.610237,5743.491775,16946.22639,50000.00000]
NUM_VAL = 55
def extract_data():
    fin = open('./dram_data.log','r')
    fout = open('./dram.txt','w')
    content = fin.read()
    RTL = re.findall(r'rtl=\s+(-?\d+.\d+\w)',content)
    IAVG = re.findall(r'avg_current=\s*(-?\d+.\d+\w)',content)
    PAVG = re.findall(r'avg_power=\s*(-?\d+.\d+\w)',content)
    # print(IAVG)
    # print(PAVG)
    fin_num = []
    cap_num = []

# normalize values and extend the list
    for num in range(NUM_VAL):
        fin_num.append(fin_num_orig[num%(NUM_VAL//5)]+num//(NUM_VAL//5))
        cap_num.append(cap_orig[num%(NUM_VAL//5)])
        RTL[num]    = normal_value(RTL[num])
        IAVG[num]   = normal_value(IAVG[num])
        PAVG[num]   = normal_value(PAVG[num])

# print dram.txt
    for num in range(NUM_VAL):
        print('NUM_FIN = ', fin_num[num], 'Cap_NUM = ', cap_num[num], file = fout)
        print('rtl = ', RTL[num], 'avg_current = ', IAVG[num], 'avg_power = ', PAVG[num],file = fout)
        print('',file = fout)
# calculate min max standard deviation and average
    arith_cal([RTL, IAVG, PAVG],['RTL','IAVG','PAVG'])
## plot
    fig = plt.figure(1)
    ax=Axes3D(fig)
    ax.set_xlabel('fin_num(s)') 
    ax.set_ylabel('cap_num(fF)') 
    ax.set_zlabel('RTL(ps)') 
    # ax.scatter(fin_num, cap_num, RTL)
    ax.plot_trisurf(fin_num,cap_num,RTL)
    plt.savefig('RTL.svg')   
    
    fig = plt.figure(2)
    ax=Axes3D(fig)
    ax.set_xlabel('fin_num(s)') 
    ax.set_ylabel('cap_num(fF)') 
    ax.set_zlabel('IAVG(A)') 
    ax.plot_trisurf(fin_num,cap_num,IAVG)
    plt.savefig('IAVG.svg')

    fig = plt.figure(3)
    ax=Axes3D(fig)
    ax.set_xlabel('fin_num(s)') 
    ax.set_ylabel('cap_num(fF)') 
    ax.set_zlabel('PAVG(W)') 
    # ax.scatter(fin_num, cap_num, RTL)
    ax.plot_trisurf(fin_num,cap_num,PAVG)
    plt.savefig('PAVG.svg')
    # plt.show()
    plt.show()
def arith_cal(data,prefix):
    fout = open('arith_statics.txt','w')
    for prefix,data in zip(prefix,data):
        data_mean = np.mean(data)
        data_max = max(data)
        data_min = min(data)
        data_std = np.std(data,ddof=1)
        print(prefix + '_max  = ', data_max, file = fout)
        print(prefix + '_min = ', data_min, file = fout)
        print(prefix + '_mean = ', data_mean, file = fout)
        print(prefix + '_std  = ', data_std, file = fout)
        print('', file  = fout)

def normal_value(str_num):
    if 'a' in str_num:
        return float(str_num.strip('a'))*10**(-18)
    if 'f' in str_num:
        return float(str_num.strip('f'))*10**(-15)
    if 'p' in str_num:
        return float(str_num.strip('p'))*10**(-12)
    if 'n' in str_num:
        return float(str_num.strip('n'))*10**(-9)
    if 'u' in str_num:
        return float(str_num.strip('u'))*10**(-6)
    if 'm' in str_num:
        return float(str_num.strip('m'))*10**(-3)
    # print(str_num)
    return float(str_num)

if __name__ == '__main__':
    extract_data()


