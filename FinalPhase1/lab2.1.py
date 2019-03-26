def sequential_data(USC_ID = '1385000226'):
    addr_list = ['01011','01010','10110','01010','10011','11111','10100','10011','10001','11011']
    addr_data = ['143B','985C','211B','4C36','E15C','542B','9F54','FF83','18D7','1A2B']

    DATA_IN = []
    for i in USC_ID:
        DATA_IN.append(bin_to_list(addr_list[int(i)])+bin_to_comp(addr_list[int(i)])+dec_to_binlist(addr_data[int(i)]))
    
    return DATA_IN
def dec_to_binlist(dec_num, digit = '16'):
        return [int(i) for i in ('{:0'+str(digit)+'b}').format(int(dec_num,16))]

def bin_to_comp(addr_bin):
    return [1^int(i) for i in addr_bin]

def bin_to_list(addr_bin):
    return [int(i) for i in addr_bin]


def write_vec(USC_ID):
    fout = open('./sram_sequential123.vec', 'w', encoding='utf-8')
    #print header
    print('radix', end = ' ',file = fout)
    for i in range(29):
        print('1',end = ' ', file=fout)
    print('\n', end = '',file = fout)

    print('io', end=' ', file=fout)
    for i in range(29):
        print('i', end=' ', file=fout)
    print('\n', end='', file=fout)

    print('vname', 'A<[4:0]>', '~A<[4:0]>', 'DATAIN<[15:0]>', 'PRE_EN', 'RE_EN', 'WR_EN',file = fout)

    print('slope', '0.01', file=fout)  
    print('vih', '1.8', file=fout)  
    print('vil', '0', file=fout)   
    print('tunit', '1ns', file=fout)  
    print('\n', end='', file=fout)
    
    data_print(USC_ID, fout)

    fout.close()


def data_print(USC_ID,outputfile):
    data = sequential_data()
    PRE_EN = 0
    RE_EN = 0
    WR_EN = 0
    for num,data_p in enumerate(data):#write data to sram
        print(num*2,end= ' ',file = outputfile)
        for bit in data_p:
            print(bit, end = ' ',file = outputfile)
        print(PRE_EN, end= ' ',file = outputfile)#precharge enable
        print(RE_EN, end=' ', file=outputfile)
        print(WR_EN, file = outputfile)
        PRE_EN = PRE_EN ^ 1
        WR_EN = WR_EN^1
        print(2*num+1, end=' ', file=outputfile)
        for bit in data_p:
            print(bit, end = ' ',file = outputfile)
        print(PRE_EN, end= ' ',file = outputfile)#precharge enable
        print(RE_EN, end=' ', file=outputfile)
        print(WR_EN, file=outputfile)
        PRE_EN = PRE_EN ^ 1
        WR_EN = WR_EN ^ 1
    
    WR_EN = 0
    for num, data_p in enumerate(data, start = data.__len__()):
        print(2*num, end=' ', file=outputfile)
        for bit in data_p:
            print(bit, end = ' ',file = outputfile)
        print(PRE_EN, end= ' ',file = outputfile)#precharge enable
        print(RE_EN, end=' ', file=outputfile)
        print(WR_EN, file = outputfile)
        PRE_EN = PRE_EN ^ 1
        RE_EN = RE_EN ^ 1
        print(2*num+1, end=' ', file=outputfile)
        for bit in data_p:
            print(bit, end = ' ',file = outputfile)
        print(PRE_EN, end= ' ',file = outputfile)#precharge enable
        print(RE_EN, end=' ', file=outputfile)
        print(WR_EN, file=outputfile)
        PRE_EN = PRE_EN ^ 1
        RE_EN = RE_EN ^ 1

if __name__ == '__main__':
    USC_ID = input('Please input your USC_ID: ')
    write_vec(USC_ID)

