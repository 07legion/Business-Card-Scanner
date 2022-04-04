# -*- coding: utf-8 -*-
# @Author: Amish
# @Date:   2021-02-25 16:48:55
# @Last Modified by:   Amish Sharma
# @Last Modified time: 2021-03-03 16:15:48

from flask import Flask, render_template, request, jsonify
import requests,  os
from modules import main
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
	file = request.files['file']
	if file:
		filename = secure_filename(file.filename)
		file.save(os.path.join("./uploaded_images", filename))
		ret = main.main_func(filename)
		return jsonify({"Email(s)": ret[0], "Organization" : ret[1], "Website(s)" : ret[2], 
						"Name" : ret[3], "Designation" : ret[4], "Mobile": [ret[5][1]], "Office" : [ret[5][0]],
						"Direct" : [ret[5][2]], "Fax" : [ret[5][3]], "Address" : ret[6][0], "Zipcode" : ret[6][1], 
						"City" : ret[6][2], "State" : ret[6][3], "Country" : ret[6][4] })

if __name__ == '__main__':
	app.run(debug = True,  host='0.0.0.0', port=5000)
	#server.run(debug = True)