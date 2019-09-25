import csv
import argparse

parser = argparse.ArgumentParser(description="Fix CSV files")
parser.add_argument("--in-delimiter", type=str, help="Delimiter in Source File", default="|")
parser.add_argument("--in-quote", type=str, help="Quote character in Source File", default='"')
parser.add_argument("source", type=str, help="Source File name")
parser.add_argument("dest", type=str, help="Destination File name")

args = parser.parse_args()

DELIMITER = args.in_delimiter
QUOTE = args.in_quote
SOURCE = args.source
DEST = args.dest

with open(SOURCE, newline='') as csvfile:
    arguments = {}
    if DELIMITER:
        arguments['delimiter'] = DELIMITER
    if QUOTE:
        arguments['quotechar'] = QUOTE
    if not DELIMITER or not QUOTE:
        rows = list(csv.reader(csvfile, **arguments))
    else:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        rows = list(csv.reader(csvfile, dialect))

    with open(DEST, 'w', newline='') as outfile:
        csv.writer(outfile).writerows(rows)