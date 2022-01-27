from pyhive import hive


conn = hive.Connection(host="localhost", port=10000,database= "default")
if conn:
    print("Succesfull connection!!!!")
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
for result in cursor.fetchall():
    print(result)