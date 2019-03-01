import re
from collections import Counter
from random import randint

def read_txt():
    words = []
    try:
        fin = open('./in.txt','r')
    except:
        print("Can't open file.")
    else:
        #readline = fin.readlines()
        for line_num,each_line in enumerate(fin,1):
            each_line =  re.sub(r'[^\w\s]','',each_line.strip('\n'))
            words.append((line_num, each_line.split(' ')))#[(line_num,one_line),...]
    # print(words)
    return words

def word_numbered(words_in_txt):
    fout = open('./out1.txt','w')
    all_words = []
    fout.write("Word number\tWord\n")
    for each_line in words_in_txt:
        # print(each_line)
        if not each_line[1] == ['\n']:
            all_words += each_line[1][:-2]

    for word_num, each_word in enumerate(all_words,1):
        fout.write("%d\t\t%s\n"%(word_num, each_word))

    fout.close()

# def word_count(words_in_txt):
#     content = []
#     for word in words_in_txt:
#         content += word[1]
#     data=dict(Counter(content))
#     data = sorted(data.items(), key = lambda item:item[1],reverse = False)
    
#     print("Word number\tWord")
#     for k,v in data:
#         print("%d\t\t%s" % (v,k))

def count_the(words_in_txt):
    fout = open('out2.txt','w')
    the_counter = {}
    fout.write('Line Number with \'the\'\t\tNumber of \'the\'\n')
    for each_line in words_in_txt:
        count = 0
        for word in each_line[1]:
            if re.match(r'\bthe\b',word,re.IGNORECASE): # match the, ignore the case
                count = count+1
        if(count):
            fout.write('%d\t\t\t\t%d\n' %(each_line[0],count));
            the_counter[each_line[0]] = count

    fout.close()


def random_insert():
    '''
    Random insert to anywhere of the txt
    each time insert the, it print line number(even the line number is same, the location of the is different)
    '''
    fin = open('in.txt','r')
    fout = open('input2.txt','w')
    fout2 = open('out3.txt','w')

    fout2.write('Random line Number\t\tNumber of “the”\n')
    context = []
    line_wordcounts = []
    word_count = 0
    thirty_random_number = []
    for line_num,each_line in enumerate(fin,0):
        context.append([line_num,each_line.split()]) #[line_number, words of each line in list]
        line_wordcounts.append([line_num,len(each_line.split(' '))])#(line_number, number of words in each line)
        word_count += len(each_line.split())#totoal words

    for i in range(30):
        while True:
            insert_position = randint(0,word_count)

            if not insert_position in thirty_random_number: #generate one random number
                thirty_random_number.append(insert_position)
                word_count += 1
                break
        
        for line_wordcount in line_wordcounts: #[which_line,how_many_words]
            insert_position -= line_wordcount[1]

            if insert_position <= 0:
                # print('insert position', insert_position + line_wordcount[1])
                # print(line_wordcount[0])
                # print(context[line_wordcount[0]])
                context[line_wordcount[0]][1].insert(insert_position + line_wordcount[1],'The') # insert
                fout2.write('%d\t\t\t\t%d\n' %(line_wordcount[0],i+1))
                break

    fout2.close()
    # print(thirty_random_number)
    for lines in context: #output
        for word in lines[1]:
            print(word,end = ' ',file = fout)

        print('\n',end = '',file = fout)
    fout.close()


if __name__ == '__main__':
    words = read_txt()
    #word_count(words)
    word_numbered(words)
    count_the(words)
    random_insert()



