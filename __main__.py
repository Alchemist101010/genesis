import argparse as arg
from sys import argv

in_file = argv

parser = arg.ArgumentParser(description='Genesis 0.10\nSearch for data')
parser.add_argument('-o', help='Open a file: Usage python Genesis -o <file>' , action='store_true')
parser.add_argument('-c', help='Concatenate a file.' , action='store_true')
parser.add_argument('-i', help='irritate like anything', action='store_true')

args = parser.parse_args()
if args.o:
    print ("Opening... Opening.... La la la!")
    x = input('Open the file you wish for. Look at Genesis using ls:')
    open(x)

if args.c:
    print ("CatTing... Farting...")
    y = input('Concatenate file:')
    md = open(y)
    md.read()

if args.i:
    print ("Smack your head on the keyboard and type random strings here")
    z = input('Type:')
    print (z * 10000)
    
args = parser.parse_args()