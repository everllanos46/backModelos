import pyodbc 


def connect_db():
    try:
        connection=pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-3BCLR7E\SQLEXPRESS;DATABASE=ModelosBd')
        return connection
    except Exception as ex:
     return null