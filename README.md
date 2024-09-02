# WSAA-BIG-PROJECT

## FishKeeping Application Log

## Project Task
> Write a program that demonstrates that you understand creating and consuming
RESTful APIs

## Overview

For this project, I decided to do a simple, yet for me useful, Fishkeeping Application Log. The application is a web-based tool built using Flask that allows users to manage, document and log fish and aquarium details which is stored in a SQLite database. 

## Feature Set

**Fish Management and Tank Management:** Add, edit, delete and view your entries in real-time. Specifically, the options are split in two separate tables specific to either fish or aquaria. In the fish table, you can Add New Fish, Species Name, Date Added and Notes. For the Aquaria,  you can Add New Tank, Name, Volume and Description. 

**Data**: All of the Data is stored in a SQLLite database which ensures everything is retained, when closed etc. 

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

- **Procfile**: Needed when deploying the app Render.com, which I found more straight forward than PythonAnywhere. 

- **Templates/index.html**: The HTML neededfor the web interface. 



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

Start the Flask server by opening the server.py file and typing python server.py in the terminal. From this, the url - http://127.0.0.1:5000 will be clickable. Click it and itll take you to thw web application. 

## Deployment

I deployed this app using Render.com, as i found its UI more intuitive than alternatives. 

**Render Deployment Steps**


	

 




