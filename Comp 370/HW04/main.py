import json
from pathlib import Path
from random import random
import pandas as pd
from bokeh.layouts import column
from bokeh.models import Button, ColumnDataSource, Dropdown
from bokeh.plotting import figure, curdoc

# global data
zipcodes = None
nyc311_df = None
fig_data = ColumnDataSource(data=dict(month=[], all_zips=[], zip1=[], zip2=[]))

all_zips_data = None

zip1 = None
zip2 = None

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

MONTH_COLUMN_NAME = "month"
ZIP1_COLUMN_NAME = "zip1"
ZIP2_COLUMN_NAME = "zip2"
ALLZIPS_COLUMN_NAME = "allzips"

INCIDENT_ZIP = "Incident Zip"
OPENED_AT_COLUMN_NAME = "Created Date"
CLOSED_AT_COLUMN_NAME = "Closed Date"
DURATION_COLUMN_NAME = "Duration"


def get_dataset_path(fname: str) -> Path:
    return Path(__file__).parent / fname


def load_data():
    global nyc311_df, zipcodes, zip1, zip2, all_zips_data

    nyc311_df = pd.read_csv(get_dataset_path("nyc_311_limit.app.2020.duration.csv"))

    # Populate zipcodes
    zipcodes = [str(int(x)) for x in nyc311_df[INCIDENT_ZIP].unique().tolist()]
    zipcodes = list(filter(lambda x: len(x) != 5, zipcodes))

    # Set the allzips data
    all_zips_df = nyc311_df.groupby([OPENED_AT_COLUMN_NAME]).agg(
        {DURATION_COLUMN_NAME: "mean"}
    )
    print(all_zips_df.head())
    all_zips_data = [
        all_zips_df.loc[all_zips_df[OPENED_AT_COLUMN_NAME] == month][
            DURATION_COLUMN_NAME
        ]
        for month in range(1, 13)
    ]

    zip1 = zipcodes[0]
    zip2 = zipcodes[1]


def build_zipcode_column_data(zip1, zip2) -> dict:
    return {
        MONTH_COLUMN_NAME: months,
        ZIP1_COLUMN_NAME: [random() for _ in months],
        ZIP2_COLUMN_NAME: [random() for _ in months],
        ALLZIPS_COLUMN_NAME: all_zips_data,
    }


def update_zip1(event):
    global zip1, zip2

    zip1 = event.item
    fig_data.data = build_zipcode_column_data(zip1=zip1, zip2=zip2)


def update_zip2(event):
    global zip1, zip2

    zip2 = event.item
    fig_data.data = build_zipcode_column_data(zip1=zip1, zip2=zip2)


def main():
    global fig_data, zipcodes

    # load the data
    load_data()

    # setup the dashboard data
    fig_data.data = build_zipcode_column_data(zip1="10001", zip2="10002")

    # setup the dashboard
    print("Setting up figure")

    p = figure(x_range=months, height=500)
    p.line(x=MONTH_COLUMN_NAME, top=ZIP1_COLUMN_NAME, source=fig_data, color="red")
    p.line(x=MONTH_COLUMN_NAME, top=ZIP2_COLUMN_NAME, source=fig_data, color="green")

    print("Setting up dropdowns")
    zip1_dropdown = Dropdown(label="Zip1", menu=[])
    zip1_dropdown.on_event("menu_item_click", update_zip1)

    zip2_dropdown = Dropdown(label="Zip2", menu=[])
    zip2_dropdown.on_event("menu_item_click", update_zip2)

    print("Adding to curdoc")
    doc = curdoc()
    doc.add_root(column(p, zip1_dropdown, zip2_dropdown))


main()
