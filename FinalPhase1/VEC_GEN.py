def print_vec(machine_code, fout):
    #print header
    print('radix', end=' ', file=fout)
    print('4444 4444 3 3 1 3 1 1 1 1 3 1 2 1', file=fout)

    print('io', end=' ', file=fout)
    print('i i i i i i i i i i i i i i', file=fout)

    print('vname', 'IMME<[15:0]>', 'SW_IMME<[15:0]>', 
    'RD1<[2:0]>', 'RD2<[2:0]>', 'SWI','ALU_OP<[2:0]>',
    'ALU_SRC','MEM_WRITE', 'LWI', 'WR_REG<[2:0]>',
    'REG_WRITE', 'DATA2REG<[1:0]>', file=fout)

    print('slope', '0.01', file=fout)
    print('vih', '1.8', file=fout)
    print('vil', '0', file=fout)
    print('tunit', '2ns', file=fout)
    print('', file=fout)
    print(';t\t','IMM', ' SW_I',
          'RD1', 'RD2', 'SWI', 'A_OP',
          'A_SRC', 'RDE','M_WR', 'LWI', 'WR_R',
          'R_WR', 'D2R','MIN', file=fout)

    for num, each in enumerate(machine_code):
        print(num, end = '\t', file = fout) 
        print(each[0:4], end = '  ', file = fout) # IMME 0+4 =4
        print(each[4:8], end='  ', file=fout)  # SW_IMME 4+4 =8
        print(each[8], end='   ', file=fout)  # RD1 9
        print(each[9], end='   ', file=fout)  # RD2 10
        print(each[10], end = '   ', file = fout)  #SWI 11
        print(int(each[11:14],2), end = '    ', file = fout) #ALU_OP 11+3
        print(each[14], end = '     ', file = fout) #ALU_SRC +1
        print(each[15], end='    ', file=fout)  # RD_ENABLE +1
        print(each[16], end='    ', file=fout) #MEM_WRITE +1
        print(each[17], end='   ', file=fout) #LWI +1
        print(each[18], end='    ', file=fout) #WR_REG +1
        print(each[19], end='    ', file=fout) #REG_WRITE +1
        print(each[20], end='   ', file=fout) #DATA2REG +1
        print(each[21], end='   ', file=fout)  # DATA2REG +1
        print('', file = fout)

