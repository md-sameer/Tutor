from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

# Email Configuration
EMAIL_ADDRESS = "sameermd010203@gmail.com"
EMAIL_PASSWORD = "qcqh sfxa jnvs hhwb"
ADMIN_EMAIL = "namesameermd786@gmail.com"  # Change this to your admin email

def send_email(to_email, subject, body, is_html=False):
    """Send email using Gmail SMTP"""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        
        if is_html:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def send_admin_notification(student_data):
    """Send notification email to admin about new registration"""
    subject = "New Student Registration - Tution"
    body = f"""
    <html>
    <body>
        <h2>New Student Registration</h2>
        <p>A new student has registered for Tution:</p>
        <ul>
            <li><strong>Name:</strong> {student_data['name']}</li>
            <li><strong>Email:</strong> {student_data['email']}</li>
            <li><strong>Phone:</strong> {student_data['phone']}</li>
            <li><strong>Course:</strong> {student_data['course']}</li>
            <li><strong>Grade/Class:</strong> {student_data['grade']}</li>
        </ul>
        <p>Please contact the student to proceed with enrollment.</p>
    </body>
    </html>
    """
    return send_email(ADMIN_EMAIL, subject, body, is_html=True)

def send_student_confirmation(student_data):
    """Send confirmation email to student"""
    subject = "Thank You for Registering with Tution"
    body = f"""
    <html>
    <body>
        <h2>Thank You for Choosing Tution!</h2>
        <p>Dear {student_data['name']},</p>
        <p>Thank you for registering with Tution. We have received your application for the <strong>{student_data['course']}</strong> course.</p>
        <p><strong>Registration Details:</strong></p>
        <ul>
            <li>Name: {student_data['name']}</li>
            <li>Email: {student_data['email']}</li>
            <li>Phone: {student_data['phone']}</li>
            <li>Course: {student_data['course']}</li>
            <li>Grade/Class: {student_data['grade']}</li>
        </ul>
        <p>Our team will contact you shortly to discuss the next steps and schedule your classes.</p>
        <p>If you have any questions, feel free to reach out to us at any time.</p>
        <br>
        <p>Best regards,</p>
        <p><strong>Tution Team</strong></p>
        <p>Email: {EMAIL_ADDRESS}</p>
    </body>
    </html>
    """
    return send_email(student_data['email'], subject, body, is_html=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student_data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'course': request.form.get('course'),
            'grade': request.form.get('grade')
        }
        
        # Send emails
        admin_sent = send_admin_notification(student_data)
        student_sent = send_student_confirmation(student_data)
        
        return redirect(url_for('success'))
    
    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
