Setup

##	Follow these steps to make sure app.js is Running:
	1) Download NodeJS and install it.
	2) Open the terminal inside the cloned folder("../sky"), we need libraries, so type: 
				npm install express
				npm install ejs
	3) Now in terminal, type 
				node sky.js
	4) If everything works fine, You should get a message that looks like 
				SERVER IS UP at http://localhost:8080/
	5) Don't close ter terminal.


##	Follow these steps to make sure server.py is Running:
	1) Install the latest version of Python. 
				Python 3.x, not Python 2.x
	2) Install pip for python 3.
	3) Make a virtual environment inside the folder.
	4) Now using pip, install the libraries. So open the terminal and type:
				pip install bottle
				pip install opencv-python
				pip install scikit-image
				pip install scipy
	5) Once All libraries are installed, run the server.
				python server.py
	6) If done correctly, you will get the message on the terminal as
				Listening on http://localhost:3000/
	7) Don't close the terminal.



##  What to do next:
	1) Go to SERVER IS UP at http://localhost:8888/
	2) Enter anything there.
	3) Try this 
				http://www.gstatic.com/tv/thumb/persons/835149/835149_v9_bb.jpg (Don't judge me.)
	4) If everything went fine, you should get this
				{"status": "success","data": {"url": "http://www.gstatic.com/tv/thumb/persons/835149/835149_v9_bb.jpg","faces": "1" },"message": null}
