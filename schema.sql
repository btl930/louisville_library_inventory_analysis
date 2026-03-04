CREATE TABLE louisville_zipcodes (
    zipcode TEXT PRIMARY KEY
);
CREATE TABLE libraries (
    library_id INT PRIMARY KEY,
    library_name TEXT, 
    latitude REAL,
    longitude REAL,
    zipcode TEXT,
    FOREIGN KEY (zipcode) REFERENCES louisville_zipcodes(zipcode)
);
CREATE TABLE library_item_details(
    item_id INT PRIMARY KEY,
    title TEXT,
    item_type TEXT,
    item_collection TEXT,
    item_location TEXT,
    item_price INT
);
CREATE TABLE library_inventory (
    library_id INT NOT NULL,
    item_id INT NOT NULL,
    PRIMARY KEY (library_id, item_id),
    FOREIGN KEY (library_id) REFERENCES libraries(library_id),
    FOREIGN KEY (item_id) REFERENCES library_item_details(item_id)
);
CREATE TABLE oss_households (
    household_id INT PRIMARY KEY,
    date_added TEXT,
    household_type TEXT,
    household_size INT,
    annual_income BIGINT,
    zipcode TEXT,
    FOREIGN KEY (zipcode) REFERENCES louisville_zipcodes(zipcode)
);
