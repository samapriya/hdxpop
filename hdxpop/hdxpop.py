#!/usr/bin/python
# -*- coding: utf-8 -*-

__copyright__ = """

    Copyright 2020 Samapriya Roy

    Permission is hereby granted, free of charge,
    to any person obtaining a copy of this software
    and associated documentation files (the Software"),
    to deal in the Software without restriction,
    including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons
    to whom the Software is furnished to do so,
    subject to the following conditions:

    MIT LICENSE: https://opensource.org/licenses/MIT

    The above copyright notice and this permission notice shall
    be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
    OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
__license__ = "Apache 2.0"


import os.path
import argparse
import sys
import zipfile
import os
import time
import requests
import json
import os
import sys
import glob
from bs4 import BeautifulSoup

MAIN_URL = "https://data.humdata.org/organization/facebook?res_format=ZIP&res_format=zipped%20geotif&res_format=zipped%20geotiff&res_format=zipped%20goetiff&q=&ext_page_size=250"


i = 1  # Set a counter


def downonly(url, destination):
    """[Downloader to check and download imagery]

    [This looks for the availability of the files,checks for existing files and downloadeds the
    necessary files]
    """
    global i
    filenames = glob.glob1(destination, "*")
    filenames = [os.path.join(destination, files) for files in filenames]

    # Get filename from URL Head
    r = requests.head(url)
    fname = r.headers["Location"].split("?")[0].split("/")[-1]
    local_path = os.path.join(destination, fname)
    if not local_path in filenames:
        r = requests.get(url)
        print("Processing: " + str(i) + " downloading to==> " + local_path)
        if r.status_code == 200:
            i = i + 1
            f = open(local_path, "wb")
            for chunk in r.iter_content(chunk_size=512 * 1024):
                if chunk:
                    f.write(chunk)
            f.close()
    else:
        print("Existing file Skipping: " + local_path)


lt = []
sub = []


def lk(url, destination):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.select("a")
    for link in links:
        try:
            ziplink = link.get("href")
            if ziplink.split("/")[-1].startswith("population") and not ziplink.split(
                "/"
            )[-1].endswith("csv.zip"):
                sub.append(ziplink)
                url = "https://data.humdata.org" + ziplink
                downonly(url, destination)
        except Exception as e:
            pass


def humdata(destination):
    try:
        page = requests.get(MAIN_URL)
        soup = BeautifulSoup(page.content, "html.parser")
        links = soup.select("a")
        for link in links:
            try:
                url = link.get("href")
                if url.startswith("/dataset"):
                    lt.append("https://data.humdata.org" + url)
            except Exception as e:
                pass
        for locations in set(lt):
            lk(locations, destination)
        print("Processed total of : " + str(len(sub)) + " links")
    except Exception as e:
        print(e)
    except (KeyboardInterrupt, SystemExit) as e:
        print("Program escaped by User")
        sys.exit()


def humdata_from_parser(args):
    humdata(destination=args.folder)


def unzip(initial, final):
    """Unzip files and moves them into a folder"""
    for root, dirs, files in os.walk(initial):
        for i in files:
            if i.endswith(".zip"):
                fullpath = os.path.join(root, i)
                zip_ref = zipfile.ZipFile(fullpath)  # create zipfile object
                for file in zip_ref.namelist():
                    if zip_ref.getinfo(file).filename.endswith(
                        ".tif"
                    ) and not os.path.exists(
                        os.path.join(final, zip_ref.getinfo(file).filename)
                    ):
                        print("Extracting: " + str(zip_ref.getinfo(file).filename))
                        zip_ref.extract(file, final)
                    elif zip_ref.getinfo(file).filename.endswith(
                        ".tif"
                    ) and os.path.exists(
                        os.path.join(final, zip_ref.getinfo(file).filename)
                    ):
                        print(
                            "Existing file Skipped: "
                            + str(zip_ref.getinfo(file).filename)
                        )


def unzip_from_parser(args):
    unzip(initial=args.initial, final=args.final)


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Simple tool to download High Resolution Population Density Maps from HDX"
    )
    subparsers = parser.add_subparsers()
    parser_humdata = subparsers.add_parser(
        "humdata", help="Download High Resolution Population Density Maps from HDX"
    )
    parser_humdata.add_argument("--folder", help="Folder to store results")
    parser_humdata.set_defaults(func=humdata_from_parser)

    parser_unzip = subparsers.add_parser("unzip", help="Unzip downloaded HDX files")
    parser_unzip.add_argument("--initial", help="Folder with zipped files")
    parser_unzip.add_argument("--final", help="Foler with unzipped tif files")
    parser_unzip.set_defaults(func=unzip_from_parser)

    args = parser.parse_args()

    args.func(args)


if __name__ == "__main__":
    main()
