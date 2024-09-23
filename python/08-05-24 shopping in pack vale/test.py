tes=[]

test=input("type the thing you are trying to find")



with open(r"business.txt", 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if test in line:
            print('string found in a file')
            print('Line Number:', l_no)
            print('Line:', line)
            # don't look for next lines
            break
