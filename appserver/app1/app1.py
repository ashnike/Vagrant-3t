from flask import Flask, jsonify
import pymysql

app1 = Flask(__name__)

# Function to connect to the MySQL database
def connect_to_db():
    try:
        connection = pymysql.connect(
            host='192.168.58.4',
            user='user1',
            password='password1',
            db='db_one',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except Exception as e:
        print("Error connecting to the database:", str(e))
        return None

# Database API (/db) - Sample data retrieval
@app1.route('/db', methods=['GET'])
def db_api():
    # Connect to MySQL database
    connection = connect_to_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                # Execute SQL query to retrieve data
                query = "SELECT * FROM table1"  # Replace 'your_table' with your actual table name
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
                "<head><title>DB API1</title></head>"
                "<body>"
                "<h1>Data Retrieved from Database for App 1</h1>"
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

# Non-Database API (/non-db) - HTTP 200 response
@app1.route('/non-db', methods=['GET'])
def non_db_api():
    # HTML content to be included in the response
    html_content = (
        "<html>"
        "<head><title>Non-DB API1</title></head>"
        "<body>"
        "<h1>Non-Database Endpoint for App 1</h1>"
        "<p>This is a sample HTML response without JSON data.</p>"
        "</body>"
        "</html>"
    )

    return html_content, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    app1.run(host='0.0.0.0', port=5001)  # Run the Flask app on port 5001

