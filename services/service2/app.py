from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return {"message": "Hello from Service 2!"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)