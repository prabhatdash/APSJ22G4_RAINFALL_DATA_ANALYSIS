import mysql.connector as mc
try:
    dbc = mc.connect(host="localhost",user="root",passwd="root",database="inventory")
    cursor=dbc.cursor()
except Exception as e:
    print(e)