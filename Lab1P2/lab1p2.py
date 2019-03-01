'''
radix vec_size_1, vec_size2....
io i i    varibales are input
vname A[3:0] it specifies the name of variables in the corresponding schematic or layout. 
slope 0.01 time for change
vih 1.8 usually vdd
tunit: ns the time unit for slope and following input values. 
'''


def vec_printer(truth_table):

    fout = open('./full_adder_1_bit.vec', 'w', encoding = 'utf-8')
    #print header
    print('radix', '1 1 1 1 1', file = fout)
    print('io','i i i o o',file = fout)
    print('vname', 'A B C Cout S', file =fout)
    print('slope', '0.01', file = fout)
    print('vih', '1.8', file = fout)
    print('vil', '0',file = fout)
    print('tunit', 'ns', file = fout)
    print('\n', end = '', file=fout)
    
    for num,each in enumerate(truth_table):
        print(num,end = ' ',file = fout)
        for val in each:
            print(val,end = ' ',file = fout)
        print('\n',end = '',file=fout)

def dec_to_binlist(dec_num):
    binlist = []
    while dec_num>0:
        binlist.append(dec_num%2)
        dec_num= dec_num // 2
    
    binlist.reverse()
    print(binlist)

def dec_to_binlist2(dec_num, digit):
    return [int(i) for i in ('{:0'+str(digit)+'b}').format(dec_num)]


def truth_table_gen(x,var_num, truth_list,array):
    if x == var_num:
        for i in range(0, var_num):
            array.append(truth_list[i])
        return truth_list

    else:
        truth_list[x] = 0
        truth_table_gen(x+1, var_num, truth_list, array)
        truth_list[x] = 1
        truth_table_gen(x+1, var_num, truth_list, array)

def generate_file(var_num,array):
    truth_list = []
    for i in range(0,len(array),var_num):
        truth_list.append(array[i:i + var_num])

    for each in truth_list:
        # write output here
        each.append((each[0]&each[1])|(each[1]&each[2])|(each[0]&each[2]))
        each.append(each[0]^each[1]^each[2])
    
    return truth_list

if __name__ == '__main__':
    char_list = ['A', 'B', 'C']
    array = []
    truth_table_gen(0, len(char_list), char_list, array)
    truth_table = generate_file(len(char_list),array)
    vec_printer(truth_table)
    dec_to_binlist(5)
    dec_to_binlist2(10,10)