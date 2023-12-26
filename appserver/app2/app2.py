from flask import Flask, jsonify
import pymysql

app2 = Flask(__name__)

# Function to connect to the MySQL database for app2
def connect_to_db_two():
    try:
        connection = pymysql.connect(
            host='192.168.58.4',
            user='user2',
            password='password2',
            db='db_two',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except Exception as e:
        print("Error connecting to the database:", str(e))
        return None

# Database API (/db) - Sample data retrieval for app2
@app2.route('/db', methods=['GET'])
def db_api_two():
    # Connect to MySQL database
    connection = connect_to_db_two()
    if connection:
        try:
            with connection.cursor() as cursor:
                # Execute SQL query to retrieve data
                query = "SELECT * FROM table2"  # Replace 'your_table' with your actual table name
                cursor.execute(query)

                # Fetch data from the result set
                data = cursor.fetchall()

            # Close connection
            connection.close()

            # Format JSON data for inclusion in HTML
            formatted_data = jsonify(data).response[0]

            # HTML content to be included in the response
            html_content = (
                "<html>"
                "<head><title>DB API2</title></head>"
                "<body>"
                "<h1>App2 Data from Database2 for app 2</h1>"
                "<p>This is a sample HTML response along with JSON data.</p>"
                "<pre>{}</pre>"
                "</body>"
                "</html>"
            ).format(formatted_data)
            return html_content, 200, {'Content-Type': 'text/html'}
        except Exception as e:
            return "Error retrieving data from the database: {}".format(str(e)), 500
    else:
        return "Failed to connect to the database", 500

# Non-Database API (/non-db) - HTTP 200 response for app2
@app2.route('/non-db', methods=['GET'])
def non_db_api_two():
    # HTML content to be included in the response
    html_content = (
        "<html>"
        "<head><title>Non-DB API2</title></head>"
        "<body>"
        "<h1>Non-Database Endpoint for App 2</h1>"
        "<p>This is a sample HTML response.</p>"
        "</body>"
        "</html>"
    )

    return html_content, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    app2.run(host='0.0.0.0', port=5002)  # Run the Flask app on port 5002

