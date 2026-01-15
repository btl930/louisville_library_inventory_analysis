# LFPL Inventory Analysis

___

This project explores inventory data for the Louisville Free Public Library. It demonstrates data cleaning, exploratory analysis, and visualizations using Python, Pandas, Matplotlib, Seaborn, and Geopandas. The goal of this project is to determine if there are areas underserved by the LFPL or to see if any library branches stand out in regards to a particular service.

## How to Use

___

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
#### macOS/Linux
```python

python3 -m venv venv
source venv/bin/activate

```
##### Deactivate
```python

deactivate

```
### Install Dependencies:  
```python

pip install -r requirements.txt

```
### Run the Project
```python

jupyter notebook

```
or
```python

jupyter lab

```

## Objectives

___

1. How is the collection as a whole distributed across the branches of the library?
2. When considered with geographic location, which library branch has the largest or smallest collection for their surrounding area? Are some library branches supporting larger geographical areas than others? Are there areas in Louisville that are more in need of a library branch?
3. How do items in the collection differ (genre, item-type, age-category, etc.) among the branches and in the library as a whole?

## Continuing Questions

___

1. Is there a dataframe with LFPL's circulation data? Is there an API available to get the most current information?
2. What is the current population data of Louisville? Are there maps showing more populated vs less populated areas that would be helpful in continuing to look into Objective #2?

## Conclusion

___

1. The majority of the collection is housed at the Main Branch, which makes sense as it is the oldest branch, houses the majority of electronic items, and serves a more archival role than the other branches.
2. 

## Data Sources

___

#### Louisville Free Public Library Inventory Data:
Source: https://louisville-metro-opendata-lojic.hub.arcgis.com/datasets/LOJIC::louisville-metro-ky-library-collection-inventory-/explore

Description: This is a dataframe of LFPL's collection inventory that is updated on a monthly basis. It includes titles, authors, ISBNs, publication years, and price of items in a variety of collections and locations.

Author: Louisville Free Public Library

#### Jefferson County, KY Zip Code Data:
Source: https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2020&layergroup=ZIP%20Code%20Tabulation%20Areas

Description: This is a dataframe of the US ZIP Code Tabulation Areas based on the most recent data from 2020.

Author: US Census Bureau, Geography Division

## Author

___

Brittany Loder – Data Analyst



