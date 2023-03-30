# %%
import pandas as pd
import time
from datetime import datetime
import re
from pathlib import Path


# %%
def convert_time(t):
    dt = datetime.strptime(" ".join(t.split()[1:5]), "%b %d %Y %H:%M:%S")
    return round(time.mktime(dt.timetuple()))


# %%
def save_file(bm, filename="bookmarks.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bm)


# %%
def process_bookmark(bookmark: dict) -> str:
    _bm = ""
    btitle = bookmark["title"]
    btitle = re.sub("http[s]?://.*", "", btitle)
    _bm += f"""<DT><A HREF="{bookmark['url']}" ADD_DATE="{convert_time(bookmark['dateCreated'])}">{btitle}</A>\n"""

    return _bm


# %%
def process_stack(stack: list):
    _bm = ""
    for bookmark in stack:
        _bm += process_bookmark(bookmark)

    return _bm


# %%
def process_tabs(tabs: list) -> str:
    # title = tabs
    _bm = ""
    for tab in tabs:
        if tab == []:
            continue
        try:
            is_stacked = bool(tab["isStacked"])
        except KeyError:
            is_stacked = False
            _bm += process_bookmark(tab)
            # TODO: process other types of entries.

        if is_stacked:
            # print(tab)
            try:
                tab_title = "stack: " + tab["title"]
            except KeyError:
                tab_title = "stack: " + "Untitled"

            _bm += f"""<DT><H3 ADD_DATE="{convert_time(tab['dateCreated'])}" >{tab_title}</H3>\n"""
            # _bm += f"""<DT><H3>{tab_title}</H3>"""

            _bm += "<DL><p>\n"
            _bm += process_stack(tab["stackedItems"])
            _bm += "</DL><p>\n"

    return _bm


# %%
def process_df(df):
    bm = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>TabExtend Bookmarks</TITLE>
<H1>TabExtend Bookmarks</H1>
<DL><p>
"""

    for cat in df["categoryID"].unique():
        cat_df = df[df["categoryID"] == cat]

        # add the category ID as a "title"
        bm += f"""<DT><H3>CATEGORY ID: {cat}</H3>\n"""
        bm += "<DL><p>\n"

        for index, row in cat_df.iterrows():
            rtitle = row["title"]  # ["TEMP Category ID" + row['categoryID']
            rlast_added = convert_time(row["lastAdded"])

            # add title of table
            bm += f"""<DT><H3 ADD_DATE="{rlast_added}">{rtitle}</H3>\n"""
            bm += "<DL><p>\n"

            # print(tabs)
            bm += process_tabs(row["tabs"])
            bm += "</DL><p>\n"

        bm += "</DL><p>\n"
    bm += "</DL><p>\n</DL><p>\n"

    return bm


# %%
# read from json into a df, use file name: "tabExtend_data_20230328.json"
fname = "tabExtend_data.json"
working_dir = Path()  # current directory
fpath = working_dir / fname

df = pd.read_json(fpath)
df = df.sort_values(by=["categoryID"])

bm = process_df(df)
save_file(bm)

# %%
