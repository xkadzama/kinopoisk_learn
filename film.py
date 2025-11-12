from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/find_film', methods=['GET', 'POST'])
def show_film():
	if request.method == 'POST':
		name_movie = request.form.get('name_movie')
		responses = requests.get(
			f'https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={name_movie}&page=1',
			headers={
				'X-API-KEY': '3cca8764-1437-44db-ac92-8ff5f6fac24d',
				'Content-Type': 'application/json',
			}
		)

		data = responses.json()['films'][0]
		m_name = data.get('nameRu')
		m_poster = data.get('posterUrl')
		m_rating = data.get('rating')
		m_year = data.get('year')
		info = [
			{'name': m_name, 'poster': m_poster, 'rating': m_rating, 'year': m_year}
		]
		return render_template('find_film.html', info=info)







if __name__ == '__main__':
	app.run(debug=True)