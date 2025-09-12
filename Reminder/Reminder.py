import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk
import ctypes
from ctypes import wintypes
from ctypes.wintypes import RECT
import datetime
from calendar import monthrange
import sqlite3 as db
import math
import re
import json
from dateutil.relativedelta import relativedelta



months={
1:"January",
2:"February",
3:"March",
4:"April",
5:"May",
6:"June",
7:"July",
8:"August",
9:"September",
10:"October",
11:"November",
12:"December"
}


rem__=[]
def can2_b1(e):
	global rem__
	global checked
	global user,sel_date





	for i in rem__:

		if i[1]<=can2.canvasy(e.y)<=i[2]:

			with open("data/reminder.json","r") as file:

				data=json.load(file)



			c=data[str(user)][str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2])][i[0]]


			if c==0:
				c=1
			elif c==1:
				c=0




			data[str(user)][str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2])][i[0]]=c


			with open("data/reminder.json","w") as file:

				json.dump(data,file,indent=4)

			main()
			return


profile=0
def can_b1(e):


	global w,h
	global state,state2
	global can 
	global date
	global ar_date
	global sel_date
	global user
	global un,pw,pw2

	global text,can2,can3
	global show,show1,show2
	global rem_ar
	global profile

	global pun,ppw,ppw2
	global prof_show







	if state=="main":

		#profile




		if 500-10-30-20-30<=e.x<=500-10-30-20:
			if 621-30-10<=e.y<=621-30-10+30:

				if profile==0:
					profile=1
					pun.delete(0,tk.END)
					ppw.delete(0,tk.END)
					ppw2.delete(0,tk.END)



					db_user=db.connect("data/user.db")
					cur=db_user.cursor()

					rows=cur.execute("SELECT * FROM user WHERE user_id="+str(user))

					for row in rows:

						_un_=row[1]
						_pw_=row[2]


					pun.insert(tk.END,_un_)
					ppw.insert(tk.END,_pw_)

					prof_show=0



				elif profile==1 or profile==2:
					profile=0
					prof_show=0


				main()


				return


		

		if 551<=e.y<=551+30:

			if 60<=e.x<60+(410-60)/2:


				if profile==1:

					profile=2

					main()

				elif profile==2:


					if pun.get()=="" or ppw.get()=="" or ppw2.get()=="":
						message(can,"Fill all Fields!","#f94449","#ffffff",60+10,551-30-5,410-10,551-5)
						return

					if ppw.get()!=ppw2.get():

						message(can,"Passwords don't match!","#f94449","#ffffff",60+10,551-30-5,410-10,551-5)

						return


					db_user=db.connect("data/user.db")
					cur=db_user.cursor()

					cur.execute("SELECT * FROM user")
					rows=cur.fetchall()

					for row in rows:

						if not row[0]==user:

							if row[1].lower()==pun.get():
								message(can,"Name exists!","#f94449","#ffffff",60+10,551-30-5,410-10,551-5)
								return

					cur.execute("UPDATE user SET user_name='"+str(pun.get())+"',password='"+str(ppw.get())+"' WHERE user_id="+str(user))
					db_user.commit()
					db_user.close()

					profile=0

					main()

			elif 60+(410-60)/2<e.x<=410:





				with open("data/reminder.json","r") as file:

					data=json.load(file)

					try:

						data.pop(str(user))

						with open("data/reminder.json","w") as file:


							json.dump(data,file,indent=4)
					except:
						pass





				db_user=db.connect("data/user.db")
				cur=db_user.cursor()


				cur.execute("DELETE FROM user WHERE user_id="+str(user))
				db_user.commit()
				db_user.close()

				sel_date=get_cur_date()
				state2=0
				profile=0
				rem_ar=[]

				text.place_forget()
				can2.place_forget()
				can3.place_forget()



				pun.place_forget()
				ppw.place_forget()
				ppw2.place_forget()

				login()



			return


		if profile!=0:


			if 381.5<=e.x<=381.5+22:
				if 420<=e.y<=420.0+22:

					if prof_show==0:
						prof_show=1
					elif prof_show==1:
						prof_show=0

					main()

			return



		#year

		if 0<=e.x<=30:
			if 10<=e.y<=10+30:
				
				date[-1]-=1

				m,y=date

				sel_date=[1,m,y]

				can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

				state2=0
				main()

				return


		l=get_text_length(can, str(date[-1]), "FreeMono", 13)

		if 30+5+l+5<=e.x<=30+5+l+5+30:
			if 10<=e.y<=10+30:
				
				date[-1]+=1

				m,y=date

				sel_date=[1,m,y]

				can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

				state2=0
				main()

				return


		#months

		if 0<=e.x<=30:
			if 10+30+10<=e.y<=10+30+10+30:


				if date[0]-1==0:
					date[-1]-=1
					date[0]=12
				else:
					date[0]-=1


				m,y=date

				sel_date=[1,m,y]

				can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

				state2=0

				main()
				return



		l=get_text_length(can, str(months[date[0]],), "FreeMono", 13)

		if 30+5+l+5<=e.x<=30+5+l+5+30:
			if 10+30+10<=e.y<=10+30+10+30:

				if date[0]+1==13:
					date[-1]+=1
					date[0]=1
				else:
					date[0]+=1

				m,y=date

				sel_date=[1,m,y]

				can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

				state2=0
				main()
				return


		for d in ar_date:

			if d[1]<=e.x<=d[1]+500/7:
				if d[2]<=e.y<=d[2]+500/7:

					m,y=date

					d_=d[0]


					sel_date=[d_,m,y]

					state2=0

					can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

					main()

					return

		if 500-10-30<=e.x<=500-10:
			if 10<=e.y<=10+30:

				sel_date=get_cur_date()
				date=sel_date[1:]

				state2=0

				can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

				main()





		if state2==1:


			#cancel



			if 519-1<=e.x<=749:
				if 582.5<=e.y<=582.5+29:

					state2=0

					can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
					text.delete("1.0",tk.END)
					main()

					return



			#create




			if 751<=e.x<=981+1:
				if 582.5<=e.y<=582.5+29:

					create_reminder()
					can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))

					main()

					

					return
		elif state2==0:


			cur_d=get_cur_date()
			tm_diff=get_time_difference(str(cur_d[0])+"/"+str(cur_d[1])+"/"+str(cur_d[2]),str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2]))

			if tm_diff==1:





				if 751<=e.x<=981+1:
					if 582.5<=e.y<=582.5+29:

						state2=1
						main()

						return
		#delete


		if 519-1<=e.x<=749:
			if 582.5<=e.y<=582.5+30:

				if state2==0:



					try:

						with open("data/reminder.json","r") as file:
							rem=json.load(file)

						v=rem[str(user)][str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2])]

						rem[str(user)].pop(str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2]))


						with open("data/reminder.json","w") as file:
							json.dump(rem,file,indent=4)

						can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))



						main()

						return


					except:
						return



		if 500-10-30<=e.x<=500-10-30+30:
			if 621-30-10<=e.y<=621-30-10+30:

				sel_date=get_cur_date()
				state2=0
				profile=0
				rem_ar=[]

				text.place_forget()
				can2.place_forget()
				can3.place_forget()


				pun.place_forget()
				ppw.place_forget()
				ppw2.place_forget()

				login()

				return





	elif state=="login":

		xx,yy=350,200

		x,y=(int(can["width"])-xx)/2,(int(can["height"])-yy)/2


		if x+140+182+5<=e.x<=x+140+182+5+22:
			if y+39-1+50<=e.y<=y+39-1+50+22:
				if pw["show"]=="*":
					pw["show"]=""
					can.delete(show)

					show=can.create_image(x+140+182+5,y+39-1+50,image=show1,anchor="nw")
				else:
					pw["show"]="*"
					can.delete(show)

					show=can.create_image(x+140+182+5,y+39-1+50,image=show2,anchor="nw")

				return






		#login

		u,p=un.get(),pw.get()

		if x<=e.x<=x+15:
			if y+yy-15<=e.y<=y+yy:


				



				cx,cy=x+15,y+yy-15

				r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

				if r<=15:


					if u=="" or p=="u":


						message(can,"Fill all Fields!","#f94449","#ffffff",x,y+yy+10,x+xx,y+yy+10+30)

						return

					if validate(u,p)==False:

						message(can,"Invalid Entry!","#f94449","#ffffff",x,y+yy+10,x+xx,y+yy+10+30)

						return

					else:

						user=validate(u,p)

						can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
						main()
					

				
				return


		if x<=e.x<=x+xx/2:
			if y+yy-30<=e.y<=y+yy:


				if u=="" or p=="u":


					message(can,"Fill all Fields!","#f94449","#ffffff",x,y+yy+10,x+xx,y+yy+10+30)

					return


				if validate(u,p)==False:

					message(can,"Invalid Entry!","#f94449","#ffffff",x,y+yy+10,x+xx,y+yy+10+30)

					return

				else:

					user=validate(u,p)
					can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
					main()

				return


		#sign_up

		if x+xx-15<=e.x<=x+xx:
			if y+yy-15<=e.y<=y+yy:



				cx,cy=x+15,y+yy-15

				r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

				if r<=15:
					create_account_()

				
				return


		if x+xx/2<=e.x<=x+xx:
			if y+yy-30<=e.y<=y+yy:

				create_account_()
				return

	elif state=="create_account":



		xx,yy=350,270

		x,y=(int(can["width"])-xx)/2,(int(can["height"])-yy)/2	


		if x+140+182+5<=e.x<=x+140+182+5+22:
			if y+39-1+50<=e.y<=y+39-1+50+22:
				if pw["show"]=="*":
					pw["show"]=""
					pw2["show"]=""
					can.delete(show)

					show=can.create_image(x+140+182+5,y+39-1+50,image=show1,anchor="nw")
				else:
					pw["show"]="*"
					pw2["show"]="*"

					can.delete(show)

					show=can.create_image(x+140+182+5,y+39-1+50,image=show2,anchor="nw")

				return



		#cancel

		u,p=un.get(),pw.get()

		if x<=e.x<=x+15:
			if y+yy-15<=e.y<=y+yy:


				



				cx,cy=x+15,y+yy-15

				r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

				if r<=15:


					login()
					

				
				return


		if x<=e.x<=x+xx/2:
			if y+yy-30<=e.y<=y+yy:


				login()

				return


		#sign_up

		u,p1,p2=un.get(),pw.get(),pw2.get()

		if x+xx-15<=e.x<=x+xx:
			if y+yy-15<=e.y<=y+yy:



				cx,cy=x+15,y+yy-15

				r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

				if r<=15:

					if u=="" or p1=="" or p2=="":

						message(can,"Fill all Fields!","#f94449","#ffffff",x,y+yy+10,x+xx,y+yy+10+30)

						return


					if p1!=p2:
						message(can,"Passwords doesn't match!","#f94449","#ffffff",x,y+yy+10,x+xx,y+yy+10+30)

						return



					db_user=db.connect("data/user.db")
					cur=db_user.cursor()

					rows=cur.execute("SELECT * FROM user")

					for row in rows:

						if u.lower()==row[1].lower():

							message(can,"Name Already Exists!","#f94449","#ffffff",x,y+yy+10,x+xx,y+yy+10+30)
							return

					create_account(u,p1)

					login()




					xx,yy=350,200

					x,y=(int(can["width"])-xx)/2,(int(can["height"])-yy)/2


					message(can,"Account Created Successfully!","#32fca7","#000000",x,y+yy+10,x+xx,y+yy+10+30)

				
				return


		if x+xx/2<=e.x<=x+xx:
			if y+yy-30<=e.y<=y+yy:


				if u=="" or p1=="" or p2=="":

					message(can,"Fill all Fields!","#f94449","#ffffff",x,y+yy+10,x+xx,y+yy+10+30)

					return


				if p1!=p2:
					message(can,"Passwords doesn't match!","#f94449","#ffffff",x,y+yy+10,x+xx,y+yy+10+30)

					return



				db_user=db.connect("data/user.db")
				cur=db_user.cursor()

				rows=cur.execute("SELECT * FROM user")

				for row in rows:

					if u.lower()==row[1].lower():
						message(can,"Name Already Exists!","#f94449","#ffffff",x,y+yy+10,x+xx,y+yy+10+30)

						return

				create_account(u,p1)


				login()



				xx,yy=350,200

				x,y=(int(can["width"])-xx)/2,(int(can["height"])-yy)/2


				message(can,"Account Created Successfully!","#32fca7","#000000",x,y+yy+10,x+xx,y+yy+10+30)


				return

m1,m2,m3,m4=0,0,0,0
def message(c,text,col1,col2,x,y,x2,y2):
	global m1,m2,m3,m4,tm

	tm=0

	m1=1
	m2=c

	c.delete(m3)
	c.delete(m4)


	m3=c.create_rectangle(x,y, x2,y2, fill=col1,outline=col1)
	m4=c.create_text(x+(x2-x)/2,y+(y2-y)/2,text=text,font=("FreeMono",13),fill=col2)


tm=0
def message_timer():
	global m1,m2,m3,m4,tm

	if m1==1:


		if tm>=3:

			m1=0

			m2.delete(m3)
			m2.delete(m4)


		tm+=1





	root.after(1000,message_timer)


def create_reminder():

	global user,sel_date,text,state2



	if text.get("1.0",tk.END)!="\n":

		try:

			with open("data/reminder.json","r") as file:

				rem=json.load(file)


			v=rem[str(user)][str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2])]



			ar=text.get("1.0",tk.END).split("\n")

			rem_dict={}

			for i in ar:
				if i=="\n" or i=="":
					continue


				c=0
				try:
					c=rem[str(user)][str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2])][i]
				except:
					pass


				rem_dict[i]=c


			rem[str(user)][str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2])]=rem_dict

			with open("data/reminder.json","w") as file:

				json.dump(rem,file,indent=4)


		except:

			try:
				with open("data/reminder.json","r") as file:

					rem=json.load(file)
			except:
				rem={}





			ar=text.get("1.0",tk.END).split("\n")

			rem_dict={}

			for i in ar:
				if i=="\n" or i=="":
					continue
				rem_dict[i]=0


			try:

				v=rem[str(user)]


				rem[str(user)].update({str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2]):rem_dict})


			except:

				rem.update({str(user):0})
				rem[str(user)]={str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2]):rem_dict}



			with open("data/reminder.json","w") as file:


				json.dump(rem,file,indent=4)


		text.place_forget()
		state2=0
		can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))
		main()




		return
	else:
		try:
			with open("data/reminder.json","r") as file:
				rem=json.load(file)

			v=rem[str(user)][str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2])]

			rem[str(user)].pop(str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2]))


			with open("data/reminder.json","w") as file:
				json.dump(rem,file,indent=4)

			can2["scrollregion"]=(0,0,int(can2["width"]),int(can2["height"]))



			main()
		except:
			pass




def validate(u,p):

	db_user=db.connect("data/user.db")
	cur=db_user.cursor()

	rows=cur.execute("SELECT * FROM user")

	for row in rows:

		if u==row[1] and p==row[2]:
			return row[0]

	return False


ar_date=[]

def det_success():
	global user

	try:
		with open("data/reminder.json","r") as file:

			data=json.load(file)

		sum_=0
		scount=0

		for i in data[str(user)]:



			for c in data[str(user)][i]:

				sum_+=1

				if data[str(user)][i][c]==1:
					scount+=1


		return int(scount/sum_*100)

	except:
		return 0


prof_show=0
def main():
	global w,h 
	global state,state2
	global can
	global previous,next_
	global date,months
	global cur_date1,cur_date2
	global sel_date
	global ar_date
	global un,pw,pw2
	global text
	global user
	global circle2,circle3,circle4,circle5,circle6,circle7,circle8,circle9,circle10
	global can2

	global checked
	global rem__
	global logout

	global trend

	global no_data
	global profile
	global pun,ppw,ppw2

	global prof_show


	un.place_forget()
	pw.place_forget()
	pw2.place_forget()


	pun.place_forget()
	ppw.place_forget()
	ppw2.place_forget()


	ar_date=[]


	state="main"


	can.delete("all")
	can["bg"]="#ffffff"





	#calender
	
	can.create_polygon(0,0, 501-15,0, 501,15, 501,621-15, 501-15,621,
		0,621, fill="#000000",outline="#000000" )

	can.create_image(501-29,0,image=circle2,anchor="nw")
	can.create_image(501-29,621-29,image=circle2,anchor="nw")
	

	#can.create_rectangle(0,0, 501,621, fill="#000000",outline="#000000")


	can.create_image(500-10-30,621-30-10,image=logout,anchor="nw")
	can.create_image(500-10-30-20-30,621-30-10,image=my_profile,anchor="nw")




	ar=[]

	a_=180

	cx,cy=501-15,15

	for a in range(90):

		x=15*math.sin(math.radians(a_))+cx
		y=15*math.cos(math.radians(a_))+cy
	
		ar.append(int(round(x,0)))
		ar.append(int(round(y,0)))
		a_-=1

	a_=90

	cx,cy=501-15,621-15

	for a in range(90):

		x=15*math.sin(math.radians(a_))+cx
		y=15*math.cos(math.radians(a_))+cy
	
		ar.append(int(round(x,0)))
		ar.append(int(round(y,0)))
		a_-=1


	#can.create_line(ar,fill="#151515")




	can.create_image(0,10,image=previous,anchor="nw")
	can.create_text(30+5,10+15,text=str(date[-1]),font=("FreeMono",13),fill="#ffffff",anchor="w")

	l=get_text_length(can, str(date[-1]), "FreeMono", 13)
	can.create_image(30+5+l+5,10,image=next_,anchor="nw")


	can.create_image(0,10+30+10,image=previous,anchor="nw")
	can.create_text(30+5,10+15+30+10,text=months[date[0]],font=("FreeMono",13),fill="#ffffff",anchor="w")

	l=get_text_length(can, str(months[date[0]],), "FreeMono", 13)
	can.create_image(30+5+l+5,10+30+10,image=next_,anchor="nw")


	if sel_date==get_cur_date():
		can.create_image(500-10-30,10,image=cur_date1,anchor="nw")
	else:
		can.create_image(500-10-30,10,image=cur_date2,anchor="nw")




	days_of_week=["MON","TUE","WED","THUR","FRI","SAT","SUN"]

	x=500/7/2

	for d in days_of_week:

		can.create_text(x,15+30+10+30+20,text=d,font=("FreeMono",13),fill="#ffffff",anchor="c")

		x+=500/7

	can.create_line(0,15+30+10+30+20+15,499,15+30+10+30+20+15,fill="#ffffff")



	n=get_days_in_month(str(date[-1])+"-"+str(date[0])+"-1")


	y=15+30+10+30+20+15+1

	dd=sel_date


	for n_ in range(n):

		con=0

		try:
			with open("data/reminder.json","r") as file:
				data=json.load(file)

			v=data[str(user)][str(n_+1)+"/"+str(date[0])+"/"+str(date[-1])]

			con=1
		except:
			pass



		x=days_of_week.index(get_day_of_week_number(str(date[-1])+"-"+str(date[0])+"-"+str(n_+1)))*500/7

		col="#ffffff"


		if con==1:

			can.create_image(x+500/7/2-4,y+500/7-15,image=circle5,anchor="nw")
			can.create_image(x+500/7/2-3,y+500/7-15+1,image=circle8,anchor="nw")


		if dd[-1]==date[-1] and dd[1]==date[0]:

			if dd[0]==n_+1:

				can.create_image(x,y,image=circle4,anchor="nw")
				can.create_image(x+500/7-20+1,y,image=circle4,anchor="nw")

				can.create_image(x,y+500/7-20+1,image=circle4,anchor="nw")
				can.create_image(x+500/7-20+1,y+500/7-20+1,image=circle4,anchor="nw")



				can.create_polygon(x+10,y, x+500/7-10,y, x+500/7,y+10, x+500/7,y+500/7-10, x+500/7-10,y+500/7, x+10,y+500/7, x,y+500/7-10,
				x,y+10, fill="#38fca5",outline="#38fca5")


				if con==1:

					can.create_image(x+500/7/2-4,y+500/7-15,image=circle6,anchor="nw")
					can.create_image(x+500/7/2-3,y+500/7-15+1,image=circle9,anchor="nw")

				col="#000000"

		ar_date.append([n_+1,x,y])


		x+=500/7/2




		can.create_text(x,y+500/7/2,text=str(n_+1),font=("FreeMono",15),fill=col)


		if get_day_of_week_number(str(date[-1])+"-"+str(date[0])+"-"+str(n_+1))=="SUN":
			y+=500/7







	if not profile==0:


		px,py=350,230

		x,y=(500-10-30-20-30)-px,(621-30-10)-py


		ar=[]

		r=15

		cx,cy=x+r,y+r

		a_=270


		for a in range(90):

			x_=r*math.sin(math.radians(a_))+cx
			y_=r*math.cos(math.radians(a_))+cy

			ar.append(round(x_,0))
			ar.append(round(y_,0))

			a_-=1




		cx,cy=x+px-r,y+r

		a_=180


		for a in range(90):

			x_=r*math.sin(math.radians(a_))+cx
			y_=r*math.cos(math.radians(a_))+cy

			ar.append(round(x_,0))
			ar.append(round(y_,0))

			a_-=1

		ar.append(x+px)
		ar.append(y+py-30-1)

		ar.append(x)
		ar.append(y+py-30-1)

		can.create_polygon(ar,fill="#ffffff",outline="#ffffff")

		ar=[]



		ar.append(x+px)
		ar.append(y+py-30-1)

		ar.append(x)
		ar.append(y+py-30-1)


		cx,cy=x+r,y+py-r

		a_=270


		for a in range(90):

			x_=r*math.sin(math.radians(a_))+cx
			y_=r*math.cos(math.radians(a_))+cy

			ar.append(round(x_,0))
			ar.append(round(y_,0))

			a_+=1


		cx,cy=x+px-r,y+py-r

		a_=0


		for a in range(90):

			x_=r*math.sin(math.radians(a_))+cx
			y_=r*math.cos(math.radians(a_))+cy

			ar.append(round(x_,0))
			ar.append(round(y_,0))

			a_+=1



		can.create_polygon(ar,fill="#555555",outline="#555555")




		


		xx=(px-(293-10))/2


		l=get_text_length(can, "User Name", "FreeMono", 13)

		can.create_text(x+xx,y+30,text="User Name",font=("FreeMono",13),fill="#000000",anchor="w")
		pun.place(in_=root,x=x+xx+l+20,y=y+30-10)
		can.create_rectangle(x+100+xx,y+19,x+283+xx,y+41,outline="#000000")


		can.create_text(x+xx,y+30+50,text="Password",font=("FreeMono",13),fill="#000000",anchor="w")
		ppw.place(in_=root,x=x+xx+l+20,y=y+30-10+50)
		can.create_rectangle(x+100+xx,y+19+50,x+283+xx,y+41+50,outline="#000000")


		if prof_show==1:

			ppw["show"]=""
			ppw2["show"]=""

			can.create_image(x+283+xx+5,y+19+50+((41-19)-22)/2,image=show1,anchor="nw")
		else:

			ppw["show"]="*"
			ppw2["show"]="*"

			can.create_image(x+283+xx+5,y+19+50+((41-19)-22)/2,image=show2,anchor="nw")


		if profile==2:
			can.create_text(x+xx,y+30+50*2,text="Password",font=("FreeMono",13),fill="#000000",anchor="w")
			ppw2.place(in_=root,x=x+xx+l+20,y=y+30-10+50*2)
			can.create_rectangle(x+100+xx,y+19+50*2,x+283+xx,y+41+50*2,outline="#000000")



		can.create_line(x,y+py-30,x+px,y+py-30,fill="#ffffff")
		can.create_line(x+px/2,y+py-30,x+px/2,y+py,fill="#ffffff")

		if profile==1:
			txt="Change"
		elif profile==2:
			txt="Save"

		can.create_text(x+px/4,y+py-30+15,text=txt,font=("FreeMono",13),fill="#ffffff")
		can.create_text(x+px-px/4,y+py-30+15,text="Delete",font=("FreeMono",13),fill="#ffffff")










	# reminder


	can.create_text(500+(int(can["width"])-500)/2,20,text=str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2]),
		font=("FreeMono",20),fill="#000000")





	cur_d=get_cur_date()
	tm_diff=get_time_difference(str(cur_d[0])+"/"+str(cur_d[1])+"/"+str(cur_d[2]),str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2]))

	


	rem_ar=[]

	try:

		with open("data/reminder.json", "r") as file:
			rem=json.load(file)



		for i in rem[str(user)][str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2])]:

			rem_ar.append([i,rem[str(user)][str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2])][i]])

	except:

		if tm_diff==0:
			state2=0

		else:
			state2=1







	def count_newlines(text):
	    return len(re.findall(r'\n', text))

	#can.create_rectangle(519,39, 981,574,outline="#999999",fill="#999999")



	ar=[]

	r=20

	a_=180

	cx,cy=519-1+r,39-1+r

	for a in range(90):

		x=r*math.sin(math.radians(a_))+cx
		y=r*math.cos(math.radians(a_))+cy

		x=int(round(x,0))
		y=int(round(y,0))

		ar.append(x)
		ar.append(y)

		a_+=1

	a_=270

	cx,cy=519-1+r,574+1-r

	for a in range(90):

		x=r*math.sin(math.radians(a_))+cx
		y=r*math.cos(math.radians(a_))+cy

		x=int(round(x,0))
		y=int(round(y,0))

		ar.append(x)
		ar.append(y)

		a_+=1


	a_=0

	cx,cy=981+1-r,574+1-r

	for a in range(90):

		x=r*math.sin(math.radians(a_))+cx
		y=r*math.cos(math.radians(a_))+cy

		x=int(round(x,0))
		y=int(round(y,0))

		ar.append(x)
		ar.append(y)

		a_+=1


	a_=90

	cx,cy=981+1-r,39-1+r

	for a in range(90):

		x=r*math.sin(math.radians(a_))+cx
		y=r*math.cos(math.radians(a_))+cy

		x=int(round(x,0))
		y=int(round(y,0))

		ar.append(x)
		ar.append(y)

		a_+=1



	can.create_polygon(*ar,fill="#ffffff",outline="#000000",width=2)

	



	if state2==0:

		text.place_forget()

		

		can2.delete("all")

		can2.place(in_=root,x=519-1+((981+1-519-1)-int(can2["width"]))/2,y=39-1+((574+1-39-1)-int(can2["height"]))/2)





		xx=((981+1)-(519-1))/4

		

		y=574+((621-574)-30)/2

		if tm_diff==1:
			col="#ffffff"
			can.create_image(981+1-19,y,image=circle7,anchor="nw")
			can.create_image(981+1-19,y+30-19,image=circle7,anchor="nw")

			can.create_polygon(751,y, 981+1-10,y, 981+1,y+10, 981+1,y+30-10, 981+1-10,y+30, 751,y+30,fill="#000000",outline="#000000")



		else:
			col="#ffffff"

			can.create_image(981+1-19,y,image=circle10,anchor="nw")
			can.create_image(981+1-19,y+30-19,image=circle10,anchor="nw")

			can.create_polygon(751,y, 981+1-10,y, 981+1,y+10, 981+1,y+30-10, 981+1-10,y+30, 751,y+30,fill="#555555",outline="#555555")


			

		can.create_text(981+1-xx,y+15,text="Modify",font=("FreeMono",13),fill=col)



		rem__=[]





		if len(rem_ar)==0:

			im=Image.open("data/no_data.png")
			x,y=im.size


			
			x,y=(int(can2["width"])-x)/2, (int(can2["height"])-y)/2

			can2.create_image(x,y,image=no_data,anchor="nw")




		else:



			y=20

			for i in rem_ar:

				y1=y


				can2.create_image(8,y+6,image=circle3,anchor="nw")

				if i[1]==1:

					can2.create_oval(int(can2["width"])-10-25+2,y+6-10+2,int(can2["width"])-10-25+2+21,y+6-10+2+21,fill="#125437",
						outline="#125437")

					can2.create_image(int(can2["width"])-10-25,y+6-10,image=checked,anchor="nw")




				val=i[0].split(" ")


				



				txt=""
				txt2=""


				sz=int(can2["width"])-70

				x=5
				for _ in range(len(val)):

					
					

					if get_text_length(can2, txt2+val[_]+" ", "FreeMono", 13)<=sz:
						txt+=val[_]+" "
						txt2+=val[_]+" "
					else:
						txt+="\n"+val[_]+" "
						txt2="\n"+val[_]+" "


				art=txt.split("\n")

				for t in art:



					can2.create_text(25,y,text=t,font=("FreeMono",13),anchor="nw",fill="#000000")

					if not t==art[-1]:

						y+=20



				y2=y


				rem__.append([i[0],y1,y2+20])




				

				y+=50


				if y>int(can2["height"]):

					can2["scrollregion"]=(0,0,int(can2["width"]),y)



		can.focus_set()

		y=574+((621-574)-30)/2


		if len(rem_ar)==0:
			col="#ffffff"
			can.create_image(519-1,y,image=circle10,anchor="nw")
			can.create_image(519-1,y+30-19,image=circle10,anchor="nw")

			can.create_polygon(519-1+10,y, 749,y, 749,y+30, 519-1+10,y+30, 519-1,y+30-10, 519-1,y+10,fill="#555555",outline="#555555" )



		else:
			col="#ffffff"

			can.create_image(519-1,y,image=circle7,anchor="nw")
			can.create_image(519-1,y+30-19,image=circle7,anchor="nw")

			can.create_polygon(519-1+10,y, 749,y, 749,y+30, 519-1+10,y+30, 519-1,y+30-10, 519-1,y+10,fill="#000000",outline="#000000" )



		xx=((981+1)-(519-1))/4
		y=574+((621-574)-30)/2

		can.create_text(519-1+xx,y+15,text="Delete",font=("FreeMono",13),fill=col)


	else:

		y=574+((621-574)-30)/2



		can.create_image(981+1-19,y,image=circle7,anchor="nw")
		can.create_image(981+1-19,y+30-19,image=circle7,anchor="nw")

		can.create_polygon(751,y, 981+1-10,y, 981+1,y+10, 981+1,y+30-10, 981+1-10,y+30, 751,y+30,fill="#000000",outline="#000000")





		can.create_image(519-1,y,image=circle7,anchor="nw")
		can.create_image(519-1,y+30-19,image=circle7,anchor="nw")

		can.create_polygon(519-1+10,y, 749,y, 749,y+30, 519-1+10,y+30, 519-1,y+30-10, 519-1,y+10,fill="#000000",outline="#000000" )


		txt=""

		try:
			with open("data/reminder.json","r") as file:

				data=json.load(file)


			for t in data[str(user)][str(sel_date[0])+"/"+str(sel_date[1])+"/"+str(sel_date[2])]:

				txt+=t+"\n\n"

		except:
			pass



		can2.place_forget()
		text.delete("1.0", tk.END)

		text.insert(tk.END,txt)


		text.place(in_=root,x=519-1+((981+1-519-1)-int(can2["width"]))/2,y=39-1+((574+1-39-1)-int(can2["height"]))/2)



		xx=((981+1)-(519-1))/4

		can.create_text(519-1+xx,y+15,text="Cancel",font=("FreeMono",13),fill="#ffffff")

		can.create_text(981+1-xx,y+15,text="Create",font=("FreeMono",13),fill="#ffffff")





		text.focus_set()


	can.create_image(5,h-30-10,image=trend,anchor="nw")

	can.create_text(5+30+10,h-10,text=str(det_success())+" %",font=("FreeMono",13),fill="#38fca5",anchor="sw")


def get_time_difference(time1,time2,c=0,format="%d/%m/%Y"):



	# Parse the date strings into datetime objects
	t1 = datetime.datetime.strptime(time1, format)
	t2 = datetime.datetime.strptime(time2, format)
	
	if c==0:

		if t1<=t2:
			return 1
		else:
			return 0
	elif c==1:

		if t1<t2:
			return 1
		else:
			return 0  
	elif c==2:  

		if t2<=t1:
			return 1
		else:
			return 0  

def get_days_in_month(date_string, format_string="%Y-%m-%d"):
    date_obj = datetime.datetime.strptime(date_string, format_string)
    year = date_obj.year
    month = date_obj.month
    return monthrange(year, month)[1]

def get_day_of_week_number(date_string, format_string="%Y-%m-%d"):
    date_obj = datetime.datetime.strptime(date_string, format_string)
    days = ["MON","TUE","WED","THUR","FRI","SAT","SUN"]
    return days[date_obj.weekday()]


def get_cur_date():

	now=datetime.datetime.now()

	year=now.year
	month=now.month
	day=now.day


	return [day,month,year]


date=get_cur_date()[1:]


def create_account(u,p):




	db_user=db.connect('data/user.db')
	cur=db_user.cursor()

	cur.execute("SELECT MAX(user_id) FROM user")
	rows=cur.fetchall()

	v=0
	for row in rows:
		v=row[0]
	if v==None:
		v=1
	else:
		v+=1

	cur.execute("INSERT INTO user VALUES("+str(v)+",'"+str(u)+"','"+str(p)+"')")
	db_user.commit()

def create_account_():
	global w,h
	global can
	global circle
	global un,pw,pw2
	global state
	global show,show1,show2

	state="create_account"


	can.delete("all")

	can["bg"]="#000000"



	xx,yy=350,270

	x,y=(int(can["width"])-xx)/2,(int(can["height"])-yy)/2

	can.create_image(x,y,image=circle,anchor="nw")
	can.create_image(x+xx-30+1,y,image=circle,anchor="nw")
	can.create_image(x,y+yy-30+1,image=circle11,anchor="nw")
	can.create_image(x+xx-30+1,y+yy-30+1,image=circle11,anchor="nw")

	can.create_polygon(x+15,y, x+xx-15,y, x+xx,y+15, x+xx,y+yy-31,
		x,y+yy-31, x,y+15,fill="#ffffff",outline="#ffffff")


	can.create_polygon(x,y+yy-31, x+xx,y+yy-31, x+xx,y+yy-15, x+xx-15,y+yy,
		x+15,y+yy, x,y+yy-15, x,y+yy-31, fill="#555555",outline="#555555")



	can.create_text(x+20,y+50,text="User Name",font=("FreeMono",13),fill="#000000",anchor="w")
	can.create_text(x+20,y+50+50,text="Password",font=("FreeMono",13),fill="#000000",anchor="w")
	can.create_text(x+20,y+50+50+50,text="Password",font=("FreeMono",13),fill="#000000",anchor="w")


	un.delete(0,tk.END)

	can.create_rectangle(x+140-1,y+39-1, x+140+182,y+39+21,outline="#000000")
	un.place(in_=root,x=x+140,y=y+39)

	pw.delete(0,tk.END)

	pw["show"]="*"
	pw2["show"]="*"


	can.create_rectangle(x+140-1,y+39-1+50, x+140+182,y+39+21+50,outline="#000000")
	pw.place(in_=root,x=x+140,y=y+39+50)

	show=can.create_image(x+140+182+5,y+39-1+50,image=show2,anchor="nw")



	pw2.delete(0,tk.END)

	can.create_rectangle(x+140-1,y+39-1+50+50, x+140+182,y+39+21+50+50,outline="#000000")
	pw2.place(in_=root,x=x+140,y=y+39+50+50)




	can.create_line(x,y+yy-30, x+xx,y+yy-30, fill="#ffffff")
	can.create_line(x+xx/2,y+yy-30, x+xx/2,y+yy, fill="#ffffff")


	can.create_text(x+xx/4,y+yy-15, text="Cancel",font=("FreeMono",13),fill="#ffffff")
	can.create_text(x+xx-xx/4,y+yy-15, text="Register",font=("FreeMono",13),fill="#ffffff")



	un.focus_set()

show=0
def login():
	global w,h
	global can
	global circle,circle11
	global un,pw,pw2
	global state
	global show,show1,show2


	state="login"
	pw2.place_forget()


	can.delete("all")

	can["bg"]="#000000"



	xx,yy=350,200

	x,y=(int(can["width"])-xx)/2,(int(can["height"])-yy)/2


	can.create_image(x,y,image=circle,anchor="nw")
	can.create_image(x+xx-30+1,y,image=circle,anchor="nw")
	can.create_image(x,y+yy-30+1,image=circle11,anchor="nw")
	can.create_image(x+xx-30+1,y+yy-30+1,image=circle11,anchor="nw")

	can.create_polygon(x+15,y, x+xx-15,y, x+xx,y+15, x+xx,y+yy-31,
		x,y+yy-31, x,y+15,fill="#ffffff",outline="#ffffff")


	can.create_polygon(x,y+yy-31, x+xx,y+yy-31, x+xx,y+yy-15, x+xx-15,y+yy,
		x+15,y+yy, x,y+yy-15, x,y+yy-31, fill="#555555",outline="#555555")




	#x+xx-15,y+yy, x+15,y+yy, x,y+yy-15, x,y+15



	can.create_text(x+20,y+50,text="User Name",font=("FreeMono",13),fill="#000000",anchor="w")
	can.create_text(x+20,y+50+50,text="Password",font=("FreeMono",13),fill="#000000",anchor="w")


	un.delete(0,tk.END)

	can.create_rectangle(x+140-1,y+39-1, x+140+182,y+39+21,outline="#000000")

	un.place(in_=root,x=x+140,y=y+39)

	pw.delete(0,tk.END)

	pw["show"]="*"

	can.create_rectangle(x+140-1,y+39-1+50, x+140+182,y+39+21+50,outline="#000000")
	pw.place(in_=root,x=x+140,y=y+39+50)


	show=can.create_image(x+140+182+5,y+39-1+50,image=show2,anchor="nw")



	can.create_line(x,y+yy-30, x+xx,y+yy-30, fill="#ffffff")
	can.create_line(x+xx/2,y+yy-30, x+xx/2,y+yy, fill="#ffffff")


	can.create_text(x+xx/4,y+yy-15, text="Login",font=("FreeMono",13),fill="#ffffff")
	can.create_text(x+xx-xx/4,y+yy-15, text="Sign Up",font=("FreeMono",13),fill="#ffffff")


	un.focus_set()



previous,next_=0,0
cur_date1,cur_date2=0,0
circle,circle2,circle3,circle4,circle5,circle6,circle7,circle8,circle9,circle10,circle11=0,0,0,0,0,0,0,0,0,0,0
checked=0
logout=0
show1,show2=0,0
trend=0
no_data=0
my_profile=0
def load_im():
	global previous,next_
	global cur_date1,cur_date2
	global circle,circle2,circle3,circle4,circle5,circle6,circle7,circle8,circle9,circle10,circle11
	global checked
	global logout
	global show1,show2

	global trend
	global no_data
	global my_profile


	previous=ImageTk.PhotoImage(file="data/previous.png")
	next_=ImageTk.PhotoImage(file="data/next.png")

	cur_date1=ImageTk.PhotoImage(file="data/cur_date1.png")
	cur_date2=ImageTk.PhotoImage(file="data/cur_date2.png")

	circle=ImageTk.PhotoImage(file="data/circle.png")
	circle2=ImageTk.PhotoImage(file="data/circle2.png")
	circle3=ImageTk.PhotoImage(file="data/circle3.png")
	circle4=ImageTk.PhotoImage(file="data/circle4.png")
	circle5=ImageTk.PhotoImage(file="data/circle5.png")
	circle6=ImageTk.PhotoImage(file="data/circle6.png")
	circle7=ImageTk.PhotoImage(file="data/circle7.png")
	circle8=ImageTk.PhotoImage(file="data/circle8.png")
	circle9=ImageTk.PhotoImage(file="data/circle9.png")
	circle10=ImageTk.PhotoImage(file="data/circle10.png")
	circle11=ImageTk.PhotoImage(file="data/circle11.png")



	checked=ImageTk.PhotoImage(file="data/checked.png")	
	logout=ImageTk.PhotoImage(file="data/logout.png")
	show1=ImageTk.PhotoImage(file="data/show1.png")	
	show2=ImageTk.PhotoImage(file="data/show2.png")

	trend=ImageTk.PhotoImage(file="data/trend.png")
	no_data=ImageTk.PhotoImage(file="data/no_data.png")
	my_profile=ImageTk.PhotoImage(file="data/my_profile.png")


def get_taskbar_height():
    # Get the screen dimensions
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    
    # Get the work area (excluding taskbar)
    rect = RECT()
    ctypes.windll.user32.SystemParametersInfoW(0x0030, 0, ctypes.byref(rect), 0)
    
    work_area_height = rect.bottom - rect.top
    taskbar_height = screen_height - work_area_height
    
    return max(0, taskbar_height)  # Ensure no negative values
def get_text_length(canvas, text, font_name, font_size):
    # Create a tkinter font object with the given font name and size
    text_font = font.Font(family=font_name, size=font_size)

    # Measure the width of the text in pixels
    text_width = text_font.measure(text)
    return text_width


cd=[]
def update_cur_date():

	global cd,state

	if cd!=get_cur_date():
		if state=="main":

			cd=get_cur_date()
			main()


	root.after(100,update_cur_date)


state=""
sel_date=get_cur_date()
user=-1
state2=0

root=tk.Tk()
root.title("HRemider")
root.iconbitmap("data/icon.ico")
root.resizable(0,0)

w,h=1000,621
wd,ht=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry(str(w)+"x"+str(h)+"+"+str(int((wd-w)/2))+"+"+str(int((ht-h)/2-get_taskbar_height())))

can=tk.Canvas(width=w,height=h,bg="#38fca5",relief="flat",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)
can.bind("<Button-1>",can_b1)


def focus_pw(e):
	global un,pw

	pw.focus_set()


def focus_pw2(e):
	global pw,pw2
	global state


	if state=="create_account":
		pw2.focus_set()



un=tk.Entry(width=20,font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0)
un.bind("<Return>",focus_pw)
pw=tk.Entry(width=20,font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,show=("*"))
pw.bind("<Return>",focus_pw2)
pw2=tk.Entry(width=20,font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,show=("*"))


text=tk.Text(width=50,height=27,font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,
	selectbackground="#000000",selectforeground="#ffffff")
text.config(wrap=tk.WORD)

def on_mousewheel(e):

    if int(can2["scrollregion"].split(" ")[-1])>int(can2["height"]):

        can2.yview_scroll(int(-1*(e.delta/120)), "units")

can2=tk.Canvas(bg="#ffffff",relief="flat",highlightthickness=0,border=0)

can2["width"]=972-519
can2["height"]=555-40
can2.bind("<Button-1>",can2_b1)
can2.bind_all("<MouseWheel>",on_mousewheel)

can3=tk.Canvas(bg="#ffffff",relief="flat",highlightthickness=0,border=0,height=20,)
l=get_text_length(can3, "Write Reminder...", "FreeMono", 13)

can3["width"]=10+l

can3.create_text(0,10,text="Write Reminder...",fill="#777777",anchor="w",font=("FreeMono",13))

def prompt_to_write():
	global state2,text
	global can2


	if state2==1:
		if text.get("1.0",tk.END)=="\n":
			can3.place(in_=root,x=519-1+((981+1-519-1)-int(can2["width"]))/2+2,y=39-1+((574+1-39-1)-int(can2["height"]))/2)
		else:
			can3.place_forget()
	else:
		can3.place_forget()


	root.after(1,prompt_to_write)


def focus_ppw(e):
	global ppw

	ppw.focus_set()

def focus_ppw2(e):
	global ppw2

	ppw2.focus_set()

pun=tk.Entry(width=20,font=("FreeMono",13),bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0)
pun.bind("<Return>",focus_ppw)
ppw=tk.Entry(width=20,font=("FreeMono",13),bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,show=("*"))
ppw.bind("<Return>",focus_ppw2)
ppw2=tk.Entry(width=20,font=("FreeMono",13),bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,show=("*"))


try:
	db_user=db.connect('data/user.db')
	cur=db_user.cursor()
	cur.execute("""CREATE TABLE user(
		user_id INT,
		user_name VARCHAR(255),
		password VARCHAR(255)
		);""")
	db_user.close()


except:
	pass


try:
	db_reminder=db.connect('data/reminders.db')
	cur=db_reminder.cursor()
	cur.execute("""CREATE TABLE reminder(
		user_id INT,
		date_ VARCHAR(255),
		reminder VARCHAR(255)
		);""")
	db_reminder.close()


except:
	pass




load_im()

#main()

login()

message_timer()
prompt_to_write()

update_cur_date()
root.mainloop()