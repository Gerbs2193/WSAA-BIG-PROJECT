# WSAA-BIG-PROJECT - Gerard Ball


## FishKeeping Application Log

## Project Task
> Write a program that demonstrates that you understand creating and consuming
RESTful APIs

## Overview

For this project, I decided to do a simple, yet for me useful, Fishkeeping Application Log. The application is a web-based tool built using Flask that allows users to manage, document and log fish and aquarium details which is stored in a SQLite database. 

## Feature Set

**Fish Management and Tank Management:** Add, edit, delete and view your entries in real-time. Specifically, the options are split in two separate tables specific to either fish or aquaria. In the fish table, you can Add New Fish, Species Name, Date Added and Notes. For the Aquaria,  you can Add New Tank, Name, Volume and Description. 

**Data**: All of the Data is stored in a SQLite database which ensures everything is retained, when closed etc. 

**Responsive Web Interferface**
The interface is dynamic and was built with HTML, CSS and JAVA which interact with the Flask

**Structure**

```
WSAA-BIG-PROJECT/
│
├── fishDAO.py
├── fishkeeping.db
├── server.py
├── requirements.txt
├── Procfile
├── README.md
└── templates/
    └── index.html
```


- **Server.py**: This is the Flask app server which handles the API requests and also renders us the web page.

- **FishDAO.py**: Here is the Data Access Object which is for interacting with SQLite.

- **fishkeeping.db**: Where all the data is stored

- **requirements.txt**: All necessary python dependancies to run the app in VSCode and Render when hosting. 

- **Procfile**: Needed when deploying the app on Render.com, which I found more straight forward than PythonAnywhere. 

- **Templates/index.html**: The HTML needed for the web interface. 



## Requirements

- Python 3.10 or higher (was chosen as the version when deploying on Render)

- Flask

- SQLite

- jQuery and Bootstrap were included via CDN for easy DOM manipulation and to create a responsive clean UI without much fuss

## Installation

- **Clone** my repo with git clone https://github.com/Gerbs2193/WSAA-BIG-PROJECT.git
cd WSAA-BIG-PROJECT

- **Install all Dependencies**. As per the requirements.txt file, you will need the following:

	**Flask:** The core framework used to create and manage the web application.

	**Flask-SQLAlchemy:** An extension for Flask that simplifies the integration with SQL databases like when using SQLite 


## Running the App

Start the Flask server by opening the server.py file and typing python server.py in the terminal. From this, the url - http://127.0.0.1:5001 will be generated. Click it and it'll take you to the web application. 

## Deployment

I deployed this app using Render.com, as I found its UI more intuitive than alternatives. 

**Render Deployment Steps**

### Live Application
You can access the live version of the application here: [Fishkeeping Application](https://wsaa-big-project.onrender.com/)

**Note:** The application is hosted on Render's free tier, which means it may take a few moments (or several moments indeed) to start up if it hasn't been accessed recently. Seriously, it took minutes at one stage. 

**How to set up in Render:**

- Create a Render Account

- Create a New Web Service: Connect it to your GitHub repository for easier file managing

- Select Environment: Choose Python 3.10.

- Set the Start Command: Use python server.py as the start command.


- Deploy: Render will then automatically detect the Procfile and deploy your app.

## Usage

Once on the FishKeeping browser app, use the interface to freely manage your fish and tanks to you hearts desire. 

## License

Free to use

## Sources

 
- All about Flask - https://flask.palletsprojects.com/en/2.1.x/quickstart/

- https://flask.palletsprojects.com/en/2.1.x/patterns/sqlalchemy/

- https://realpython.com/learning-paths/flask-by-example/

- https://ericbernier.com/flask-restful-api

- Labs in relation to the project provided by my Lecturer. 

