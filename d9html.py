from flask import Flask
import json
import MySQLdb

db=MySQLdb.connect('localhost','impk','Littleboy0@','WEATHER')
c=db.cursor()
c.execute('select * from WEATHER limit 100')
a = c.fetchall()
db.close
app=Flask(__name__)
<<<<<<< HEAD
@app.route('/') # defining route --- @app.route('/home') goes to home page
=======
@app.route('/')  # sets path --- @app.route ('/home ') goes to home page
>>>>>>> a0c27676b9c476cdd673dae63d15770ab1789a30
def hello_world():
	rtn = ''
	h=0;
	l=999;
	for i in a:
		rtn = rtn+'<tr>'
		for x in range(5):
			rtn = rtn + '<td> '+str(i[x])+'</td>'
		rtn = rtn + '</tr>'
	grph=''
	for i in range(10):
		num=0
		if a[i][1]==0:
			num=2
		else:
			num=4*a[i][1]+10
		grph=grph+'<div class="di" style="height: '+str(num)+'px; margin-top: '+str(240-(num))+'px;">'+str(a[i][1])+'% </div>'
	
	print(rtn)
	return '<html><style type="text/css"> .di{ width: 50px; padding: -5px; margin-left: 20px; text-align: center; background-color: rgb(100,110,255); color: white	} </style><body style="display: float"> <table border=1 style="float: left; width: 25%;"> <tr> <th>id</th><th>temp</th><th>humi</th><th>press</th><th>temp(f)</th></tr> '+rtn+' </table> <div style="float: right; display: flex; width: 75%; height: 230px">'+grph+' </div> </body> </html>'

if __name__=='__main__':
	app.run(debug=True)
