#DBMS Winter '21
#vaccination DB
#UI file
#Team-26

import sys
import mysql.connector as conn
from mysql.connector import Error
from tkinter import *
from PIL import ImageTk, Image
from tkinter import scrolledtext


#connect to db
#establish connection with db

try:
        connection = conn.connect(host='localhost',
                                database='vaccination',
                                user='kone',
                                password='Klol4365!')

        pointer = connection.cursor()
        #run(connection)
        #connection.close()

except Error:
        print("error while connecting", Error)
        exit(0)


class MyWindow:
    
    def __init__(self, win):

        self.toplabel = Label(win, text = 'COVID-19 DATA APPLICATION', fg = "white", bg = "black", font = "Helvetica 16 bold italic")
        self.mainlabel = Label(win, text = 'TEEKA-KARAN', fg = "black", bg = "white", font = "Helvetica 16 bold")
        self.mainlabel.place(x = 350, y = 70)
        self.toplabel.place(x = 10, y = 10) 
        self.query = Label(win, text = 'Input', font = "Helvetica 16 bold")
        self.result = Label(win, text = 'Result', font = "Helvetica 16 bold")
        self.text_area1 = Entry(bd = 1)
        self.text_area1.place(x = 220, y = 150)
        self.query.place(x = 100, y = 150)

        
        self.exitt = Button(win, text='exit application', command=self.exitt, fg = "black", bg = "white", font = "Helvetica 12 bold italic")
        self.exitt.place(x = 250, y = 300)

        self.query1 = Button(win, text='enter new employee', command=self.query1, fg = "black", bg = "white", font = "Helvetica 12 bold italic")
        self.query1.place(x = 100, y = 220)

        self.query2 = Button(win, text='heart patient, senior citizens, vaccinated >=1 times', command=self.query2, fg = "black", bg = "white", font = "Helvetica 12 bold italic")
        self.query2.place(x = 475, y = 220)

        self.query3 = Button(win, text='vaccines with price > avg price', command=self.query3, fg = "black", bg = "white", font = "Helvetica 12 bold italic")
        self.query3.place(x = 475, y = 150)

        self.query4 = Button(win, text='show employees grouped by experience', command=self.query4, fg = "black", bg = "white", font = "Helvetica 12 bold italic")
        self.query4.place(x = 475, y = 290)

        self.result.place(x = 20, y = 300)
        self.text_area2 = scrolledtext.ScrolledText(win, width = 95, height = 10, font = ("Times New Roman",12))
        self.text_area2.grid(column = 0, pady = 10, padx = 10)
        self.text_area2.place(x = 10, y = 350)


    def query1(self):
        a,b,c,d = self.text_area1.get().split(',')
        query = "insert into health_ministry(e_name, e_dob, e_experience, e_password) values('" + a + "','" + b + "'," + c + ",'" + d+"');"
        pointer.execute(query)
        connection.commit()
        print("executed successfully")
        #self.text_area2.append(str(a+" "+b+" "+c+" "+d))

    def query2(self):
        query="select health_care_centre.h_id, health_care_centre.h_name, citizen.c_id, "\
        "citizen.c_name, ST_DISTANCE_SPHERE(POINT(citizen_location.longitude, "\
        "citizen_location.latitude ), POINT(health_centre_location.longitude, "\
        "health_centre_location.latitude))/1000 AS distance FROM health_care_centre, "\
        "citizen, citizen_location, health_centre_location WHERE citizen.h_id = "\
        "health_care_centre.h_id AND citizen.h_id = health_centre_location.h_id AND "\
        "citizen.c_id = citizen_location.c_id AND TIMESTAMPDIFF(YEAR, c_dob, CURDATE())"\
        " >=60 AND c_vaccinated>=1 AND LOWER(c_medicalhistory) LIKE '%heart%' ORDER BY "\
        "distance;"

        pointer.execute(query)
        result = pointer.fetchall()

        ans="\nh_id, h_name, c_id, c_name, distance\n"

        for value in result:
            ans=ans+str(value)+"\n"

        self.text_area2.insert(END, ans)

    def query3(self):

        query="select * FROM vaccine WHERE v_price > (SELECT AVG(v_price) FROM vaccine);"

        pointer.execute(query)
        result = pointer.fetchall()

        ans="\nm_id, v_id, v_name, v_type, v_price, v_manufacture_date, expiry date, storage_temp \n"

        for value in result:
            ans=ans+str(value)+"\n"

        self.text_area2.insert(END, ans)

    def query4(self):
        query="select count(*) as num_emp, e_experience FROM health_ministry group by e_experience;"

        pointer.execute(query)
        result = pointer.fetchall()

        ans="\nnum_emp, experience\n"

        for value in result:
            ans=ans+str(value)+"\n"

        self.text_area2.insert(END, ans)

    def exitt(self):
        pointer.close()
        connection.close()
        exit(0)


root = Tk()

canv = Canvas(root, width = 1000, height = 600, bg='white')
canv.grid(row = 2, column = 3)

img = ImageTk.PhotoImage(Image.open("bg.jpeg"))
canv.create_image(0, 0, anchor = NW, image = img)


mywin = MyWindow(root)

root.title('HEALTH MINISTRY')

root.mainloop()
