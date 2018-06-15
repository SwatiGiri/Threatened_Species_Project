import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from sqlalchemy import MetaData
from sqlalchemy import inspect
from sqlalchemy import Table

import pandas as pd


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
db_path = "sqlite:///threatened_species.db"
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/threatened_species")
def get_otu_ids():
    # defining metatdata
    metadata = MetaData()
    metadata.reflect(bind=db.engine)
    # getting the samples table     
    samples = metadata.tables['spec_table']
    # converting table into something we can actually use  
    res = db.session.query(samples)
    # Final data
    data = res
    #getting the data
    return jsonify(data[0 :])

if __name__ == "__main__":
    app.run(debug=True)  
    
