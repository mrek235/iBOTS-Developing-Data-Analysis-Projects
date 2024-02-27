import glob
import numpy as np
import pandas as pd
import argparse
from pathlib import Path 
parser =argparse.ArgumentParser('Feed me Path')

parser.add_argument('input_path',type=str,help = 'Input path for CSV files, Path must finish with \\ ')

args = parser.parse_args()

task_data_path = Path(args.input_path)

task_data_pattern = str(task_data_path / 'trial*.csv')
task_csvs = glob.glob(task_data_pattern)

csv_list = []
for csv in task_csvs:
    current_csv = pd.read_csv(csv)
    csv_list.append(current_csv)

task_df = pd.concat(csv_list)
task_df['Path'] = task_csvs
task_df.to_csv('C:\\Users\\mreki\\iBOTS-Developing-Data-Analysis-Projects\\session2\\data\\processed\\performance_data.csv')