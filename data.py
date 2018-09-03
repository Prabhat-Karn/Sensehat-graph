import MySQLdb
import random
db=MySQLdb.connect('localhost','impk','Littleboy0@','WEATHER')
cursor=db.cursor()
sqlCreate='CREATE TABLE IF NOT EXISTS WEATHER(ID INT PRIMARY KEY AUTO_INCREMENT , TempInCelcius INT, Pressure INT, Humid INT)'
#cursor.execute('DROP TABLE IF EXISTS WEATHER')
cursor.execute(sqlCreate)
for x in range(100):
	a=random.randint(0,30)
	b=random.randint(50,100)
	c=random.randint(50,100)
	sqlInsert='INSERT INTO WEATHER(TempInCelcius, Pressure, Humid) VALUES (%d,%d,%d)'%(a,b,c)
	cursor.execute(sqlInsert)
	try:
		sqlAlter='ALTER TABLE WEATHER ADD COLUMN IF NOT EXISTS TempInF FLOAT'
		cursor.execute(sqlAlter)
		sqlUpdate='UPDATE WEATHER SET TempInF=TempInCelcius*1.8+32' 
		cursor.execute(sqlUpdate)
	except:
		sqlUpdate='UPDATE WEATHER SET TempInF=TempInCelcius*1.8+32' 
		cursor.execute(sqlUpdate)
		db.commit()

	cursor.execute("select * from WEATHER LIMIT 100")# aaba run gara taw
	a=cursor.fetchall()
	for i in a:
		print('SN: '+str(i[0])+" TempInCelcius: "+str(i[1])+" Pressure: "+str(i[2])+" Humid: "+str(i[3])+' TempInF: '+str(i[4]))
db.close()

'''data=cursor.fetchone()
print(data)'''	
	