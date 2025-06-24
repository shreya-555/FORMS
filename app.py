
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# MySQL connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SHREYASINGH!999",
    database="contactdb"
)
cursor = db.cursor()

@app.route('/api/submit', methods=['POST'])
def submit_form():
    data = request.json
    try:
        # Save to MySQL
        sql = """
            INSERT INTO users (first_name, last_name, email, mobile, gender, hobbies)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            data['firstName'],
            data['lastName'],
            data['email'],
            data['mobile'],
            data['gender'],
            ', '.join(data['hobbies'])
        )
        cursor.execute(sql, values)
        db.commit()

        # Send Email
        sender_email = "imshreyasingh9@gmail.com"         # Your Gmail
        receiver_email = "pratikgandole@gmail.com"       # Where you want to receive data
        app_password = "qzpr hujf crex gppk"       # App password (not your Gmail login password)

        subject = "New Contact Form Submission "
        body = f"""
        First Name: {data['firstName']}
        Last Name: {data['lastName']}
        Email: {data['email']}
        Mobile: {data['mobile']}
        Gender: {data['gender']}
        Hobbies: {', '.join(data['hobbies'])}
        """

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()

        return jsonify({"message": "Data inserted & emailed successfully!"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "Error inserting data!"}), 500

if __name__ == '__main__':
    app.run(debug=True)
