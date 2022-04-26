'''
References:
Table: https://physionet.org/content/gait-maturation-db/1.0.0/data/table.csv
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_pickle.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html
https://joblib.readthedocs.io/en/latest/why.html
https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
https://towardsdatascience.com/using-joblib-to-speed-up-your-python-pipelines-dd97440c653d
https://towardsdatascience.com/how-to-easily-deploy-machine-learning-models-using-flask-b95af8fe34d4
'''

from flask import Flask, render_template, request

import numpy as np
import os
from datetime import datetime as dt
import datetime
import shutil

app = Flask(__name__)
app.debug = True

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=80)

@app.route('/')
def homepage():
    return render_template("main.html")




@app.route('/cpp/', methods=['GET', 'POST'])
def cpp():
    t=""
    my_path = os.path.dirname(__file__)
    req_type = request.method
    if req_type == 'GET':
        return render_template("cpp.html")
    else:
        symbol = request.form['stock'] 
        t = symbol

        if request.form['submit_button'] == 'Summary':
            if os.path.exists(my_path + '\\static\\images\\'+ symbol +'_stock_summary.jpg'):
                shutil.copy(my_path + '\\static\\images\\'+ symbol +'_stock_summary.jpg',my_path + '\\static\\images\\stock_forecast.jpg')

        else:
            if os.path.exists(my_path + '\\static\\images\\'+ symbol +'_stock_forecast.jpg'):
                shutil.copy(my_path + '\\static\\images\\'+ symbol +'_stock_forecast.jpg',my_path + '\\static\\images\\stock_forecast.jpg')
           
    return render_template("cpp.html", p = t)





