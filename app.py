from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return "flask app is running and I made this changes to check" \
           "whether it is visible on circle ci or not"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)