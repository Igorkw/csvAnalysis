# Step 1 - Run all files from the database folder
import os #deal with files and folders
import pandas as pd #deal with databases
import plotly.express as px #create graphics


file_list = os.listdir("/your-directory")
print(file_list)

total_table = pd.DataFrame() #create a empty table

# Step 2 - Import selling databases
for file in file_list:
  if "sales" in file.lower():
    tfile = f"/your-directory/{file}"

    #Import file
    table = pd.read_csv(tfile) #choose the type to be read (csv in this case)
    total_table = pd.concat([total_table, table], ignore_index = True) #add each table inside total_table

# Step 3 - treat / compile the databases
display(total_table)

# Step 4 - Calculate the most selling product (in amount)
products_table = total_table.groupby("Product").sum() #group the products

products_table = products_table[["Amount of sells", "Unity price"]].sort_values(by="Amount of sells", ascending=False) #select only the columns I want to calculate
display(products_table)

# Step 5 - Calculate the product that earned the most (in invoicing)
total_table['Invoicing'] = total_table['Amount of sells'] * total_table['Unity price'] #create a table
invoicing_table = total_table.groupby('Product').sum()

invoicing_table = invoicing_table[["Invoicing"]].sort_values(by="Invoicing", ascending=False)
display(invoicing_table)

# Step 6 - Calculate the store/city who sold the most (in invoicing) - create a graphic/dashboard
store_table = total_table.groupby('Store').sum()

store_table = store_table[["Invoicing"]].sort_values(by="Invoicing", ascending=False)
display(store_table)

graphic = px.bar(store_table, x=store_table.index, y='Invoicing')
graphic.show()