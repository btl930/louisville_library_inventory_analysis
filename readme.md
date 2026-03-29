# An Evaluation of the Louisville Free Public Library Inventory Coverage in High-Need Areas

This project analyzes the distribution of the Louisville Free Public Library inventory as a whole and within its individual branches. The goal is to determine if there are areas underserved in regards to library branch locations or collections; in addition, the evaluation may also highlight library branches that stand out with regard to a particular service. The outcomes may provide insight for the city of Louisville and the library system in determining the allocation of new products or next steps in expanding the branch locations.

## How to Use

### 1. Clone the Repository and Set Up Git LFS:
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

```
python -m venv venv
.\venv\Scripts\activate
```

#### macOS/Linux

```
python3 -m venv venv
source venv/bin/activate
```

#### To Deactivate:

```
deactivate
```

#### Install Dependencies:  

```
pip install -r requirements.txt
```

### 3. Rebuild Database
```
sqlite3 database.db < schema.sql
python load_data.py 
```

### 4. Run the Project

##### Option A: VS Code (Recommended)
Make sure Jupyter extension is installed:

```
code .
```

##### Option B: Jupyter Notebook:

```
jupyter notebook
```

##### Run LFPL_ANALYSIS notebook


## Objectives

1. When considering geographic location, how do library branch distributions align with regions in need?

2. How are item types and collections distributed across the library as a whole and within each individual branch? 

## Analysis

Louisville is not unique in that there are those in the community needing extra support and resources. The Office of Social Services can provide many resources to those who apply, but it also helpful to evaluate other ways one can get much needed resources. One's local library can be a major resource in a fast-moving and expensive society. Several LFPL branches-including Shawnee, Portland, and Shively-serve communities with the highest amount of OSS Households. Below are conclusions found from analyzing data regarding the LFPL and OSS Household Demographics:

- The LFPL branch distribution correlates well to zipcodes holding OSS Households. 
- While many of the LFPL branches serving the highest concentration of OSS Households have smaller collections, the Main branch with the largest collection supports the area as well. (Note: the Main branch is currently closed to renovations)
- The majority of the collection is housed at the Main branch, which makes sense as it is the oldest branch, houses the majority of electronic items, and serves a more archival role than the other branches.
- The Northeast, South Central, and Southwest branches have the largest collections (excluding Main). The Northeast and Southwest branches serve larger geographic regions with a smaller concentration of library branches. South Central has a bit more library branches in its area (with a new Fern Creek branch opening in 2026) but still serves a large geographic region.
- OSS Households in the Southwest portion of Jefferson County may have more resources at the South Central and Southwest branches, which hold large collections of adult, teen, and children's books.
- OSS Households in the Northwest portion of Jefferson County may have more resources at the Iroquois branch for adult books, the Shawnee branch for teen books, and either Iroquois or Shawnee for children's books. In addition, the Main branch holds large collections for adult, teen, and children's books.
- While requiring access to the internet, the Ebooks and other electronic options could be a helpful resource to OSS Household.
- Please note, that these findings are based on collection size and geographic proximity and do not account for population density.

## Continuing Questions

1. Is there a dataframe with LFPL's circulation data? Is there an API available to get the most current information to see how each branch's collection is being used?
2. How do the percentages of item types between each branch compare?
3. How has the LFPL collection changed over time?
4. How have electronic resources changed over time?
5. How does the LFPL collection compare to another city of comparable size and population?
6. How does the percentage of electronic resources in LFPL compare to other libraries? 

## Data Sources

### Louisville Free Public Library Inventory Data:
Source: https://louisville-metro-opendata-lojic.hub.arcgis.com/datasets/LOJIC::louisville-metro-ky-library-collection-inventory-/explore

Description: This is a CSV file of LFPL's collection inventory that is updated regularly. Fields used are Title, ItemType, ItemCollection, ItemLocation, and ItemPrice.

Author: Louisville Free Public Library

### OSS Households Demographics
Source: https://data.louisvilleky.gov/datasets/LOJIC::oss-households-demographics/explorehttps://data.louisvilleky.gov/datasets/LOJIC::oss-households-demographics/explore

Description: This is a CSV file containing the demographics of households that applied for services through the Office of Social Services in Jefferson County, KY. Fields used are Date_Added, Household_Type, Household_Size, Annual_Income, and Zip_Code.

Author: Louisville Metro Open Data

### Louisville KY Free Public Libraries
Source: https://data.louisvilleky.gov/datasets/LOJIC::louisville-ky-free-public-libraries-1/about

Description: This includes CSV and SHP files regarding the geographic locations of LFPL branches. Fields used are LFPL_NAME, LFPL_LOC, LATITUDE, LONGITUDE, X, and Y.

Author: Louisville Metro Open Data

### Jefferson County, KY Zip Codes:
Source: https://data.louisvilleky.gov/datasets/LOJIC::jefferson-county-ky-zip-codes/about

Description: This includes CSV and SHP files regarding the zip code boundaries of Jefferson County, KY. Fields used are Zipcodes, SHAPEAREA, and SHAPELEN.

Author: Louisville Metro Open Data

## Acknowledgement of Tools and Assistance

This project was developed using Python, SQL, and Jupyter Notebooks. Python Libraries such as pandas, Matplotlib, Seaborn and GeoPandas were utilized to analyze the data. SQLite was used to create the relational database supporting the analysis.

ChatGPT was used as a supplementary tool for troubleshooting and debugging. All code and results were reviewed, validated, and implemented independently.

## Author

Brittany Loder – Data Analyst



