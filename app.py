from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Site under construction'

@app.route('/0day0')
def poc():
    return 'Another Subdomain Takeover PoC By 0day0 AKA Rounak'

if __name__ == '__main__':
    app.run(debug=True)
