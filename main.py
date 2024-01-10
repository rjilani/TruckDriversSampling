import configparser
import os
import sys
from datetime import datetime
import pandas as pd

input_dir = "input_dir"
output_dir = "output_dir"
output_file = "employees-" + datetime.today().strftime('%Y-%m-%d-%H-%M-%S') + ".csv"


def random_output(file, sample_size, debug):
    df = pd.read_csv(os.path.join(input_dir, file))
    if debug == "True":
        print(output_file)
        print(df.columns)
        print(df.head())
        print(df.info(verbose=True, show_counts=True))

    row_count = df.shape[0]
    size = int(sample_size)

    if size > row_count:
        exit_program(size, row_count, file)

    rows = df.sample(n=size)
    rows.to_csv(os.path.join(output_dir, output_file), encoding='utf-8', index=False)


def create_dir():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def exit_program(sample_size, rows_in, file):
    print(
        f'Random sample {sample_size} should be lower than or equal to number of records that is {rows_in} in the file named {file}')
    sys.exit(0)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('./config/config.ini')
    print(f'Generating Sample file of size:' + config['DEFAULT']['SampleSize'])
    try:
        create_dir()
        random_output(config['DEFAULT']['FileName'], config['DEFAULT']['SampleSize'], config['DEFAULT']['Debug'])
    except Exception as e:
        print("An exception occurs: " + str(sys.exc_info()[0]))
        print(e)
