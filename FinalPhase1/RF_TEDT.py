def sequential_data(USC_ID='13572460'):
    wr_addr = ['000', '001', '010', '011', '100', '101', '110', '111']
    rd1_list = ['000', '001', '010', '011', '100', '101', '110', '111']
    rd2_list = ['000', '010', '100', '110', '001', '011', '101', '111']
    wr_data = ['143B', '985C', '211B', '4C36', 'E15C', '542B', '9F54', 'FF83']
    
    DATA_IN = []
    
    for i in USC_ID:
        # print(bin_to_list(rd1_list[int(i)]))
        # print(bin_to_comp(rd1_list[int(i)]))
        print(bin_to_list(rd2_list[int(i)]))
        print(bin_to_comp(rd2_list[int(i)]))
        # print(WR_addr_bin = bin_to_list(int(wr_addr[int(i)])))
        # print(WR_addr_COMP = bin_to_comp(int(wr_addr[int(i)])))
        # print(WR_DATA = bin_to_list(hex_to_binlist(wr_data[int(i)])))
        
        DATA_IN.append(bin_to_list(rd1_list[int(i)]) \
                        + bin_to_comp(rd1_list[int(i)])
                        + bin_to_list(rd2_list[int(i)])
                        + bin_to_comp(rd2_list[int(i)])
                        + bin_to_list(wr_addr[int(i)])
                        + bin_to_comp(wr_addr[int(i)])
                        + bin_to_list(hex_to_binlist(wr_data[int(i)])))

    return DATA_IN

def hex_to_binlist(dec_num, digit='16'):
        return [int(i) for i in ('{:0'+str(digit)+'b}').format(int(dec_num, 16))]

def bin_to_comp(addr_bin):
    return [1 ^ int(i) for i in addr_bin]

def bin_to_list(addr_bin):
    return [int(i) for i in addr_bin]

def write_vec(USC_ID):
    fout = open('./RF_TEST.vec', 'w', encoding='utf-8')
    #print header
    print('radix', end=' ', file=fout)
    for i in range(35):
        print('1', end=' ', file=fout)
    print('\n', end='', file=fout)

    print('io', end=' ', file=fout)
    for i in range(35):
        print('i', end=' ', file=fout)
    print('\n', end='', file=fout)

    print('vname', 'RD1<[2:0]>', '~RD1<[2:0]>', 'RD2<[2:0]>', '~RD2<[2:0]>',
          'WR_REG<[2:0]>', '~WR_REG<[2:0]>', 'WR_DATA<[15:0]>', 'WR_EN', file=fout)

    print('slope', '0.01', file=fout)
    print('vih', '1.8', file=fout)
    print('vil', '0', file=fout)
    print('tunit', '1ns', file=fout)
    print('\n', end='', file=fout)

    data_print(USC_ID, fout)

    fout.close()


def data_print(USC_ID, outputfile):
    data = sequential_data()
    datax2 = data + data

    for num, data_p in enumerate(datax2):  # write data to sram
        print(num, end=' ', file=outputfile)
        for bit in data_p:
            print(bit, end=' ', file=outputfile)
        
        print('1',file = outputfile)


if __name__ == '__main__':
    # USC_ID = input('Please input your USC_ID: ')
    write_vec('13572460')
