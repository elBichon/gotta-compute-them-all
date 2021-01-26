import pandas as pd
import utils
from flask import Flask, jsonify
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
@app.route('/query-pokemon')
def query():
	TYPES_LIST = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fight','fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison','psychic', 'rock', 'steel', 'water']
	try:
		df = pd.read_csv('https://raw.github.com/elBichon/gotta-compute-them-all/master/post_treat_pokemon.csv')
		pokemon_number = int(request.args.get('pokemon_number'))
		pokemon_number = utils.test_pokemon_number(df,pokemon_number)
		return utils.build_answer(df, pokemon_number, TYPES_LIST)
	except:
		return '''<h1> Something failed 2</h1>'''

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)


#http://127.0.0.1:5000/query-pokemon?pokemon_number=100
