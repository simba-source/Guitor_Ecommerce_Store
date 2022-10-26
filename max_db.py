# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="final-db-205.cwokmtfympzg.us-east-1.rds.amazonaws.com",
#   user="admin205",
#   password="software",
#   database="mktdata"
# )
#
# cur = mydb.cursor()
#
# cur.execute("DROP TABLE guitar")
# cur.execute("CREATE TABLE guitar(ID INT, Name VARCHAR(150), Price DECIMAL(7, 2))")
# cur.execute("INSERT INTO guitar VALUES (123, 'Fender Strat', 499.99)")
# cur.execute("SELECT * FROM guitar")
#
# res = cur.fetchall()
#
# mydb.commit()
#
# print(res)