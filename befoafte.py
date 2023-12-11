from flask import Flask
peach = Flask(__name__)

@peach.before_request
def before_request_func():
    values = {"before_request": "running"}
    print('before request')
    # return values

@peach.after_request
def after_request_func(response):
    print('After request')
    print(response)
    return response

@peach.route("/")
def index():
    valus = {"index": "running"}
    print('Index running')
    return valus





if __name__ == "__main__":
    peach.run()


