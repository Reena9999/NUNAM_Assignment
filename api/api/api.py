# Creating the API connection to the direct link to local db in MySQL
from flask import Flask, jsonify
from .db import create_connection, get_cursor, close_connection

# creating Flask app
app = Flask(__name__)

# REST API to read data from the database 
@app.route('/read_data/<int:id>', methods=['GET'])
def read_data_by_id(id):
    connection = create_connection()
    cursor = get_cursor(connection)
    
    try:
        cursor.execute("select curent_mA,voltage_v,capacity_mAh,auxilary_channel_TU1_temperature,absolute_time from _cell_monitor_ where cell_ID= %s", (id,))
        row = cursor.fetchall()
        if row:
            return jsonify(row), 200
        else:
            return jsonify({"error": "Data not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        close_connection(connection)


if __name__ == '__main__':
    app.run(debug=True,port=8080)
