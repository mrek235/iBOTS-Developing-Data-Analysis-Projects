import argparse 

parser = argparse.ArgumentParser('Greetings')

parser.add_argument('num',type=float,help = 'Num to be squared')
args = parser.parse_args()

print(args.num*args.num)