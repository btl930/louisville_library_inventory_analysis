# LFPL Inventory Analysis

This project explores inventory data for the Louisville Free Public Library. It demonstrates data cleaning, exploratory analysis, and visualization in Python.

## How to Use
### 1. Clone the Repository:
```python 

git clone https://github.com/btl930/louisville_library_inventory_analysis.git
cd louisville_library_inventory_analysis

``` 
### 2. Handle Large Files:
This repository uses Git LFS to manage large datasets. When you clone this repository, Git will download pointer files instead of the actual data. To download the real files, run:
```python

git lfs pull

```
#### Git LFS setup (if not installed):
Download and install Git LFS: https://git-lfs.github.com
&
run:
```python

git lfs install
git lfs pull

```
### 3. Create and Activate a Virtual Environment:
#### Windows (Powershell)
```python

python -m venv venv
./venv/Scripts/activate

```
##### Deactivate
```python

deactivate

```

___

#### macOS/Linux
```python

python3 -m venv venv
source venv/bin/activate

```
##### Deactivate
```python

deactivate

```

___

### Install Dependencies:  
```python

pip install -r requirements.txt

```

___

### Run the Project
```python

jupyter notebook

```
or
```python

jupyter lab

```

## Data Sources
#### Louisville Free Public Library Inventory Data:
Author: Louisville Free Public Library

Description: This is a dataframe of LFPL's collection inventory that is updated on a monthly basis. It includes titles, authors, ISBNs, publication years, and price of items in a variety of collections and locations.

Source: https://louisville-metro-opendata-lojic.hub.arcgis.com/datasets/LOJIC::louisville-metro-ky-library-collection-inventory-/explore

___

#### Jefferson County, KY Zip Code Data:
Author: US Census Bureau, Geography Division

Description: This is a dataframe of the US ZIP Code Tabulation Areas based on the most recent data from 2020.

Source: https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2020&layergroup=ZIP%20Code%20Tabulation%20Areas


## Author
Brittany Loder – Data Analyst



