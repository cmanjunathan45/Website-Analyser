import socket 
from bs4 import BeautifulSoup as bs
import requests
import folium
import webbrowser
from tkinter import *
from tkinter import messagebox,filedialog
import tkinter as tk

root=tk.Tk()
root.title("WebSite Analyser | Manjunathan C")
root.config(bg="#0090d3")
root.geometry("600x600")
ico=PhotoImage(file="icon.png")
root.iconphoto(True,ico)
head=Label(root,text="Enter the Website address (without http)",font=("font awesome",15,"bold italic"),fg="#3d155f",bg="#0090d3")
head.place(x=60,y=10)
def clear():
	hosText.delete("1.0",END)
	conText.delete("1.0",END)
	counText.delete("1.0",END)
	latLonText.delete("1.0",END)
	pinText.delete("1.0",END)
	ipText.delete("1.0",END)
def find():
	clear()
	sitename=entry.get()
	try:
		url1="http://"+sitename
		resp=requests.get(url1)
		if resp.status_code==200:
			ipadr=socket.gethostbyname(sitename)
			url="https://whatismyipaddress.com/ip/"+ipadr
			headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"}
			response=requests.get(url,headers=headers)
			soup=bs(response.text,"html.parser")

			ipText.insert(END,ipadr)

			hos=soup.find_all("td")[2].get_text()
			hosText.insert(END,hos)
			
			cont=soup.find_all("td")[10].get_text()
			conText.insert(END,cont)
			
			coun=soup.find_all("td")[11].get_text()
			counText.insert(END,coun)
			
			try:
				lat=soup.find_all("td")[14].get_text()
				lat=lat.split("  ")
				lat=lat[0].replace("\n","")
				lon=soup.find_all("td")[15].get_text()
				lon=lon.split("  ")
				lon=lon[0].replace("\n","")
				post=soup.find_all("td")[16].get_text()
				pinText.insert(END,post)
				latLonText.insert(END,lat+" & "+lon)

			
			except:
				lat=soup.find_all("td")[12].get_text()
				lat=lat.split("  ")
				lat=lat[0].replace("\n","")
				lon=soup.find_all("td")[13].get_text()
				lon=lon.split("  ")
				lon=lon[0].replace("\n","")
				post=soup.find_all("td")[14].get_text()
				pinText.insert(END,post)
				latLonText.insert(END,lat+" & "+lon)
			def save():
				mapFind=folium.Map(location=[lat,lon],zoom_start=14)
				mapName=entry.get()+".html"
				a=mapFind.save("sites/"+mapName)
				webbrowser.open("sites/"+mapName)
			buttonSave=Button(root,text="Save",font=("font awesome",15,"bold italic"),bg="#3d155f",fg="#0090d3",width=5,borderwidth=5,activebackground="pink",command=save)
			buttonSave.place(x=225,y=440)
		elif(resp.status_code==301):
			messagebox.showinfo("Error 301 - Moved Permanently","The requested resource has been assigned a new permanent Uniform Resource Identifier (URI) and any future references to the resource should use one of the returned URIs.")
		elif(resp.status_code==302):
			messagebox.showinfo("Error 302 - Moved Permanently","The requested resource resides temporarily under a different Uniform Resource Identifier (URI).")
		elif(resp.status_code==400):
			messagebox.showinfo("Error 400 - Bad Request","The request could not be understood by the server due to invalid syntax.")
		elif(resp.status_code==403):
			messagebox.showinfo("Error 403 - Access Forbidden","The server understood the request, but is refusing to fulfill it.")
		elif(resp.status_code==404):
			messagebox.showinfo("Error 404 - Not Found","The server has not found anything matching the Request-URI (Uniform Resource Identifier)")
		elif(resp.status_code==407):
			messagebox.showinfo("Error 407 -  Proxy Authentication Required")
		elif(resp.status_code==408):
			messagebox.showinfo("Error 408 - Connection Time Out","The client did not produce a request within server timeout limit.")
		elif(resp.status_code==409):
			messagebox.showinfo("Error 409 - Conflict","reCaptcha or The request could not be completed due to a conflict with the current state of the resource. The user should resolve the conflict and resubmit the request.")
		elif(resp.status_code==500):
			messagebox.showinfo("Error 500 - Internal Server Error","The server encountered an unexpected condition that prevented it from fulfilling the request.")
		else:
			messagebox.showinfo("Unable to Reach","Check Your Internet Connection")
	except:
		messagebox.showinfo("Unable to Reach","Check Your Internet Connection Or ReCheck Your Input")
entry=Entry(root,width=30,borderwidth=6,font=("fontawesome",15,"bold italic"),bg="white",fg="#3d155f")
entry.place(x=70,y=50)

buttonFind=Button(root,text="Find",font=("font awesome",15,"bold italic"),bg="#3d155f",fg="#0090d3",width=5,borderwidth=5,activebackground="pink",command=find)
buttonFind.place(x=290,y=100)

buttonClear=Button(root,text="Clear",font=("font awesome",15,"bold italic"),bg="#3d155f",fg="#0090d3",width=5,borderwidth=5,activebackground="pink",command=lambda: entry.delete(0,END))
buttonClear.place(x=180,y=100)

host=Label(root,text="Host Server      : ",font=("font awesome",15,"bold italic"),fg="#3d155f",bg="#0090d3")
host.place(x=20,y=160)
hosText=Text(root,width=40,height=1,font=("font awesome",10,"bold"),borderwidth=3)
hosText.place(x=210,y=160)

cont=Label(root,text="Continent         : ",font=("font awesome",15,"bold italic"),fg="#3d155f",bg="#0090d3")
cont.place(x=20,y=200)
conText=Text(root,width=40,height=1,font=("font awesome",10,"bold"),borderwidth=3)
conText.place(x=210,y=200)

coun=Label(root,text="Country            : ",font=("font awesome",15,"bold italic"),fg="#3d155f",bg="#0090d3")
coun.place(x=20,y=240)
counText=Text(root,width=40,height=1,font=("font awesome",10,"bold"),borderwidth=3)
counText.place(x=210,y=240)

latLon=Label(root,text="Latitude&\nLongitude        : ",font=("font awesome",15,"bold italic"),fg="#3d155f",bg="#0090d3")
latLon.place(x=20,y=280)

latLonText=Text(root,width=40,height=1,font=("font awesome",10,"bold"),borderwidth=3)
latLonText.place(x=210,y=290)

pin=Label(root,text="Postal Code     : ",font=("font awesome",15,"bold italic"),fg="#3d155f",bg="#0090d3")
pin.place(x=20,y=340)

pinText=Text(root,width=40,height=1,font=("font awesome",10,"bold"),borderwidth=3)
pinText.place(x=210,y=340)

ip=Label(root,text="IP Address     : ",font=("font awesome",15,"bold italic"),fg="#3d155f",bg="#0090d3")
ip.place(x=20,y=390)

ipText=Text(root,width=40,height=1,font=("font awesome",10,"bold"),borderwidth=3)
ipText.place(x=210,y=390)

buttonClearText=Button(root,text="Clear",font=("font awesome",15,"bold italic"),bg="#3d155f",fg="#0090d3",width=5,borderwidth=5,activebackground="pink",command=clear)
buttonClearText.place(x=140,y=490)

buttonExit=Button(root,text="Exit",font=("font awesome",15,"bold italic"),bg="#3d155f",fg="#0090d3",width=5,borderwidth=5,activebackground="pink",command=root.destroy)
buttonExit.place(x=310,y=490)

buttonContact=Button(root,text="Contact",font=("font awesome",15,"bold italic"),bg="#3d155f",fg="#0090d3",width=5,borderwidth=5,activebackground="pink",command=lambda:webbrowser.open("https://github.com/cmanjunathan45") )
buttonContact.place(x=225,y=540)

root.mainloop()