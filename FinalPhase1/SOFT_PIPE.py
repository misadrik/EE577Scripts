from Compile_log import log_printer
from VEC_GEN import print_vec
from MiniCompiler import compiler

RF = {'$0': 0, '$1': 0, '$2': 0, '$3': 0, '$4': 0, '$5': 0, '$6': 0, '$7': 0}
MEM = {}

Rtype = ['and', 'or', 'add','min', 'mul']
Itype = ['andi', 'ori', 'addi', 'mini', 'muli', 'sfl', 'sfr']
LWI = ['lwi']
SWI = ['swi']
LW = ['lw']
SW = ['sw']

def SOFT_PIPE():
    fin = open('./assemblycode.txt', 'r')

    for instr in fin.readlines():
        instr_split = instr.split()

        OPCODE = instr_split[0]

        if OPCODE in LWI:
            LWI_FUNC(instr_split[0], instr_split[1], instr_split[2])
        if OPCODE in Rtype:
            Rtype_FUNC(instr_split[0], instr_split[1],
                       instr_split[1], instr_split[2])


def print_RESULT():
    fout = open('./idea_result.txt','w')

def Rtype_FUNC(OP_CODE, RD, RS, RT):
    if OP_CODE == 'and':
        RD_DATA = Fetch_RF(RS) and Fetch_RF(RT)
        RF[RD] = RD_DATA 
    
    if OP_CODE == 'or':
        RD_DATA = Fetch_RF(RS) or Fetch_RF(RT)
        RF[RD] = RD_DATA 

    if OP_CODE == 'add':
        RD_DATA = Fetch_RF(RS) + Fetch_RF(RT)
        RF[RD] = RD_DATA

    if OP_CODE == 'min':
        RD_DATA = min(Fetch_RF(RS),Fetch_RF(RT))
        RF[RD] = RD_DATA 

    if OP_CODE == 'mul':
        RD_DATA = Fetch_RF(RS) * Fetch_RF(RT)
        RF[RD] = RD_DATA

def hex_to_dec(hex_num):
    
def dec_to_hex():

def Fetch_RF(REG_NAME):
    return int(RF[REG_NAME],16)


def Fetch_MEM():

if __name__ == "__main__":
    compiler()
