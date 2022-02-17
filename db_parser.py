import sqlite3
import json
import pandas as pd
from employee import Employee

   
# Opening JSON file
f = open('data/AthenaC_setup_20Aug2021_AAA_082321_CORR___20210902130347.json',)  #note that this still requires quick edit to export the json.
   
# returns JSON object as 
# a dictionary
#data = json.load(f)
   

df=pd.read_json('data/AthenaC_setup_20Aug2021_AAA_082321_CORR___20210902130347.json')

print(df.head(100))
print(df.tail(100))

print(df['hand_id'])

# Iterating through the json
# list
# for i in data:
#     print(i)
   
# Closing file
#f.close()





# conn = sqlite3.connect('sample.db')

# c= conn.cursor()
# #c.execute("DROP TABLE employees")

# #c.execute("""CREATE TABLE employees (
# #            first text,
# #            last text,
# #            pay integer
# #            )""")

# emp_1=Employee("John", "Doe", 80000)
# emp_2=Employee("Jane", "Doe", 90000)

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)


# #c.execute("INSERT INTO employees VALUES (:first,:last, :pay)",{'first':emp_1.first,'last':emp_1.last,'pay':emp_1.pay})
# #conn.commit()

# c.execute("SELECT * FROM employees WHERE last='Doe'")

# print(c.fetchall())

# conn.commit()

# conn.close()
