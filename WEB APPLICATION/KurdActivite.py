from flask import Flask, render_template

app = Flask(__name__, template_folder='KuTE', static_folder='KuST')

@app.route('/')
@app.route('/Home')
def home():
    return render_template('HHome.html', name='Home')

@app.route('/Contact')
def contact():
    return render_template('CContact.html', name='Contact')

@app.route('/About')
def about():
    return render_template('AAbout.html', name='About')





if __name__ == '__main__':
    app.run(debug=True ,port=12323)