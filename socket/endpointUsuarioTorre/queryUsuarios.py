import psycopg2
from config import load_config

#obtener y mostrar todos los usuarios
def usuarios_query():

	config = load_config()
	
	query = "SELECT * FROM usuario;"
	
	try:
		with psycopg2.connect(**config) as conn:
			with conn.cursor() as cursor:
				cursor.execute(query)
				all_users = cursor.fetchall()
				return all_users
	except psycopg2.DatabaseError as error:
		print('error')
	except Exception as e:
		print(f'error: {e}')
		
		
#obtener y mostrar un usuario por torre_id
def torre_query(torre_id):
	config = load_config()
	
	query = "SELECT * FROM usuario WHERE torre_id = %s;"
	
	try:
		with psycopg2.connect(**config) as conn:
			with conn.cursor() as cursor:
				cursor.execute(query, (torre_id,))
				usuarios = cursor.fetchall()
				return usuarios
	except psycopg2.DatabaseError as error:
		print('error')
	except Exception as e:
		print(f'error: {e}')
			
