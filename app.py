from flask import Flask, request, jsonify
app = Flask(__name__)

from gtrends.gtrends import APIClient


@app.route('/')
def index():
    """
    """
    api_client = APIClient()
    res = api_client.get_gtrends()

    return jsonify(res)


if __name__ == "__main__":
    app.run()
