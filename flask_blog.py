from flask import Flask,render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='57aae01cb47f3437c6a9e82c01f56480'


posts = [

    {
        'author': 'Amit' ,
        'title': 'Owner',
        'content':'First post content',
        'date_posted': '31/08/2023'
    },

    {
        'author': 'Noam' ,
        'title': 'Teacher',
        'content':'Second post content',
        'date posted': '31/08/2023'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)



@app.route("/about")
def about():
    return render_template('about.html',title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form =form)



@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form =form)




if __name__ == '__main__':
    app.run(debug=True)