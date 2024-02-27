from flask import Flask
import schedule
import time
import mysql.connector

app = Flask(__name__)

def update_data():
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='test'
        )
        cursor = conn.cursor()

        # Update data in the database
        query = "UPDATE table1 SET status = '1' WHERE name='sayantan'"
        cursor.execute(query)
        conn.commit()

        print("Data updated successfully")

    except mysql.connector.Error as error:
        print("Error updating data:", error)

    finally:
        # Close the database connection
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

# Schedule the job to run at a specific time
schedule.every().day.at("10:00").do(update_data)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
    
    while True:
        schedule.run_pending()
        time.sleep(1)