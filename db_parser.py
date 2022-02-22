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

#print(df.head(100))
#print(df.tail(100))

#stdf notes:
#PIR starts each new run
#PRR (part result record) ends each run.  it has the serial number of the device (index number that is)

#print(df)
#these are from the jupyter nb, all work to make little tables:
MIRs = df[df["recordType"] == "MIR"]
MIRs[["node_nam","job_nam","exec_ver","stat_num","rtst_cod","prot_cod","lot_id","flow_id","mode_cod","part_typ","setup_t","tstr_typ","exec_typ"]]
#{"recordType":"MIR","node_nam":"D10-2","job_nam":"AthenaC_setup_20Aug2021_AAA_082321","exec_ver":"U4.2.4","stat_num":1,"rtst_cod":"N","prot_cod":" ","lot_id":"CORR","flow_id":"MainFlow_NONSec","mode_cod":" ","part_typ":"AthenaC","burn_tim":0,"setup_t":1630587827,"start_t":1630587827,"tstr_typ":"Fusion_EX","exec_typ":"Unison","cmod_cod":" "},
PIRs = df[df["recordType"] == "PIR"]
PIRs[['site_num','head_num']]

PRRs = df[df["recordType"] == "PRR"]
PRRs[["part_id","soft_bin","hard_bin","site_num","num_test","head_num","x_coord","y_coord","hashCode"]]
#"recordType":"PRR","x_coord":-32768,"soft_bin":6,"part_id":"1","hard_bin":6,"site_num":1,"num_test":1,"head_num":1,"y_coord":-32768,"hashCode":-2277251},

print (PRRs[["part_id","soft_bin","hard_bin","site_num","num_test","head_num","x_coord","y_coord","hashCode"]])



#new_df=pd.DataFrame(2)
#print(new_df)

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
