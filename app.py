from flask import Flask, request, render_template
from waitress import serve
import pandas as pd
import requests
app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello World!"
# @app.route('/custom')
# def custom_hello():
#     return "Hello Custom World!"
df = pd.read_excel('Certificates_holders.xlsx')
# df.to_excel('Certificates_holders.xlsx', index=None)
  
  
# route to html page - "table"
@app.route('/')
@app.route('/table')
def table():
    
    # converting csv to html
    robj = requests.get("https://fakestoreapi.com/products")
    lod = eval(robj.content)
    data = pd.DataFrame(lod)
    return render_template('table.html', tables=[data.to_html()], titles=[''])

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
