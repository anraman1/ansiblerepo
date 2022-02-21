#!/usr/bin/python3
# This program is to merge the given list
# And To check the excess length of elemement between the List
# using Zip function
# usage: mergelists.py [-h] [-l LIST LIST] [-a {m,d}]
##################
__version__="1.0.0"
##################

import argparse
from argparse import RawTextHelpFormatter

def main():

    import argparse

    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument('-l',
                        dest='List',
                        nargs=2,
                        help="Pass two paramenters(list) \n"
                        "Example \n"
                        "merge.py --l 1,2,3,2 a,b,c,d,f",
                        default=['1,2,3,4', 'a,b,c,d,f']
                        )
    parser.add_argument('-a',
                        choices = ['m','d'],
                        help="m for Merge the list \n"
                            "d for To see excess length of element from the given list \n"
                            "Default is m ",
                        default='m'
                        )
    args = parser.parse_args()
    l_action = args.a
    List1=list(args.List[0].split(','))
    List2=list(args.List[1].split(','))
    List3=[]
    if not type(List1) is list or not type(List2) is list:
       raise TypeError("Give Values are not a List format")

    def print_output(List1,List2,List3,action): 

        if action == 'm':
            msg="combined List"
        elif action == 'd':
            msg="excess length of element"
        print("List one : {}\nList Two : {}\n{} : {}".format(List1,List2,msg,List3))


    def merge_list(l1,l2):
        return [item for sl in zip(l1,l2) for item in sl]



    if l_action == 'm':
        List3=merge_list(List1,List2)


# zip function only combins the same number of elemenet from given List
# Here just adding remaining elements from higher Lenth List into the new List using below code.
# And printing the final output
        if len(List1) > len(List2):
            List3=List3+List1[len(List2)-len(List1)::]

        elif len(List2) > len(List1):
           List3=List3+List2[len(List1)-len(List2)::]

# if arg pass d ( to see to see the execs length of the elements )
    elif l_action == 'd':

        if len(List1) > len(List2):
           List3=List1[len(List2)-len(List1)::]

        elif len(List2) > len(List1):
           List3=List2[len(List1)-len(List2)::]



    print_output(List1,List2,List3,l_action)

if __name__ ==  "__main__":
 main()
