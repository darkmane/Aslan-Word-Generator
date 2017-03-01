# traveller_data
JSON files meant to allow automation of parts of the Traveller game, like creating alien words.

# Purpose

This project is meant to allow other programmers to write better code while automating Traveller projects.

The complexity of code implementing tables as 4, 5 and 6 clause switch statements can go away. 

With these files you import the right file and then look up the data you need. 

# Contributions
This is a daunting project for a single person, but for a community it could be done very quickly.

Each file has 1 JSON dictionary with 2 elements
## "title"
The title of table 
## "data"
The JSON data. Not all tables are simple matricies. On the page they look like tabular data, but they are logically a collection of small objects, displayed in a tabular for. It is better to group the data logically, rather than by the table.

For example the "Prior Service" table (lbb/b01/14.1.json) could be a series of arrays, 1 for each row but logically it should be a series of objects, 1 for each column.

## Naming convention
Please group the data by generation of Traveller (LBB == original traveller, MT = MegaTraveller and T5 = Traveller 5th ed), then book and page number. If there are multiple tables on a page number them left to right, top to bottom.

eg: lbb/b01/14.1/json
Original Traveller, Book 1 (Characters and Combat), pg 14, table 1 (Prior Service Table)
