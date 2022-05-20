from flask import Flask, request, render_template
from waitress import serve
# import pandas as pd
import requests
app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello World!"
# @app.route('/custom')
# def custom_hello():
#     return "Hello Custom World!"
# df = pd.read_excel('Certificates_holders.xlsx')
# df.to_excel('Certificates_holders.xlsx', index=None)
  
  
# route to html page - "table"
@app.route('/')
@app.route('/table')
def table():
    return "Hello"
    # converting csv to html
    #robj = requests.get("https://fakestoreapi.com/products")
    #lod = eval(robj.content)
    # data = pd.DataFrame(lod)
    # np_lod = np.array(lod)
    # np_lod.reshape(-1,4)
    #return render_template('table.html', lod=lod)

if __name__ == '__main__':
    # app.run()
    serve(app, host='0.0.0.0', port=8080)
    # app.run(host = '0.0.0.0')
