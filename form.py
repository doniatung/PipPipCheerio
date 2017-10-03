from flask import Flask, render_template, request

my_app = Flask(__name__)

@my_app.route('/', methods = ['GET', 'POST'])
def root():
    #print request.headers
    #print request.method
    #print request.args
    #print request.form
    return render_template('form.html') 

@my_app.route('/response', methods = ['POST', 'GET'])
def greeting():
    return render_template('salutations.html',name = request.form['data'], method = request.method)

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
