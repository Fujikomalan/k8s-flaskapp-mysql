from flask import Flask, render_template
import mysql.connector
import os
import sys

app = Flask(__name__)

@app.route('/')  
def message(): 
    try:
        dataBase = mysql.connector.connect(
            host=os.getenv('DATABASE_HOST'),
            user=os.getenv('DATABASE_USER'),
            passwd=os.getenv('DATABASE_PASSWORD'),
            database=os.getenv('DATABASE_NAME', 'company'),
            port=os.getenv('DATABASE_PORT', 3306)
        )
        
        cursorObject = dataBase.cursor(dictionary=True)
        table_name = os.getenv('DATABASE_TABLE', 'employees')  # New environment variable for table name
        query = f"SELECT * FROM {table_name}"  # Use the configurable table name
        cursorObject.execute(query)
        records = cursorObject.fetchall()  # Changed variable name from 'students' to 'records'
        dataBase.close()
        
        return render_template('index.html.tmpl',
                           students=records,  # Still using 'students' for template compatibility
                           hostname=os.getenv('HOSTNAME', 'Unknown Host'))

    except mysql.connector.Error as err:
        print(f"Database error: {err}", file=sys.stderr)
        return "<h3>Database Connection Error</h3><p>Please try again later.</p>", 500

    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return "<h3>Application Error</h3><p>An unexpected error occurred.</p>", 500

if __name__ == '__main__': 
    # Check required environment variables
    required_vars = ['DATABASE_HOST', 'DATABASE_USER', 'DATABASE_PASSWORD']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Error: Missing required environment variables: {', '.join(missing_vars)}", file=sys.stderr)
        sys.exit(1)
    
    hostname = os.getenv('HOSTNAME', None)
    database_host = os.getenv('DATABASE_HOST', None)
    database_port = os.getenv('DATABASE_PORT', 3306)
    database_user = os.getenv('DATABASE_USER', None)
    database_password = os.getenv('DATABASE_PASSWORD', None)
    database_name = os.getenv('DATABASE_NAME', 'company')
    database_table = os.getenv('DATABASE_TABLE', 'employees')
    flask_port = os.getenv('FLASK_PORT', 8080)
    debug_mode = os.getenv('FLASK_DEBUG', 'True')
    
    app.run(debug=debug_mode, port=flask_port, host="0.0.0.0")
