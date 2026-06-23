import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)
mycursor = mydb.cursor()
#Insertar registro para poder actualizar
sql_insert = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val_insert = ("Peter", "Valley 345")
mycursor.execute(sql_insert, val_insert)
mydb.commit()

#Actualizar registro
sql_update = "UPDATE customers SET address = 'Cayon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql_update)
mydb.commit()   

print(mycursor.rowcount, "registro(s) actualizado(s).")
