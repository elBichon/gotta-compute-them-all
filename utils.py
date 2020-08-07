import pandas as pd
import utils
from flask import Flask, jsonify
from flask import Flask, render_template, request


def get_target_data(df, pokemon_number):
	try:
		if isinstance(df, int) == False and len(df) != 0:
			df = df.loc[df['pokedex_number'] == pokemon_number]
			return df
		else:
			return False
	except:
		return False


def get_target_weakness(df):
	try:
		if isinstance(df, int) == False and len(df) != 0:
			weak_list = df[['bug', 'dark', 'dragon', 'electric', 'fairy', 'fight','fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison','psychic', 'rock', 'steel', 'water']].values.tolist()[0]
			max_value = max(weak_list)
			max_index = []
			i = 0
			for value in weak_list:
				if value == max_value:
					max_index.append(i)
				else:			
					pass
			i += 1
			return max_index
		else:
			return False
	except:
		return 	False


def clean_target_data(df):	
	try:
		if isinstance(df, int) == False and len(df) != 0:
			df = df[['classfication', 'attack','height_m', 'name', 'pokedex_number', 'type1', 'weight_kg','generation', 'is_legendary', 'image', 'type2']]
			df['target'] = 1
			return df
		else:
			return False
	except:
		return False


def create_output(df, df1, max_index, TYPES_LIST):
	try:
		if isinstance(df, int) == False and len(df) != 0 and len(max_index) > 0 and len(TYPES_LIST) > 0:
			for index in max_index:
				df = df.loc[df['is_legendary'] != 1]
				df2 = df.loc[df['type1'] == str(TYPES_LIST[index])].sort_values(by='attack', ascending=False, na_position='first')
				df2 = df2[['classfication', 'attack','height_m', 'name', 'pokedex_number', 'type1', 'weight_kg','generation', 'is_legendary', 'image', 'type2']].head(5)
				df2['target'] = 0
				df1 = df1.append(df2)
			df1 = df1.drop_duplicates()
			return df1
		else:
			return False
	except:
		return False

def send_query_answer(df):
	try:
		if isinstance(df, int) == False and len(df) != 0:
			pokemon_data = {"id":df.pokedex_number.values.tolist(),'classfication':df.classfication.values.tolist(), 'attack':df.attack.values.tolist(),'height_m':df.height_m.values.tolist(), 'name':df.name.values.tolist(), 'type1':df.type1.values.tolist(), 'type2':df.type2.values.tolist(),'weight_kg':df.weight_kg.values.tolist(),'generation':df.generation.values.tolist(), 'is_legendary':df.is_legendary.values.tolist(), 'image':df.image.values.tolist()}
			return pokemon_data
		else:
			return False
	except:
		return False


def check_dataframe(df):
	try:
		if isinstance(df, int) == False and len(df) != 0:
			return True
		else:
			return False
	except:
		return False


def test_pokemon_number(df,pokemon_number):
	try:
		if check_dataframe(df) == True:
			if  isinstance(pokemon_number, int) == True and pokemon_number > 0 and pokemon_number < len(df.pokedex_number.values.tolist()):
				return pokemon_number
			else:
				return False
	except:
		return False


def build_answer(df, pokemon_number, TYPES_LIST):
	try:
		df1 = get_target_data(df, pokemon_number)
		max_index = get_target_weakness(df1)
		df1 = clean_target_data(df1)
		df1 = create_output(df, df1, max_index,TYPES_LIST)
		pokemon_data = send_query_answer(df1)
		return jsonify(pokemon_data)
	except:
		return '''<h1> Something failed </h1>'''

def get_img_pokemon(url,term,pokedex_number,img_list):
	try:
		if len(url) > 0 and len(term) > 0 and len(pokedex_number) > 0 and len(img_list) == 0 and isinstance(url, str) == True and isinstance(term, str) == True and isinstance(pokedex_number, list) == True and isinstance(img_list, list) == True:
			i = 0
			while i < 801:
				if len(str(pokedex_number[i])) == 3:
					img_list.append(url+str(pokedex_number[i])+term)
				elif len(str(pokedex_number[i])) == 2:
					img_list.append(url+'0'+str(pokedex_number[i])+term)
				elif len(str(pokedex_number[i])) == 1:
					img_list.append(url+'00'+str(pokedex_number[i])+term)
				i += 1
			return img_list
		else:
			print('bad input data')
			return False
	except:
		return False

def replace_type(type1,type2,type2_list):
	try:
		if len(type1) > 0 and len(type2) > 0 and isinstance(type1, list) == True and isinstance(type2, list) == True:
			i = 0
			while i < 801:
				if str(type2[i]) == 'nan':
					type2_list.append(type1[i])
				else:
					type2_list.append(type2[i])
				i += 1
			return type2_list
		else:
			print('bad input data')
			return False
	except:
		return False


def generate_dataframe(df,img_list,type2_list):
	try:
		if check_dataframe(df) == True and len(img_list) > 0 and len(type2_list) > 0 and isinstance(img_list, list) == True and isinstance(type2_list, list) == True:
			data_dict = {'img':img_list}
			df2 = pd.DataFrame.from_dict(data_dict)
			df['image'] = df2
			data_dict = {'type2':type2_list}
			df2 = pd.DataFrame.from_dict(data_dict)
			df['type2'] = df2
			return df
		else:
			print('bad input data3')
			return False
	except:
		return False

def rename_columns(df,columns_names):
	try:
		if check_dataframe(df) == True and len(columns_names) == 18 and isinstance(columns_names, dict) == True:
			df = df.rename(columns=columns_names)
			return df
		else:
			print('bad input data')
			return False
	except:
		print('zob')
		return False
	
def save_dataframe(df,csv_name):
	try:
		if check_dataframe(df) == True and len(csv_name) > 0 and isinstance(csv_name, str) == True:
			df.to_csv(csv_name)
		else:
			return False
	except:
		return False
