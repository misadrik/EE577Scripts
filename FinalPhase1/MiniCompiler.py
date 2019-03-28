from Compile_log import log_printer
from VEC_GEN import print_vec

def compiler():
    fin = open('./assemblycode.txt','r')
    #fout = open('./machinecode.txt','w')
    fout_log = open('./compilelog.txt','w')
    fout_vec = open('./phase1_test.vec', 'w')

    vec_machine_code = []
    for instr in fin.readlines():
        instr_split = instr.split()
        print(instr_split)
        if instr_split[0] == 'swi':
            if 'H' in instr_split[1]:
                num, machine_code = SWI_DEC(instr_split)
                vec_machine_code.append(machine_code)
                log_printer(instr_split, machine_code, fout_log)

            elif instr_split[1] == '1' or instr_split[1] == '2' or instr_split[1] == '4':
                
                num, machine_code = SWI_DEC(instr_split)
                
                if num == 0:
                    pass
                elif num == 1:
                    vec_machine_code.append(machine_code)
                    log_printer(instr_split, machine_code, fout_log)
                elif num == 2:
                    for i in range(2):
                        # print(machine_code[i])
                        vec_machine_code.append(machine_code[i])
                        log_printer(instr_split, machine_code[i], fout_log)
                elif num == 4:
                    for i in range(4):
                        print(machine_code[i])
                        vec_machine_code.append(machine_code[i])
                        log_printer(instr_split, machine_code[i], fout_log)
                    
            else:
                print('Error000: Command ' + instr.strip() + ' has invalid burst length')

        else:
            machine_code = Instr_decode(instr_split)
            vec_machine_code.append(machine_code)
        #print(machine_code, file = fout)
        
            print(machine_code)
            log_printer(instr_split, machine_code, fout_log)

    print(vec_machine_code)
    print_vec(vec_machine_code, fout_vec) 

    fin.close()  

def hex_to_binlist(hex_num, digit='4'):
    hex_num = hex_num.strip('H')
    hex_num = ('{:0'+str(digit)+'x}').format(int(hex_num, 16))
    return hex_num.split('x')[-1]


def BURST_ADDR(hex_num, burst,digit='4'):
    hex_num = hex_num.strip('H')
    
    if burst == 2:
        hex_num0 = ('{:0'+str(digit)+'x}').format(int(hex_num, 16))
        hex_num1 = ('{:0'+str(digit)+'x}').format(int(hex_num, 16)+1)
        return hex_num0.split('x')[-1], hex_num1.split('x')[-1]
    if burst == 4:
        hex_num0 = ('{:0'+str(digit)+'x}').format(int(hex_num, 16))
        hex_num1 = ('{:0'+str(digit)+'x}').format(int(hex_num, 16)+1)
        hex_num2 = ('{:0'+str(digit)+'x}').format(int(hex_num, 16)+2)
        hex_num3 = ('{:0'+str(digit)+'x}').format(int(hex_num, 16)+3)
        return hex_num0.split('x')[-1], hex_num1.split('x')[-1], hex_num2.split('x')[-1], hex_num3.split('x')[-1]

def dec3_to_binlist(dec_num, digit='3'):
    dec_num = dec_num.strip('$')
    return dec_num

def IMME_to_HEX(dec_num,digit = '4'):
    dec_num = dec_num.strip('#')
    hex_num = ('{:0'+str(digit)+'x}').format(int(dec_num,16))
    return hex_num.split('x')[-1]

def SWI_DEC(INSTR_SPLIT):
    if len(INSTR_SPLIT) == 3:
        # IMM
        IMME = hex_to_binlist(INSTR_SPLIT[1])
        SWI_IMME = IMME_to_HEX(INSTR_SPLIT[2])
        RD1 = '0'
        RD2 = '0'
        SWI = '1'
        # EX
        ALU_OP = '000'  # regular special in i type
        ALU_SRC = '0'
        # MEM
        READ_EN='0'
        MEM_WRITE = '1'
        LWI = '0'
        # WB
        WR_REG = '0'
        REG_WRITE = '0'
        DATA_TO_REG = '0'
        MIN = '0'

        DECODED_INSTR = IMME + SWI_IMME + RD1 + RD2 + SWI + ALU_OP \
                + ALU_SRC + READ_EN + MEM_WRITE + LWI + WR_REG + REG_WRITE + DATA_TO_REG + MIN

        return  1, DECODED_INSTR

    if len(INSTR_SPLIT) == 4:
                # IMM
        IMME = hex_to_binlist(INSTR_SPLIT[2])
        SWI_IMME = IMME_to_HEX(INSTR_SPLIT[3])
        RD1 = '0'
        RD2 = '0'
        SWI = '1'
        # EX
        ALU_OP = '000'  # regular special in i type
        ALU_SRC = '0'
        # MEM
        READ_EN = '0'
        MEM_WRITE = '1'
        LWI = '0'
        # WB
        WR_REG = '0'
        REG_WRITE = '0'
        DATA_TO_REG = '0'
        MIN = '0'

        DECODED_INSTR = IMME + SWI_IMME + RD1 + RD2 + SWI + ALU_OP \
            + ALU_SRC + READ_EN + MEM_WRITE + LWI + WR_REG + REG_WRITE + DATA_TO_REG + MIN

        return 1, DECODED_INSTR

    if len(INSTR_SPLIT) == 5:
        if(int(hex_to_binlist(INSTR_SPLIT[2]), 16) % 2) != 0:
            print('ERROR001: Command ' +
                  INSTR_SPLIT[0] + ' ' + INSTR_SPLIT[1] + ' ' + INSTR_SPLIT[2] + ' ' 
                  + INSTR_SPLIT[3] + ' ' + INSTR_SPLIT[4] + ' '+ 'is not aligned properly')
        
            return 0, 'INVALID'
        
        else:
            IMME0, IMME1 = BURST_ADDR(INSTR_SPLIT[2],2)
            print(IMME0,IMME1)
            SWI_IMME0 = IMME_to_HEX(INSTR_SPLIT[3])
            SWI_IMME1 = IMME_to_HEX(INSTR_SPLIT[4])
            RD1 = '0'
            RD2 = '0'
            SWI = '1'
            # EX
            ALU_OP = '000'  # regular special in i type
            ALU_SRC = '0'
            # MEM
            READ_EN = '0'
            MEM_WRITE = '1'
            LWI = '0'
            # WB
            WR_REG = '0'
            REG_WRITE = '0'
            DATA_TO_REG = '0'
            MIN = '0'

            DECODED_INSTR0 = IMME0 + SWI_IMME0 + RD1 + RD2 + SWI + ALU_OP \
                + ALU_SRC + READ_EN + MEM_WRITE + LWI + WR_REG + REG_WRITE + DATA_TO_REG + MIN

            DECODED_INSTR1 = IMME1 + SWI_IMME1 + RD1 + RD2 + SWI + ALU_OP \
                + ALU_SRC + READ_EN + MEM_WRITE + LWI + WR_REG + REG_WRITE + DATA_TO_REG + MIN
            
            # print([DECODED_INSTR0, DECODED_INSTR1])
            return 2, [DECODED_INSTR0, DECODED_INSTR1]

    if len(INSTR_SPLIT) == 7:
        if(int(hex_to_binlist(INSTR_SPLIT[2]), 16) % 4) != 0:
            print('ERROR001: Command ' +
                INSTR_SPLIT[0] + ' ' + INSTR_SPLIT[1] + ' ' + INSTR_SPLIT[2] + ' ' 
              + INSTR_SPLIT[3] + ' ' + INSTR_SPLIT[4] + ' ' + INSTR_SPLIT[5] + ' ' 
              + INSTR_SPLIT[6] + ' ' + 'is not aligned properly')
    
            return 0, 'INVALID'
    
        else:
            IMME0, IMME1, IMME2, IMME3 = BURST_ADDR(INSTR_SPLIT[2],4)
            SWI_IMME0 = IMME_to_HEX(INSTR_SPLIT[3])
            SWI_IMME1 = IMME_to_HEX(INSTR_SPLIT[4])
            SWI_IMME2 = IMME_to_HEX(INSTR_SPLIT[5])
            SWI_IMME3 = IMME_to_HEX(INSTR_SPLIT[6])
            RD1 = '0'
            RD2 = '0'
            SWI = '1'
            # EX
            ALU_OP = '000'  # regular special in i type
            ALU_SRC = '0'
            # MEM
            READ_EN = '0'
            MEM_WRITE = '1'
            LWI = '0'
            # WB
            WR_REG = '0'
            REG_WRITE = '0'
            DATA_TO_REG = '0'
            MIN = '0'

            DECODED_INSTR0 = IMME0 + SWI_IMME0 + RD1 + RD2 + SWI + ALU_OP \
                + ALU_SRC + READ_EN + MEM_WRITE + LWI + WR_REG + REG_WRITE + DATA_TO_REG + MIN

            DECODED_INSTR1 = IMME1 + SWI_IMME1 + RD1 + RD2 + SWI + ALU_OP \
                + ALU_SRC + READ_EN + MEM_WRITE + LWI + WR_REG + REG_WRITE + DATA_TO_REG + MIN

            DECODED_INSTR2 = IMME2 + SWI_IMME2 + RD1 + RD2 + SWI + ALU_OP \
                + ALU_SRC + READ_EN + MEM_WRITE + LWI + WR_REG + REG_WRITE + DATA_TO_REG + MIN

            DECODED_INSTR3 = IMME3 + SWI_IMME3 + RD1 + RD2 + SWI + ALU_OP \
                + ALU_SRC + READ_EN + MEM_WRITE + LWI + WR_REG + REG_WRITE + DATA_TO_REG + MIN

            # print([DECODED_INSTR0, DECODED_INSTR1, DECODED_INSTR2, DECODED_INSTR3])
            return 4, [DECODED_INSTR0, DECODED_INSTR1, DECODED_INSTR2, DECODED_INSTR3]

def Instr_decode(INSTR_SPLIT):
    if INSTR_SPLIT[0] == 'sw':
        mcd = swi()
        # IMM
        IMME = hex_to_binlist(INSTR_SPLIT[1])
        SWI_IMME = '0000'
        RD1 = dec3_to_binlist(INSTR_SPLIT[2])
        RD2 = '0'
        SWI = '0'
        # EX
        ALU_OP = '000'  # regular special in i type
        ALU_SRC = '0'
        # MEM
        READ_EN='0'
        MEM_WRITE = '1'
        LWI = '0'
        # WB
        WR_REG = '0'
        REG_WRITE = '0'
        DATA_TO_REG = '0'
        MIN = '0'

    if INSTR_SPLIT[0] == 'lw':
        # IMM
        IMME = hex_to_binlist(INSTR_SPLIT[2])
        SWI_IMME = '0000'
        RD1 = '0'
        RD2 = '0'
        SWI = '0'
        # EX
        ALU_OP = '000'  # regular special in i type
        ALU_SRC = '0'
        # MEM
        READ_EN='1'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '1'
        MIN = '0'

    if INSTR_SPLIT[0] == 'lwi':
        # IMM
        IMME = IMME_to_HEX(INSTR_SPLIT[2])
        SWI_IMME = '0000'
        RD1 = '0'
        RD2 = '0'
        SWI = '0'
        # EX
        ALU_OP = '000'  # regular special in i type
        ALU_SRC = '0'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '1'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '2'
        MIN = '0'


    if INSTR_SPLIT[0] == 'and':
        # IMM
        IMME = '0000'
        SWI_IMME = '0000'
        RD1 = dec3_to_binlist(INSTR_SPLIT[2])
        RD2 = dec3_to_binlist(INSTR_SPLIT[3])
        SWI = '0'
        # EX
        ALU_OP = '010' ###regular special in i type
        ALU_SRC = '0'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '0'
        MIN = '0'

    if INSTR_SPLIT[0] == 'or':
        # IMM
        IMME = '0000'
        SWI_IMME = '0000'
        RD1 = dec3_to_binlist(INSTR_SPLIT[2])
        RD2 = dec3_to_binlist(INSTR_SPLIT[3])
        SWI = '0'
        # EX
        ALU_OP = '100' ###regular special in i type
        ALU_SRC = '0'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '0'
        MIN = '0'

    if INSTR_SPLIT[0] == 'min':
        # IMM
        IMME = '0000'
        SWI_IMME = '0000'
        RD1 = dec3_to_binlist(INSTR_SPLIT[2])
        RD2 = dec3_to_binlist(INSTR_SPLIT[3])
        SWI = '0'
        # EX
        ALU_OP = '001' ###regular special in i type
        ALU_SRC = '0'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '2' ### special in r type
        MIN = '1'

    if INSTR_SPLIT[0] == 'add':
        # IMM
        IMME = '0000'
        SWI_IMME = '0000'
        RD1 = dec3_to_binlist(INSTR_SPLIT[2])
        RD2 = dec3_to_binlist(INSTR_SPLIT[3])
        SWI = '0'
        # EX
        ALU_OP = '000' ###regular special in i type
        ALU_SRC = '0'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '0'
        MIN = '0'

   
    if INSTR_SPLIT[0] == 'addi':
        # IMM
        IMME = IMME_to_HEX(INSTR_SPLIT[3])
        SWI_IMME = '0000'
        RD1 = dec3_to_binlist(INSTR_SPLIT[2])
        RD2 = '0'
        SWI = '0'
        # EX
        ALU_OP = '000' ###regular special in i type
        ALU_SRC = '1'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '0'
        MIN = '0'

    if INSTR_SPLIT[0] == 'mini':
        # IMM
        IMME = IMME_to_HEX(INSTR_SPLIT[3])
        SWI_IMME = '0000'
        RD1 = dec3_to_binlist(INSTR_SPLIT[2])
        RD2 = '0'
        SWI = '0'
        # EX
        ALU_OP = '001' ###regular special in i type
        ALU_SRC = '1'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '2' ######special in imme####
        MIN = '0'

    if INSTR_SPLIT[0] == 'andi':
        # IMM
        IMME = IMME_to_HEX(INSTR_SPLIT[3])
        SWI_IMME = '0000'
        RD1 = dec3_to_binlist(INSTR_SPLIT[2])
        RD2 = '0'
        SWI = '0'
        # EX
        ALU_OP = '010' ###regular special in i type
        ALU_SRC = '1'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '0'
        MIN = '0'

    if INSTR_SPLIT[0] == 'ori':
        # IMM
        IMME = IMME_to_HEX(INSTR_SPLIT[3])
        SWI_IMME = '0000'
        RD1 = dec3_to_binlist(INSTR_SPLIT[2])
        RD2 = '0'
        SWI = '0'
        # EX
        ALU_OP = '100' ###regular special in i type
        ALU_SRC = '1'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '0'
        MIN = '0'

    if INSTR_SPLIT[0] == 'sfl':
        # IMM
        IMME = IMME_to_HEX(INSTR_SPLIT[3])
        SWI_IMME = '0000'
        RD1 = dec3_to_binlist(INSTR_SPLIT[2])
        RD2 = '0'
        SWI = '0'
        # EX
        ALU_OP = '110' ###regular special in i type
        ALU_SRC = '1'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '0'
        MIN = '0'

    if INSTR_SPLIT[0] == 'sfr':
        # IMM
        IMME = IMME_to_HEX(INSTR_SPLIT[3])
        SWI_IMME = '0000'
        RD1 = dec3_to_binlist(INSTR_SPLIT[2])
        RD2 = '0'
        SWI = '0'
        # EX
        ALU_OP = '111' ###regular special in i type
        ALU_SRC = '1'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = dec3_to_binlist(INSTR_SPLIT[1])
        REG_WRITE = '1'
        DATA_TO_REG = '0'
        MIN = '0'

    if INSTR_SPLIT[0] == 'nop':
        # IMM
        IMME = '0000'
        SWI_IMME = '0000'
        RD1 = '0'
        RD2 = '0'
        SWI = '0'
        # EX
        ALU_OP = '000'  # regular special in i type
        ALU_SRC = '0'
        # MEM
        READ_EN='0'
        MEM_WRITE = '0'
        LWI = '0'
        # WB
        WR_REG = '0'
        REG_WRITE = '0'
        DATA_TO_REG = '0'
        MIN = '0'    

    DECODED_INSTR = IMME + SWI_IMME + RD1 + RD2 + SWI + ALU_OP \
        + ALU_SRC + READ_EN + MEM_WRITE + LWI + WR_REG + REG_WRITE + DATA_TO_REG + MIN

    return DECODED_INSTR
    print(DECODED_INSTR)

if __name__ == '__main__':
    compiler()
    SOFT_PIPE()
