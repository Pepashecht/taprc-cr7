import logging
import azure.functions as func
import os
import pyodbc

app = func.FunctionApp()

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_tables(myTimer: func.TimerRequest) -> None:
    #importar as variaveis de ambiente
    host = os.getenv("HOST")
    database = os.getenv("DATABASE")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")

    #como criar uma connection string usando pyodbc
    conn = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={host};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    #Criar a conexão com o banco
    #Fazer um select * na tabela
    #Imprimir os dados da tabela usando logging.info()
    #Fazer o deploy

    #ANALISTA
    try:
        with pyodbc.connect(conn) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM itsm.analista")
            rows = cursor.fetchall()
            for row in rows:
                logging.info(row)
    except Exception as e:
                logging.error(f"Error connecting to the database: {e}")
    #ANALISTA
    #CATEGORIA
    try:
        with pyodbc.connect(conn) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM itsm.categoria")
            rows = cursor.fetchall()
            for row in rows:
                logging.info(row)
    except Exception as e:
            logging.error(f"Error connecting to the database: {e}")
    #CATEGORIA
    #CHAMADO
    try:
        with pyodbc.connect(conn) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM itsm.chamado")
            rows = cursor.fetchall()
            for row in rows:
                logging.info(row)
    except Exception as e:
            logging.error(f"Error connecting to the database: {e}")
    #CHAMADO
    #CHAMADO_SLA
    try:
        with pyodbc.connect(conn) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM itsm.chamado_sla")
            rows = cursor.fetchall()
            for row in rows:
                logging.info(row)
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
    #CHAMADO_SLA
    #CHAMADO_STATUS_HISTORICO
    try:
        with pyodbc.connect(conn) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM itsm.chamado_status_historico")
            rows = cursor.fetchall()
            for row in rows:
                logging.info(row)
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
    #CHAMADO_STATUS_HISTORICO
    #CLIENTE_ORGANIZACAO
    try:
        with pyodbc.connect(conn) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM itsm.cliente_organizacao")
            rows = cursor.fetchall()
            for row in rows:
                logging.info(row)
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
    #CLIENTE_ORGANIZACAO
    #CSAT_AVALIAÇÃO
    try:
        with pyodbc.connect(conn) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM itsm.csat_avaliacao")
            rows = cursor.fetchall()
            for row in rows:
                logging.info(row)
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
    #CSAT_AVALIAÇÃO
    #FILA
    try:
        with pyodbc.connect(conn) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM itsm.fila")
            rows = cursor.fetchall()
            for row in rows:
                logging.info(row)
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
    #FILA
    #SLA
    try:
        with pyodbc.connect(conn) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM itsm.sla")
            rows = cursor.fetchall()
            for row in rows:
                logging.info(row)
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
    #SLA
    #SOLICITANTE
    try:
        with pyodbc.connect(conn) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM itsm.solicitante")
            rows = cursor.fetchall()
            for row in rows:
                logging.info(row)
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
    #SOLICITANTE

    