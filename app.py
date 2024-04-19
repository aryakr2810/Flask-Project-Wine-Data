from flask import Flask, render_template
import sqlite3 
import csv 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    # Connect to SQLite database
    con = sqlite3.connect('Wine.db')
    cursor = con.cursor()

    # Check if the wine table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='wine';")
    table_exists = cursor.fetchone()

    if not table_exists:
        # Create wine table if it does not exist
        cursor.execute("""CREATE TABLE wine (
                            wine_index TEXT PRIMARY KEY,
                            pH TEXT,
                            residual_sugar TEXT,
                            sulphates TEXT,
                            density TEXT,
                            chlorides TEXT,
                            alcohol TEXT,
                            quality TEXT 
                        );""")

        # Insert data from CSV into the wine table
        with open("wine.csv") as f:
            data = csv.reader(f)
            for row in data:
                if row[0] == 'wine_index':
                    continue
                cursor.execute("INSERT INTO wine VALUES (?, ?, ?, ?, ?, ?, ?, ?)", row)

        con.commit()

    # Fetch data from the wine table
    cursor.execute("SELECT * FROM wine")
    wine_data = cursor.fetchall()

    con.close()

    # Pass wine data to the template
    return render_template("data.html", wine=wine_data)

if __name__ == "__main__":
    app.run(debug=True)