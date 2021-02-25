import os
from pyreportjasper import JasperPy
from platform import python_version
import cx_Oracle
conn_str='USR_CONSUL_TREE/PassConsul@localhost:1521/xepdbtree'
db_conn = cx_Oracle.connect(conn_str)
cursor = db_conn.cursor()

def advanced_example_using_database():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/graf(1).jrxml'
    output = os.path.dirname(os.path.abspath(__file__)) + '/output/examples'
    #con = {
    #    'driver': 'Consulta_Arbol',
    #    'username': 'USR_CONSUL_TREE',
    #    'password': 'PassConsul',
    #    'host': 'localhost',
    #    'database': 'xepdbtree',
    #    'port': '1521'
    #}

    jasper = JasperPy()
    try:
      print("Dentro del proceso 4.")
      jasper = JasperPy()
      print("Ya pasado el proceso 4.")
      jasper.process(input_file,output_file=output,format_list=["pdf"],db_connection=conn_str)
    except:
      print("Error en la comunicacion")
 