import argparse

from my_package.data_processing import input_data, filter_by_name, filter_by_declination
from my_package.plotting import mollewide_plot
from my_package.load_data import PULSAR_CSV_PATH


def main():
    # Create an argument parser so users can understand and use command line options
    parser = argparse.ArgumentParser(description='Process and filter an input CSV file and create a sky plot of the sources.')

    # Add arguments to the parser
    parser.add_argument(
        # A short version of the argument which is normally a single dash and a single letter
        '-i',
        # A long version of the argument which is normally two dashes and a word
        '--input',
        # The type of the argument that will be converted when it is read in
        type=str,
        # A description of what the argument does
        help='The path to the input csv file. If none is provided the default pulsar data will be used.',
        # The default value of the argument if none is provided
        default=PULSAR_CSV_PATH,
    )
    # nargs='*' means that the argument can take 0 or more values
    parser.add_argument('-s', '--source', type=str, nargs='*', help='A space separated list of source names to plot.')
    parser.add_argument('--dec_min', type=float, help='A minimum declination of sources to plot.', default=-90.)
    parser.add_argument('--dec_max', type=float, help='A maximum declination of sources to plot.', default=90.)

    # Parse the arguments
    args = parser.parse_args()

    # Read in the data
    df = input_data(args.input)

    # If filters are given filter the data
    if args.source:
        print(f"Filtering by source name: {args.source}")
        df = filter_by_name(df, args.source)
    print(f"Filtering by declination: {args.dec_min} to {args.dec_max}")
    df = filter_by_declination(df, args.dec_min, args.dec_max)

    print("Plotting the data")
    mollewide_plot(df)

if __name__ == "__main__":
    main()