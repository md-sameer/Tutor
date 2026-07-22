# Tution - Tutor Company Landing Page

A complete tutor company website with email notification system built with Flask (backend) and HTML/CSS/JavaScript (frontend).

## Features

- **Modern UI/UX Design**: Beautiful, responsive landing page with professional design
- **Multiple Pages**: Home, About, Faculty, Registration, and Success pages
- **Email System**: Automatic email notifications to both admin and students
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Form Validation**: Client-side validation for registration form
- **Smooth Animations**: Scroll animations and interactive elements

## Pages

1. **Home Page** (`/`): Hero section, features, courses, statistics, and call-to-action
2. **About Page** (`/about`): Company story, mission, vision, and testimonials
3. **Faculty Page** (`/faculty`): Team of expert tutors with qualifications
4. **Registration Page** (`/register`): Student registration form with validation
5. **Success Page** (`/success`): Confirmation page with next steps

## Email Configuration

The application uses Gmail SMTP for sending emails. Configure your email settings in `app.py`:

```python
EMAIL_ADDRESS = "Tution@gmail.com"
EMAIL_PASSWORD = "qcqh sfxa jnvs hhwb"
ADMIN_EMAIL = "admin@tution.com"  # Change to your admin email
```

### Email Features

- **Admin Notification**: When a student registers, the admin receives an email with student details
- **Student Confirmation**: Students receive a thank you email with their registration details

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Email Settings**:
   - Update `EMAIL_ADDRESS` and `EMAIL_PASSWORD` in `app.py`
   - Update `ADMIN_EMAIL` to receive registration notifications
   - Make sure to enable 2-factor authentication on your Gmail account
   - Generate an App Password from Google Account settings (the password provided is an app password)

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Website**:
   Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure

```
Mail-Config/
├── app.py                      # Flask application with email functionality
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/                  # HTML templates
│   ├── index.html             # Home page
│   ├── about.html             # About page
│   ├── faculty.html           # Faculty page
│   ├── register.html          # Registration page
│   └── success.html           # Success page
└── static/                     # Static assets
    ├── css/
    │   └── style.css          # Main stylesheet
    └── js/
        └── script.js          # JavaScript functionality
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Email**: SMTP (Gmail)
- **Icons**: Font Awesome
- **Design**: Custom CSS with modern UI principles

## Gmail Setup for Email

To use Gmail SMTP:

1. Go to your Google Account settings
2. Enable 2-factor authentication
3. Go to Security > App Passwords
4. Generate a new app password for "Mail"
5. Use that app password in `EMAIL_PASSWORD`

## Customization

- **Colors**: Modify CSS variables in `static/css/style.css`
- **Content**: Update HTML files in `templates/` directory
- **Email Templates**: Modify email body in `app.py` functions
- **Faculty Members**: Add/remove faculty in `templates/faculty.html`

## Features Breakdown

### Navigation
- Responsive navbar with hamburger menu for mobile
- Active state highlighting
- Smooth scrolling

### Home Page
- Hero section with gradient background
- Feature cards with hover effects
- Course showcase
- Statistics section
- Call-to-action

### About Page
- Company story and mission
- Values section
- Testimonials from students
- Differentiators

### Faculty Page
- Faculty member cards with photos
- Qualifications and experience
- Social media links

### Registration Page
- Comprehensive registration form
- Form validation
- Benefits list
- Contact information

### Success Page
- Confirmation message
- Next steps timeline
- Contact information

## Security Notes

- Never commit actual email passwords to version control
- Use environment variables for sensitive data in production
- The provided app password should be kept secure
- Consider using a dedicated email service like SendGrid for production

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

This project is for educational purposes.

## Support

For issues or questions, contact: Tution@gmail.com
