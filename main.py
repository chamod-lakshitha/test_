from flask import Flask, render_template

app = Flask('__name__')
 
#Initial route  
@app.route('/')
def index():
    return(render_template('index.html'))

#Home route
@app.route('/home')
def home():
    return(render_template('home.html'))

if __name__ == '__main__':
    app.run(debug=True)