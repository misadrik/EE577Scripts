import matplotlib.pyplot as plt
def read_file():
    fin = open('./nandsg.log','r')

    data = []
    group_lables = []
    t = []
    A = []
    Z = []
    flag = False
    for each_line in fin.readlines():
        if each_line.split() == ['b','out']:
            flag = True

        if each_line.strip() == 'y':
            flag = False

        if flag == True:
            data.append(each_line.split())

    #print(data)
    group_lables = data[0]
    group_lables.insert(0,'t')

    for item in range(1, len(data)):

        t.append(normal_value(data[item][0].strip('.')))
        A.append(normal_value(data[item][1].strip('.')))
        Z.append(normal_value(data[item][2].strip('.')))

    plt.plot(t,A)
    plt.plot(t,Z)
    plt.show()


def normal_value(str_num):
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
    read_file()