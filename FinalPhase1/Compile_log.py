def log_printer(Instr_split, machine_code, fout):
    print(Instr_split, file = fout)
    print('*******************IMME*******************',file = fout)
    print('IMME    = ', machine_code[0:4], file = fout)
    print('SW_IMME = ', machine_code[4:8], file = fout)
    print('*******************ID*******************',file = fout)
    print('RD1 = ', machine_code[8], file = fout)
    print('RD2 = ', machine_code[9], file=fout)
    print('SWI = ', machine_code[10], file=fout)
    print('*******************EX*******************',file = fout)
    print('ALU_OP  = ', machine_code[11:14], file=fout)
    print('ALU_SRC = ', machine_code[14], file=fout)
    print('*******************MEM*******************',file = fout)
    print('READ_EN', machine_code[15],file = fout)
    print('MEM_WRITE|LWI = ', machine_code[16:18], file=fout)
    print('MIN = ', machine_code[21], file = fout)
    print('*******************WB*******************', file=fout)
    print('WRITE_REG|REG_WRITE = ', machine_code[18], machine_code[19], file=fout)
    print('DATA2REG         = ', machine_code[20], file=fout)
    
    print('',file = fout)
    print('',file = fout)
