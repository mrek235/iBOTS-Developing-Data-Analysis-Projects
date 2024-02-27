import argparse
import numpy as np
parser = argparse.ArgumentParser('Greetings')


# Command-line inputs

parser.add_argument('input_arr',type = str,help = 'Input arr')
parser.add_argument('output_arr',type = str,help = 'Output arr')
parser.add_argument('--method',type = str,default = 'std', help = 'Method. std or norm')

args = parser.parse_args()
if args.method == 'std' :
    # Load the input and standardize it
    input_array = np.load(args.input_arr)
    output_array = (input_array - np.mean(input_array)) / np.std(input_array)
if args.method == 'norm' :
    input_array = np.load(args.input_arr)
    output_array = input_array - np.min(input_array)
    output_array = output_array / np.max(output_array)

# Save the standardized array

np.save(args.output_arr, output_array)