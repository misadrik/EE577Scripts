'''
radix vec_size_1, vec_size2....
io i i    varibales are input
vname A[3:0] it specifies the name of variables in the corresponding schematic or layout. 
slope 0.01 time for change
vih 1.8 usually vdd
tunit: ns the time unit for slope and following input values. 
'''


def vec_printer(truth_table):

    fout = open('./multiplier.vec', 'w', encoding = 'utf-8')
    #print header
    print('radix', '1 1 1 1 1 1 1 1 1 1 1 1', file = fout)
    print('io','i i i i i i i i i i i i',file = fout) 
    print('vname', 'A5 A4 A3 A2 A1 A0 B5 B4 B3 B2 B1 B0', file =fout)
    print('slope', '0.01', file = fout)
    print('vih', '1.8', file = fout)
    print('vil', '0',file = fout)
    print('tunit', '10ns', file = fout)
    print('\n', end = '', file=fout)
    
    for num,each in enumerate(truth_table):
        print(num,end = ' ',file = fout)
        for val in each:
            print(val,end = ' ',file = fout)
        print('\n',end = '',file=fout)

# def dec_to_binlist(dec_num):
#     binlist = []
#     while dec_num>0:
#         binlist.append(dec_num%2)
#         dec_num= dec_num // 2
    
#     binlist.reverse()
#     print(binlist)

def dec_to_binlist2(dec_num, digit):
    if dec_num<0:
        return [int(i) for i in format(2**digit+dec_num,'b')]
    else:
        return [int(i) for i in ('{:0'+str(digit)+'b}').format(dec_num)]

def truth_table_gen(A_end, B_end, A_digit, B_digit, A_start = 0, B_start = 0):
    truth_table = []
    golden_results = []
    for A in range(A_start,A_end):
        for B in range(B_start,B_end):
            truth_table.append(dec_to_binlist2(A,A_digit)+dec_to_binlist2(B,B_digit))
            golden_results.append([A]+[B]+[A*B]+dec_to_binlist2(A*B,12))
    return truth_table,golden_results

def golden_result_printer(golden_results):
    fout = open('./multiplier_golden_result.vec', 'w', encoding = 'utf-8')
    for num,each in enumerate(golden_results):
        print(num,end = ' ',file = fout)
        for val in each:
            print(val,end = ' ',file = fout)
        print('\n',end = '',file=fout)
    

if __name__ == '__main__':

    # char_list = ['A', 'B', 'C']
    # array = []
    # truth_table_gen(0, len(char_list), char_list, array)
    # truth_table = generate_file(len(char_list),array)
    truth_table,golden_results = truth_table_gen(32,32,6,6,-32,-32)
    vec_printer(truth_table)
    golden_result_printer(golden_results)
