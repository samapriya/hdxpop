# hdxpop

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3735435.svg)](https://doi.org/10.5281/zenodo.3735435)
[![Downloads](https://pepy.tech/badge/hdxpop/month)](https://pepy.tech/project/hdxpop/month)
[![Build status](https://ci.appveyor.com/api/projects/status/8acj7x6fcmecouj0?svg=true)](https://ci.appveyor.com/project/samapriya/hdxpop)

Simple tool to download High Resolution Population Density Maps from Humanitarian Data Exchange

## [For usage go to the medium article](https://medium.com/@samapriyaroy/community-datasets-in-google-earth-engine-an-experiment-b72daa474819)

```
Samapriya Roy. (2020, March 31). samapriya/hdxpop: hdxpop: Simple tool to download High Resolution Population Density Maps from
Humanitarian Data Exchange (Version 0.0.3). Zenodo. http://doi.org/10.5281/zenodo.3735435
```

## Table of contents
* [Prerequisites](#prerequisites)
* [Installing hdxpop](#installing-hdxpop)
* [Using without install](#using-without-install)

## Prerequisites
This assumes that you have native python & pip installed in your system, you can test this by going to the terminal (or windows command prompt) and trying. I recommend installation within virtual environment if you are worries about messing up your current environment.

```python``` and then ```pip list```

If you get no errors and you have python 3.2 or higher you should be good to go.

## Installing hdxpop
Once you have determined you have python, you can simply install hdxpop using two methods

```
pip install hdxpop
```

For linux I found it helps to specify the pip type and use --user. Here pip refers to your default python and pip installations, assumption here is you are using python3 and up.

```
pip install hdxpop --user

or

pip3 install porder --user
```

or you can also try

```
git clone https://github.com/samapriya/hdxpop.git
cd hdxpop
python setup.py install
```

![hdxpop](https://user-images.githubusercontent.com/6677629/75043238-be6a9780-548d-11ea-9b3e-d7a4824ca8fc.png)


## Using without install
You can do this too,by simply going downloading and unzipping the repo onto your machine and migrating to the innner hdxpop folder with the hdxpop.py file.

you can then do a

```
python3 hdxpop.py -h
```

or simply if you have Git enabled

```
git clone https://github.com/samapriya/hdxpop.git
cd hdxpop/hdxpop/
python hdxpop.py -h
```

## Changelog

### v0.0.3
- Changes to search URL to include geotif, zipped only, goetiff and geotiff keyword filters.

### v0.0.2
- Added installation instructions and setup
