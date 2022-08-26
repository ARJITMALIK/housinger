from email.mime import base
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

mdl = pickle.load(open('mdl.pkl', 'rb'))

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
  area = int(request.form.get('area'))
  bedrooms = int(request.form.get('bedrooms')) 
  bathrooms =int(request.form.get('bathrooms')) 
  stories = int(request.form.get('stories')) 
  mainroad = int(request.form.get('mainroad')) 
  guestroom = int(request.form.get('guestroom')) 
  basement = int(request.form.get('basement')) 
  hotwater = int(request.form.get('hotwater'))
  air = int(request.form.get('air'))
  parking = int(request.form.get('parking'))
  prefarea = int(request.form.get('prefarea'))
  furnish = int(request.form.get('furnish'))

  results = mdl.predict([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwater, air, parking, prefarea, furnish]])
  output = round(results[0], 3)
  return render_template('result.html', pred=f'{output}')

if __name__ == '__main__':
  app.run(debug=True)
