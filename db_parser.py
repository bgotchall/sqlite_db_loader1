import sqlite3
from employee import Employee


conn = sqlite3.connect('sample.db')

c= conn.cursor()
#c.execute("DROP TABLE employees")

#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            pay integer
#            )""")

emp_1=Employee("John", "Doe", 80000)
emp_2=Employee("Jane", "Doe", 90000)

print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)


#c.execute("INSERT INTO employees VALUES (:first,:last, :pay)",{'first':emp_1.first,'last':emp_1.last,'pay':emp_1.pay})
#conn.commit()

c.execute("SELECT * FROM employees WHERE last='Doe'")

print(c.fetchall())


conn.commit()






conn.close()



print("hi")