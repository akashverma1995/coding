import serial
import serial.tools.list_ports
import time
# import keyboard
import cv2
from tracker import *
import numpy as np
from skimage.measure import find_contours
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.draw import polygon_perimeter
import os
from time import sleep
from time import *            
import time
import glob
from flask import send_file
from datetime import datetime, date
from flask import Flask
import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import flash, request
from flask_cors import CORS, cross_origin
from flask import Flask,render_template,Response
#from werkzeug import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import random
import requests
from time import time
import numpy as np
import math
import keyboard
import json
# import serial
# import serial.tools.list_ports


# img=cv2.imread('frame_con_21.png',1)

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (0, 255, 0)
thickness = 2


print("start")
ports = serial.tools.list_ports.comports(include_links=False)
print(ports)
#Serial takes two parameters: serial device and baudrate
ser = serial.Serial('COM3', 115200, timeout=0.5)

print(ser)


# ports = serial.tools.list_ports.comports(include_links=False)
# #Serial takes two parameters: serial device and baudrate
# ser = serial.Serial('COM3', 115200, timeout=1)


# while True:
# 	data = ser.readline()
# 	start_ = data.decode()
#     print(start_)

img_path = r'D:\wadiraj\img'
@app.route('/video', methods=['POST', 'GET'])
@cross_origin()
def track():
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])
	start = False   
	cap1 = cv2.VideoCapture(1)
	cap2 = cv2.VideoCapture(0)
	cap3 = cv2.VideoCapture(2)
	count = 0
	count_new = 0
	tracker = EuclideanDistTracker()
	object_detector = cv2.createBackgroundSubtractorMOG2()
	img_path = os.getcwd()
	copy = np.zeros((720, 1280, 3), np.uint8)
	track.var3 = copy
	while True:
		flag_list=[]
		print('while')
		ret1, frame1 = cap1.read()
		ret2, frame2 = cap2.read()
		ret3, frame3 = cap3.read()

		if ret1 == True and ret2 == True:
			frame1 = cv2.flip(frame1, -1)
			frame1 = cv2.resize(frame1, (426, 720))
			frame2 = cv2.flip(frame2, -1)
			frame2 = cv2.resize(frame2, (426, 720))
			frame3 = cv2.flip(frame3, -1)
			frame3 = cv2.resize(frame3, (426, 720))
			frame_con = np.concatenate((frame1, frame2, frame3), axis = 1)
			#cv2.imwrite(f'lhs_image/{count}.png',frame_con)
		else:
			if ret1 == True:
				frame1 = cv2.flip(frame1, -1)
				frame1 = cv2.resize(frame1, (426, 720))
				frame2 = np.zeros([frame1.shape[0], frame1.shape[1], 3], dtype = 'uint8')
				frame3 = cv2.flip(frame3, -1)
				cv2.putText(frame2, 'Camera \nnot working', (300, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (145, 100, 245), 2, cv2.LINE_AA)
				frame_con = np.concatenate((frame1, frame2, frame3), axis = 1)
			elif ret2 == True:
				frame2 = cv2.resize(frame2, (426, 720))
				frame1 = np.zeros([frame2.shape[0], frame2.shape[1], 3], dtype = 'uint8')
				frame2 = cv2.flip(frame2, -1)
				frame3 = cv2.flip(frame3, -1)
				cv2.putText(frame1, f'Camera \nnot working', (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (145, 100, 245), 2, cv2.LINE_AA)
				frame_con = np.concatenate((frame1, frame2, frame3), axis = 1)
			else:            
				frame2 = cv2.resize(frame2, (426, 720))
				frame1 = cv2.flip(frame1, -1)
				frame2 = cv2.flip(frame2, -1)
				frame3 = np.zeros([frame2.shape[0], frame2.shape[1], 3], dtype = 'uint8')
				cv2.putText(frame1, f'Camera \nnot working', (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (145, 100, 245), 2, cv2.LINE_AA)
				frame_con = np.concatenate((frame1, frame2, frame3), axis = 1)
				# cv2.imwrite(f'lhs_image/{count}.png',frame_con)
		# if count_new % 100 == 0:
		# 	count = 0
		# 	start = True
		# 	print('key is pressed')
		data = ser.readline()
		print('data-------------------------------------------',data)
		start_ = data.decode()
		print('statr-------------------------',start_)

		if(start_ == "START\r\n"):
			print("Time to start algo...")
			# ser.write(b'R')
			print('key is pressed')
			img=frame_con
			# 1
			img1=img[355:416,10:42]
			hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
			mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
			res1 = cv2.bitwise_and(img1,img1, mask= mask1)
			n_white_pix1 = np.sum(img1 == 255)
			print(n_white_pix1 )
			if n_white_pix1>200:
				flag_list.append('OK')
				img=cv2.rectangle(img, (10, 355), (42, 416), (255,0,0), 2)  # White
				img = cv2.putText(img, '1', (15, 350), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')


			#2
			img2=img[365:440,174:220]
			hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
			lower_blue = np.array([110,50,50])
			upper_blue = np.array([130,255,255])
			mask2 = cv2.inRange(hsv2, lower_blue, upper_blue)
			res2 = cv2.bitwise_and(img2,img2, mask= mask2)
			n_white_pix2 = np.sum(img2 == 255)
			print(n_white_pix2 )
			if n_white_pix2>200:
				flag_list.append('OK')
				img=cv2.rectangle(img, (174, 365), (220, 440), (255,0,0), 2)
				img = cv2.putText(img, '2', (179, 360), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			#3
			img3=img[365:437,288:347]
			hsv3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
			lower_blue = np.array([110,50,50])
			upper_blue = np.array([130,255,255])
			mask3 = cv2.inRange(hsv3, lower_blue, upper_blue)
			res3 = cv2.bitwise_and(img3,img3, mask= mask3)
			n_white_pix3 = np.sum(img3 == 255)
			# im_h3 = cv2.hconcat([img3, mask3,res3])
			# cv2.imshow('img3',img3)
			# cv2.imshow('mask3',mask3)
			# cv2.imshow('res3',res3)
			print(n_white_pix3 )
			if n_white_pix3>500:
				flag_list.append('OK')
				img=cv2.rectangle(img, (288, 365), (347, 437), (255,0,0), 2)
				img = cv2.putText(img, '3', (293, 360), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			#4
			img4=img[349:409,411:439]
			hsv4 = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)
			mask4 = cv2.inRange(hsv4, lower_blue, upper_blue)
			res4 = cv2.bitwise_and(img4,img4, mask= mask4)
			n_white_pix4 = np.sum(img4 == 255)
			print(n_white_pix4 )
			if n_white_pix4>200:
				flag_list.append('OK')
				img=cv2.rectangle(img, (411, 349), (439, 409), (255,0,0), 2)
				img = cv2.putText(img, '4', (416, 344), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			#5
			img5=img[365:437,288:347]
			hsv5 = cv2.cvtColor(img5, cv2.COLOR_BGR2HSV)
			mask5 = cv2.inRange(hsv5, lower_blue, upper_blue)
			res5 = cv2.bitwise_and(img5,img5, mask= mask5)
			n_white_pix5 = np.sum(img5 == 255)
			print(n_white_pix5)
			if n_white_pix5>200:
				flag_list.append('OK')
				img=cv2.rectangle(img, (441, 341), (466, 446), (255,0,0), 2)
				img = cv2.putText(img, '5', (446, 336), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			#6
			img6=img[334:447,488:525]
			hsv6 = cv2.cvtColor(img6, cv2.COLOR_BGR2HSV)
			mask6 = cv2.inRange(hsv6, lower_blue, upper_blue)
			res6 = cv2.bitwise_and(img6,img6, mask= mask6)
			n_white_pix6 = np.sum(img6 == 255)
			print(n_white_pix6)
			if n_white_pix6>200:
				flag_list.append('OK')
				img=cv2.rectangle(img, (488, 334), (525, 447), (255,0,0), 2)
				img = cv2.putText(img, '6', (493, 329), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')


			#7
			img7=img[347:442,580:600]
			hsv7 = cv2.cvtColor(img7, cv2.COLOR_BGR2HSV)
			mask7 = cv2.inRange(hsv7, lower_blue, upper_blue)
			res7 = cv2.bitwise_and(img7,img7, mask= mask7)
			n_white_pix7 = np.sum(img7 == 255)
			print(n_white_pix7)
			if n_white_pix7>200:
				flag_list.append('OK')
				img=cv2.rectangle(img, (580, 347), (600, 442), (255,0,0), 2)
				img = cv2.putText(img, '7', (585, 342), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')


			#8
			img8=img[332:413,602:644]
			hsv8 = cv2.cvtColor(img8, cv2.COLOR_BGR2HSV)
			mask8 = cv2.inRange(hsv8, lower_blue, upper_blue)
			res8 = cv2.bitwise_and(img8,img8, mask= mask8)
			n_white_pix8 = np.sum(img8 == 255)
			print(n_white_pix8)
			if n_white_pix8>200:
				flag_list.append('OK')
				img=cv2.rectangle(img, (602, 332), (644, 413), (255,0,0), 2)
				img = cv2.putText(img, '8', (607, 327), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')


			#9
			img9=img[300:432,669:722]
			hsv9 = cv2.cvtColor(img9, cv2.COLOR_BGR2HSV)
			mask9 = cv2.inRange(hsv9, lower_blue, upper_blue)
			res9 = cv2.bitwise_and(img9,img9, mask= mask9)
			n_white_pix9= np.sum(img9 == 255)
			print(n_white_pix9)
			if n_white_pix9>200:
				flag_list.append('OK')
				img=cv2.rectangle(img, (669, 300), (722, 432), (255,0,0), 2)
				img = cv2.putText(img, '9', (674, 295), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			#10
			img10=img[359:424,806:845]
			hsv10 = cv2.cvtColor(img10, cv2.COLOR_BGR2HSV)
			mask10 = cv2.inRange(hsv10, lower_blue, upper_blue)
			res10 = cv2.bitwise_and(img10,img10, mask= mask10)
			n_white_pix10 = np.sum(img10 == 255)
			print(n_white_pix10)
			if n_white_pix10>200:
				flag_list.append('OK')
				img=cv2.rectangle(img, (806, 359), (845, 424), (255,0,0), 2)
				img = cv2.putText(img, '10', (811, 354), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			#11
			img11=img[405:444,928:961]
			hsv11 = cv2.cvtColor(img11, cv2.COLOR_BGR2HSV)
			mask11 = cv2.inRange(hsv11, lower_blue, upper_blue)
			res11 = cv2.bitwise_and(img11,img11, mask= mask11)
			n_white_pix11 = np.sum(img11 == 255)
			print(n_white_pix11)
			if n_white_pix11>100:
				flag_list.append('OK')
				img=cv2.rectangle(img, (928, 405), (961, 444), (255,0,0), 2)
				img = cv2.putText(img, '11', (933, 400), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			#12
			img12=img[400:453,968:995]
			hsv12 = cv2.cvtColor(img12, cv2.COLOR_BGR2HSV)
			mask12 = cv2.inRange(hsv12, lower_blue, upper_blue)
			res12 = cv2.bitwise_and(img12,img12, mask= mask12)
			n_white_pix12 = np.sum(img12 == 255)
			print(n_white_pix12)
			if n_white_pix12>200:
				flag_list.append('OK')
				img=cv2.rectangle(img, (968, 400), (995, 453), (255,0,0), 2) # white
				img = cv2.putText(img, '12', (973, 395), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			#13
			img13=img[389:469,1007:1035]
			hsv13 = cv2.cvtColor(img13, cv2.COLOR_BGR2HSV)
			mask13 = cv2.inRange(hsv13, lower_blue, upper_blue)
			res913 = cv2.bitwise_and(img13,img13, mask= mask13)
			n_white_pix13 = np.sum(img13 == 255)
			print(n_white_pix13)
			if n_white_pix13>100:
				flag_list.append('OK')
				img=cv2.rectangle(img, (1007, 389), (1035, 469), (255,0,0), 2)
				img = cv2.putText(img, '13', (1013, 383), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			#14
			img14=img[395:458,1045:1077]
			hsv14 = cv2.cvtColor(img14, cv2.COLOR_BGR2HSV)
			mask14 = cv2.inRange(hsv14, lower_blue, upper_blue)
			res14 = cv2.bitwise_and(img14,img14, mask= mask14)
			n_white_pix14 = np.sum(img14 == 255)
			print(n_white_pix14)
			if n_white_pix14>100:
				flag_list.append('OK')
				img=cv2.rectangle(img, (1045, 395), (1077, 458), (255,0,0), 2)
				img = cv2.putText(img, '14', (1050, 390), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			#15
			img15=img[391:461,1099:1129]
			hsv15 = cv2.cvtColor(img15, cv2.COLOR_BGR2HSV)
			mask15 = cv2.inRange(hsv15, lower_blue, upper_blue)
			res15 = cv2.bitwise_and(img15,img15, mask= mask15)
			n_white_pix15 = np.sum(img15 == 255)
			print(n_white_pix15)
			if n_white_pix15>100:
				flag_list.append('OK')
				img=cv2.rectangle(img, (1099, 391), (1129, 461), (255,0,0), 2)
				img = cv2.putText(img, '15', (1104, 386), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			#16
			img16=img[406:460,1130:1151]
			hsv16 = cv2.cvtColor(img16, cv2.COLOR_BGR2HSV)
			mask16 = cv2.inRange(hsv16, lower_blue, upper_blue)
			res16 = cv2.bitwise_and(img16,img16, mask= mask16)
			n_white_pix16 = np.sum(img16 == 255)
			print(n_white_pix16)
			if n_white_pix16>100:
				flag_list.append('OK')
				img=cv2.rectangle(img, (1130, 406), (1151, 460), (255,0,0), 2)
				img = cv2.putText(img, '16', (1135, 401), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			img17=img[417:477,1158:1182]
			hsv17 = cv2.cvtColor(img17, cv2.COLOR_BGR2HSV)
			mask17 = cv2.inRange(hsv17, lower_blue, upper_blue)
			res17 = cv2.bitwise_and(img17,img17, mask= mask17)
			n_white_pix17 = np.sum(img17 == 255)
			print(n_white_pix17)
			if n_white_pix17>200:
				flag_list.append('OK')
				img=cv2.rectangle(img, (1158, 417), (1182, 477), (255,0,0), 2)
				img = cv2.putText(img, '17', (1163, 412), font, fontScale, color, thickness, cv2.LINE_AA)
			else:
				flag_list.append('Not OK')

			# print(flag_list)
			alerts_=[]
			count+=1

			for i in range(len(flag_list)):
				dict_={}                        
				id1=i+1
				flag=flag_list[i]
				# print(flag)
				if id1==0 or id1==12:
					color_='white'
				else:
					color_='blue'
				time = datetime.now()
                
                
				current_time = time.strftime("%H:%M:%S %d/%m/%Y") 
				track.var2 = current_time
                
				alerts_.append({'id': id1, 'alert': flag, 'time_': current_time, 'tape_id': '310', 'color': 'blue'})
				
				sql = "INSERT INTO alert(alert,time_, tape_id, color) VALUES(%s, %s, %s, %s)"
				data = (flag, current_time, id1, color_)
				conn = mysql.connect()
				cursor = conn.cursor()
				cursor.execute(sql, data)
				conn.commit()
				cursor = conn.cursor(pymysql.cursors.DictCursor)
				track.var3 = img
			track.variable=alerts_
			print(alerts_)
				# cv2.waitKey(0)
	return jsonify('Detection complete')


@app.route('/img', methods = ['GET'])
@cross_origin()
def img():
	j=jsonify("hi------------------------")
	return j

def video3():

	while True:
		try:
			img_ = track.var3
		except:
			img_ = np.zeros((720, 1280, 3), np.uint8)       
		ret,buffer=cv2.imencode('.jpg',img_)
		Frame=buffer.tobytes()
		yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + Frame + b'\r\n')

@app.route('/img1')
@cross_origin()
def img1():
	return Response(video3(),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/alert', methods = ['GET'])
@cross_origin()
def alerts():
	_alert = track.var
	alert_ = jsonify(_alert)
	return alert_

@app.route('/all', methods = ['GET'])
@cross_origin()
def all():
	# return jsonify('hi')
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	_time = track.var2
	rows=track.variable
# 	if cursor.execute("SELECT * FROM alert WHERE time_ = '"+_time+"' LIMIT 17"):
# 		rows = cursor.fetchall()
	# print(rows)
        
	resp = jsonify(rows)
	return resp


@app.route('/date', methods = ['GET'])
@cross_origin()
def date():
	_time = track.var2
	time_ = jsonify(_time)
	return time_
	
# if __name__=="__main__":

#     print('')
#     app.run(debug=True)
	
@app.errorhandler(404)
def not_found(error=None):
	message = {
		'status': 404,
		'message': 'Not Found: ' + request.url,
	}
	resp = jsonify(message)
	resp.status_code = 404

	return resp
		
if __name__ == "__main__":
	app.run()
