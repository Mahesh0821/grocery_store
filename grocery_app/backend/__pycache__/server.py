from flask import Flask,request,jsonify
# import products_dao
import sql_connection


app=Flask(__name__)
connection=sql_connection.get_sql_conneccion()

@app.route('/getproducts',method=['GET'])
def get_products():
    products=get_all_products(connection)
    reponse=jsonify(products)
    response.headers.add('Access-Control-Allow-Orgin','*')
    return response

if __name__=="__main__":
    print("starting python flask server for grocery store management")
    app.run(port=5000)