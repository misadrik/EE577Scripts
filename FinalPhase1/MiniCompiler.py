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
        machine_code = Instr_decode(instr_split)
        
        vec_machine_code.append(machine_code)
        #print(machine_code, file = fout)
        
        log_printer(instr_split, machine_code, fout_log)

    print(vec_machine_code)
    print_vec(vec_machine_code, fout_vec)   

def hex_to_binlist(hex_num, digit='4'):
    hex_num = hex_num.strip('H')
    hex_num = ('{:0'+str(digit)+'x}').format(int(hex_num, 16))
    return hex_num.split('x')[-1]


def dec3_to_binlist(dec_num, digit='3'):
    dec_num = dec_num.strip('$')
    return dec_num


def dec_to_hex(dec_num,digit = '4'):
    dec_num = dec_num.strip('#')
    hex_num = ('{:0'+str(digit)+'x}').format(int(dec_num))
    return hex_num.split('x')[-1]

def Instr_decode(INSTR_SPLIT):
    if INSTR_SPLIT[0] == 'sw':
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

    if INSTR_SPLIT[0] == 'swi':
        # IMM
        IMME = hex_to_binlist(INSTR_SPLIT[1])
        SWI_IMME = dec_to_hex(INSTR_SPLIT[2])
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

    if INSTR_SPLIT[0] == 'lwi':
        # IMM
        IMME = dec_to_hex(INSTR_SPLIT[2])
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

   
    if INSTR_SPLIT[0] == 'addi':
        # IMM
        IMME = dec_to_hex(INSTR_SPLIT[3])
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

    if INSTR_SPLIT[0] == 'mini':
        # IMM
        IMME = dec_to_hex(INSTR_SPLIT[3])
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

    if INSTR_SPLIT[0] == 'andi':
        # IMM
        IMME = dec_to_hex(INSTR_SPLIT[3])
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

    if INSTR_SPLIT[0] == 'ori':
        # IMM
        IMME = dec_to_hex(INSTR_SPLIT[3])
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

    if INSTR_SPLIT[0] == 'sfl':
        # IMM
        IMME = dec_to_hex(INSTR_SPLIT[3])
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

    if INSTR_SPLIT[0] == 'sfr':
        # IMM
        IMME = dec_to_hex(INSTR_SPLIT[3])
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
    
    DECODED_INSTR = IMME + SWI_IMME + RD1 + RD2 + SWI + ALU_OP \
        + ALU_SRC + READ_EN + MEM_WRITE + LWI + WR_REG + REG_WRITE + DATA_TO_REG

    return DECODED_INSTR
    print(DECODED_INSTR)

if __name__ == '__main__':
    compiler()
