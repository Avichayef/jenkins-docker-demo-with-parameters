from flask import Flask
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello():
    app.logger.info('Received request on root endpoint')
    return {"message": "Hello from Service 2!"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.logger.info(f'Starting service on port {port}')
    app.run(host='0.0.0.0', port=port, debug=False)