- [x] create a new directory
- [ ] inside the directory create a virtual environment by running
        pipenv install flask pymysql
- [ ] activate the virtual environment
        pipenv shell
- [x] create root [server.py](server.py)
- [x] Boilerplate:
        from flask import Flask, render_template, redirect, request, session
        app = Flask(__name__)
        app.secret_key = ""

        @app.route('/')
        def index():
        return render_template('index.html')

        if __name__=="__main__":
                app.run(debug=True)

- [ ] start the application by running
        python server.py
- [ ] open browser and navigate to localhost:5000
- [x] create directory [templates](templates/index.html) with html index file