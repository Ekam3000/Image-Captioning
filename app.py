from flask import Flask, render_template, redirect, request

import caption_it

# __name__ == __main__
app = Flask(__name__)


@app.route('/')
def hello():
	return render_template("index.html")


@app.route('/', methods= ['POST'])
def marks():
	if request.method == 'POST':
		f = request.files['userfile'] #receiving files by name 'userfile'
		path = "./static/{}".format(f.filename)# ./static/images.jpg  
		f.save(path) #saving the path, in static folder 

		caption = caption_it.caption_this_image(path)  # when we are importing caption_it module and using function of that module , then a error will occur on the web , to overcome that error we have included line 22 , line 28 in caption_it
		
		result_dic = {
		'image' : path,
		'caption' : caption
		}
	return render_template("index.html", your_result =result_dic) # both image and caption will be displayed in the web

if __name__ == '__main__':
	# app.debug = True
	# due to versions of keras we need to pass another paramter threaded = Flase to this run function
	app.run(debug = False, threaded = False)


#run this file not index.html
# Running on http://127.0.0.1:5000