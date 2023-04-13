from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = ""
from user import User

# This route shows all users on the home page
@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html',users = users)

# This route takes you to the form
@app.route("/new")
def new():
    return render_template('new.html')

# This route processes the form and redirects to the main page
@app.route("/create", methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/')

#READ ONE
@app.route('/users/<int:id>')
def show(id):
    user = User.get_user(id)
    return render_template('show.html', user=user)

# This route displays the form
@app.route("/users/<int:id>/edit")
def edit(id):
    user = User.get_user(id)
    return render_template('edit.html', user=user)

#UPDATE - Processing
@app.route('/users/<int:id>/update',methods=['POST'])
def update(id):
    User.update(request.form)
    return redirect(f"/users/{request.form['id']}")


#*****************
#DELETE
@app.route('/users/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/')


if __name__=="__main__":
        app.run(debug=True)

