import argparse

parser = argparse.ArgumentParser('Hellowsies')

parser.add_argument('number1',type = float,help ='Numero uno')
parser.add_argument('number2',type = float,help ='Numero duo')

parser.add_argument('--scale',type = float,default = 1, help= 'Scale for the addition')

args = parser.parse_args()

print((args.number1+args.number2)*args.scale)