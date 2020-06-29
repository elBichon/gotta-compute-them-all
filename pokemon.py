import pandas as pd
import utils


if __name__ == "__main__":
	CSV_NAME = 'post_treat_pokemon.csv'
	COLUMNS_NAMES = {'against_bug':'bug','against_dark':'dark','against_dragon':'dragon','against_electric':'electric','against_fairy':'fairy','against_fight':'fight','against_fire':'fire','against_flying':'flying','against_ghost':'ghost', 'against_grass':'grass', 'against_ground':'ground','against_ice':'ice','against_normal':'normal', 'against_poison':'poison', 'against_psychic':'psychic','against_rock':'rock','against_steel':'steel', 'against_water':'water'}
	df = pd.read_csv('pokemon.csv')
	type1 = df.type1.values.tolist()
	type2 = df.type2.values.tolist()
	img_list = []
	type2_list = []
	pokedex_number = df.pokedex_number.values.tolist()
	url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/'
	term = '.png'
	df = df[['against_bug', 'against_dark', 'against_dragon',
	       'against_electric', 'against_fairy', 'against_fight', 'against_fire',
	       'against_flying', 'against_ghost', 'against_grass', 'against_ground',
	       'against_ice', 'against_normal', 'against_poison', 'against_psychic',
	       'against_rock', 'against_steel', 'against_water','classfication', 
	       'height_m','name','attack','pokedex_number','type1','type2','weight_kg','generation', 'is_legendary']]

	img_list = utils.get_img_pokemon(url,term,pokedex_number,img_list)
	type2_list = utils.replace_type(type1,type2,type2_list)
	df = utils.rename_columns(df,COLUMNS_NAMES)
	df = utils.generate_dataframe(df,img_list,type2_list)
	utils.save_dataframe(df,CSV_NAME)

