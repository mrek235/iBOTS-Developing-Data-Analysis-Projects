import sys
import pandas as pd
import argparse
parser = argparse.ArgumentParser('Greetings')

# Command-line inputs
parser.add_argument('input_csv',type = str,help = 'Input csv path')
parser.add_argument('output_csv',type = str,help = 'Output csv path')
args = parser.parse_args()

# Load the csv file and extract active trials
df = pd.read_csv(args.input_csv)
df_valid = df[df.valid].copy()

# Save the new dataframe as a csv file
df_valid.to_csv(args.output_csv, index=False)