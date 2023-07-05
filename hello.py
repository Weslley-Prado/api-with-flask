from flask import Flask

app = Flask(__name__)


@app.route("/<numerous>", methods=['GET','POST'])
def hello(numerous):
    return f'Create {numerous} using Flask'


if __name__ == "__main__":
    app.run()
