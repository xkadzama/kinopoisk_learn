from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
	responses = requests.get(
		'https://kinopoiskapiunofficial.tech/api/v2.2/films/313',
		headers={
			'X-API-KEY': '3cca8764-1437-44db-ac92-8ff5f6fac24d',
			'Content-Type': 'application/json',
		}
	)

	data = responses.json()
	poster_url = data.get('posterUrl')
	return f'<img src="{poster_url}">'





if __name__ == '__main__':
	app.run(debug=True)