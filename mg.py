#!/usr/bin/python

import sys



def mg():
    if len(sys.argv) < 3:
        print('Error! Two arguments required!')
        sys.exit()
    file_1 = sys.argv[1]
    file_2 = sys.argv[2]
    ## print(file_1, file_2)
    with open(file_1) as f1:
        lines_1 = f1.readlines()
    with open(file_2) as f2:
        lines_2 = f2.readlines()
    len1, len2 = len(lines_1), len(lines_2)
    if len1 != len2:
        if len1 > len2:
            extra_lines = lines_1[len2:len1]
            lines_1 = lines_1[:len2]
        else:
            extra_lines = lines_2[len1:len2]
            lines_2 = lines_2[:len1]
    ##print(lines_1)
    ##print('********************************')
    ##print(lines_2)
    diffs_dict = dict()
    i = 0
    line = 0
    while i < len(lines_1):
        line += 1
        if lines_1[i] != lines_2[i]:
            diffs_dict[line] = [lines_1[i], lines_2[i]]
        i += 1
    confs = len(diffs_dict)
    if confs > 0:
        print(f'Number of conficts: {confs}')
        for conf in diffs_dict.keys():
            print(f'In line: {conf}:\n(1)->{file_1}<<<\n{diffs_dict[conf][0]}>>>{file_2}-<-(2)\n{diffs_dict[conf][1]}\n')
    print('Extra lines:')
    for ln in extra_lines:
        print(ln)

            


mg()