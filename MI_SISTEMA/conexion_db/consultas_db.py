import cx_Oracle
class Conectar_db():
    #nombre_bd= 'db/TREE.db'

    def run_db(self,query,parametros =()):
       
       conn_str='USR_CONSUL_TREE/PassConsul@localhost:1521/xepdbtree'
       db_conn = cx_Oracle.connect(conn_str)
       cursor = db_conn.cursor()
       datos = cursor.execute(query,parametros)
       registros = cursor.fetchall()
       

       return datos