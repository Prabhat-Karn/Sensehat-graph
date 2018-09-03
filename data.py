import MySQLdb
import random
def dataUsed():
        a=0;
        b=0;
        c=0;
        try:
                try:
                        print("searching for sensehat")
                        from sense_hat import SenseHat
                        print("sensehat found")
                except ImportError:
                        raise ImportError('Sense hat not found, trying emulator')
                        from sense_emu import SenseHat
               
                        a = str(int(s.get_temperature()))
                        b = str(int(s.get_pressure()))
                        c = str(int(s.get_humidity()))
                
        except ImportError:
                raise ImportError('emulator not found either, creating random data')
                
                a=random.randint(0,30)
                b=random.randint(50,100)
                c=random.randint(50,100)

        return (a,b,c)

db=MySQLdb.connect('localhost','impk','Littleboy0@','WEATHER')
cursor=db.cursor()
cursor.execute('DROP TABLE IF EXISTS WEATHER')  #comment this to retain previous data
sqlCreate='CREATE TABLE IF NOT EXISTS WEATHER(ID INT PRIMARY KEY AUTO_INCREMENT , TempInCelcius INT, Pressure INT, Humid INT)'
cursor.execute(sqlCreate)
for x in range(100):
	(a,b,c) = dataUsed()
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
def showTable():
	cursor.execute("select * from WEATHER LIMIT 100")
	ret=cursor.fetchall()
	for i in ret:
		print('SN: '+str(i[0])+" TempInCelcius: "+str(i[1])+" Pressure: "+str(i[2])+" Humid: "+str(i[3])+' TempInF: '+str(i[4]))

#showTable()  #uncomment this to show table in terminal
db.close()

