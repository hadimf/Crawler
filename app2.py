from colorful_logging import c_print
from writeInDb import WriteInDb
from Operating import Operating
from ReadFiles import Read
from Create import Create

c_print("Start!", "red")

dbName = "links2.db"
dbNameData = "data2.db"
tableName = "table"
path = r'C:\Users\Hadi\PycharmProjects\crawel\images'

# Create Table for Links
c_print("Create Table for Links ....", "red")
Create.createTableLinks(dbName, tableName)
c_print("Create Table For Links Is Done!", "red")

# # Get Links
c_print("Get All Links ...", "yellow")
links = Operating.get_links()
total_links = Operating.get_all_total()
c_print("Get All Links Is Done", "green")

# # Write in DB Links
c_print("Writing Links In DataBase...", "yellow")
for link in total_links:
    WriteInDb.writingInDbLinksByLink(dbName, tableName, link)
for link in links:
    WriteInDb.writingInDbLinksByLink(dbName, tableName, link)
c_print("Writing Links In DataBase Is Done", "green")

# Read From LinksTable
c_print("Reading Links From DataBase...", "yellow")
read_links = Read.getLinksFromTable(dbName, tableName)
c_print("Reading Links From DataBase Is Done!", "green")

# Create table for Data
c_print("Creating Table for Data...", "yellow")
Create.createTableData(dbNameData, tableName)
c_print("Creating Table for Data is Done", "green")

# write in DataBase Data
c_print("Writing Data in DataBase Data ...", "yellow")

for link in read_links:
    WriteInDb.writingInDbPerLink(dbNameData, tableName, path, link)
c_print("Writing Data in DataBase Data Is Done", "green")
