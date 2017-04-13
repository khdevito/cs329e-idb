from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.

URLs that will call the index() function if running app.py on localhost:
http://localhost:5000/
http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
    return render_template('index.html') # located in templates/

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/bands')
def bands():
    return render_template('bands.html')

@app.route('/bandsP2')
def bandsP2():
    return render_template('bandsP2.html')

@app.route('/bandsP3')
def bandsP3():
    return render_template('bandsP3.html')

@app.route('/venues')
def venues():
    return render_template('venues.html')

@app.route('/venuesP2')
def venuesP2():
    return render_template('venuesP2.html')

@app.route('/venuesP3')
def venuesP3():
    return render_template('venuesP3.html')

@app.route('/festivals')
def festivals():
    return render_template('festivals.html')

@app.route('/festivalsP2')
def festivalsP2():
    return render_template('festivalsP2.html')

@app.route('/festivalsP3')
def festivalsP3():
    return render_template('festivalsP3.html')

@app.route('/bio/<bio_name>')
def bio(bio_name):
    return render_template('biofolder/bio_' + bio_name + '.html')

if __name__ == '__main__':
    app.run('138.197.91.16','80') # Run application
