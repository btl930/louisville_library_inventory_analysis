# LFPL Inventory Analysis

This project explores inventory data for the Louisville Free Public Library. It demonstrates data cleaning, exploratory analysis, and visualizations using Python, Pandas, Matplotlib, Seaborn, and Geopandas. The goal of this project is to determine if there are areas underserved by the LFPL or to see if any library branches stand out with regard to a particular service.

## How to Use

### 1. Clone the Repository and Handle Large File Downloads:
#### Git LFS setup (if not installed):
Download and install Git LFS: https://git-lfs.github.com
&
run:
```

git lfs install

```
#### Clone the Repository:
``` 

git clone https://github.com/btl930/louisville_library_inventory_analysis.git
cd louisville_library_inventory_analysis

``` 
### 2. Create and Activate a Virtual Environment:
#### Windows (Powershell)
```python

python -m venv venv
./venv/Scripts/activate

```
#### macOS/Linux
```python

python3 -m venv venv
source venv/bin/activate

```
##### To Deactivate:
```python

deactivate

```
#### Install Dependencies:  
```python

pip install -r requirements.txt

```
### 3. Run the Project
```python

jupyter notebook

```
or
```python

jupyter lab

```

## Objectives

1. How is the collection as a whole distributed across the branches of the library?
2. When considered with geographic location, which library branch has the largest or smallest collection for their surrounding area? Are some library branches supporting larger geographical areas than others? Are there areas in Louisville that are more in need of a library branch?
3. How do items in the collection differ (genre, age-category, etc.) among the branches and in the library as a whole?

## Continuing Questions

1. Is there a dataframe with LFPL's circulation data? Is there an API available to get the most current information?
2. What is the current population data of Louisville? Are there maps showing more populated vs less populated areas that would be helpful in continuing to look into Objective #2?
3. How do the percentages of item types between each branch compare?
4. How does the LFPL collection compare to another city of comparable size and population?
5. How does the percentage of ebooks in LFPL compare to other libraries? 

## Conclusions

1. The majority of the collection is housed at the Main branch, which makes sense as it is the oldest branch, houses the majority of electronic items, and serves a more archival role than the other branches.
2. The majority of the branches with smaller collections are located on the West side of Louisville; however, there are more library branches centered there. The library branch that likely serves the largest area with the smallest collection is either Fairdale or Middletown. Please note, however, that these findings are based on collection size and geographic proximity and do not account for population density.
3. The Main, Northeast, and South Central branches have the highest concentration of children's books. The Northeast branch has the highest diversity of genres among those books.
4. The South Central, Southwest, Northeast, Shawnee, and Main branches have the highest concentration of teen books with South Central and Southwest having the highest diversity of genres.
5. The Main branch has the highest concentration of adult books. Within this, the Main branch also has the highest amount of government documents and Kentucky history books showcasing its use as an archive.
6. The adult non-fiction genre has a higher count than fiction.

## Data Sources

#### Louisville Free Public Library Inventory Data:
Source: https://louisville-metro-opendata-lojic.hub.arcgis.com/datasets/LOJIC::louisville-metro-ky-library-collection-inventory-/explore

Description: This is a CSV file of LFPL's collection inventory that is updated regularly. It includes titles, authors, ISBNs, publication years, and price of items in a variety of collections and locations.

Author: Louisville Free Public Library

#### Jefferson County, KY Zip Code Data:
Source: https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2020&layergroup=ZIP%20Code%20Tabulation%20Areas

Description: These are shapefiles of the US ZIP Code Tabulation Areas based on the most recent data from 2020. This data was filtered to only the zip codes of the LFPL branches.

Author: US Census Bureau, Geography Division

## Author

Brittany Loder – Data Analyst



