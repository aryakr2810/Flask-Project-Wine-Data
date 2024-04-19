# THE FLASK RED WINE DATA APPLICATION

## Overview

### The application we created using Flask displays the red wine quality data stored in an SQLite Database. The application shows the score of Wine Quality from 0 to 10 obtained from analysing various characteristics of red wine.


## Features

### Home Page : Starts with a welcome message. The home page shows the information about the research paper from we which we took our red wine data. Background, findings and conclusion is given.
### About Page : Provides information about the dataset - an introduction, the attribute names, the attribute count, missing data and the number of instances. The citation is displayed on this page. 
### Data Page : Displays The Red Wine Quality Data.

## Installation

### Clone the Repository: git clone https://github.com/aryakr2810/Flask-Project-Wine-Data.git
### Install Dependencies: pip install -r requirements.txt
### Run the Application: flask run   


## Usage

### Navigate to http://localhost:5000/ in your web browser to access the home page.
### Click on the "Home" button in the navigation bar to know more about The Research Article from which we took the data.
### Click on the "About" button in the navigation bar to learn more about The Red Wine Quality Dataset.
### Click on the "Data" button to view wine data retrieved from the Sqlite3 Database.

## Project Structure

### app.py: Main Flask application file containing route definitions.
### templates: Directory containing HTML templates for rendering web pages.
### static: Directory containing the common styles.css cascading stylesheet 
### Wine.db: SQLite database file containing wine data table.
### wine.csv: CSV file containing wine data to be imported into the database.