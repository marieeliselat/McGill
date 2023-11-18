import argparse
import pandas as pd
import sys
from datetime import datetime
import logging
from enum import Enum

# Constants and Enum definitions
class Nyc311ColumnName(Enum):
    Borough = "Borough"
    ComplaintType = "Complaint Type"
    OpenedDate = "Created Date"
    ClosedDate = "Closed Date"
    Status = "Status"

INCIDENT_ZIP = "Incident Zip"
OPENED_AT_COLUMN_NAME = "Created Date"
CLOSED_AT_COLUMN_NAME = "Closed Date"
DURATION_COLUMN_NAME = "Duration"

# Data Preparation Functions
def load_and_filter_data(file_name, start_date, end_date):
    df = pd.read_csv(file_name)
    fmt_string = "%Y.%m.%d"
    start_date = datetime.strptime(start_date, fmt_string)
    end_date = datetime.strptime(end_date, fmt_string)
    df[Nyc311ColumnName.OpenedDate.value] = pd.to_datetime(df[Nyc311ColumnName.OpenedDate.value], format="%m/%d/%Y %I:%M:%S %p")
    df = df[(df[Nyc311ColumnName.OpenedDate.value] >= start_date) & (df[Nyc311ColumnName.OpenedDate.value] <= end_date)]
    return df

def add_duration_column(df):
    df[OPENED_AT_COLUMN_NAME] = pd.to_datetime(df[OPENED_AT_COLUMN_NAME])
    df[CLOSED_AT_COLUMN_NAME] = pd.to_datetime(df[CLOSED_AT_COLUMN_NAME])
    df[DURATION_COLUMN_NAME] = df[CLOSED_AT_COLUMN_NAME] - df[OPENED_AT_COLUMN_NAME]
    df[DURATION_COLUMN_NAME] = df[DURATION_COLUMN_NAME].dt.total_seconds() / 60 / 60
    return df

def aggregate_data(df):
    df = df.groupby([INCIDENT_ZIP, OPENED_AT_COLUMN_NAME]).agg({DURATION_COLUMN_NAME: "mean"})
    return df

# Main Function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="A csv containing NYC 311 data")
    parser.add_argument("-s", "--start_date", required=True, help="Start date for filtering data")
    parser.add_argument("-e", "--end_date", required=True, help="End date for filtering data")
    parser.add_argument("-o", "--output", help="The output file to write to", default="stdout")

    args = parser.parse_args()
    df = load_and_filter_data(args.file, args.start_date, args.end_date)
    df = add_duration_column(df)
    df = aggregate_data(df)

    if args.output != "stdout":
        df.to_csv(args.output)
    else:
        print(df.to_csv(index=False))

if __name__ == "__main__":
    main()
