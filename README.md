# Simple Pay PWA

![Simple Pay Logo](./simplepay-rocket.webp)


## Overview

Simple Pay is a Progressive Web Application (PWA) designed to simplify rent payments. With features like rent reminders, secure user authentication, and a sleek rocket-themed interface, it’s built specifically for **Launch Now Apartments**. The app focuses on delivering a seamless experience for tenants while impressing potential investors with its cool, modern design.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **User Authentication**: Login/Signup functionality using Flask-Login.
- **Rent Reminders**: Push notifications to remind tenants about upcoming rent payments.
- **Rocket-Themed UI**: Engaging design for Launch Now Apartments, creating a "cool" look.
- **PWA Support**: Works offline and can be installed on devices as a web app.
- **Responsive Design**: Optimized for both desktop and mobile views.

---

## Technologies Used
<ul>
  <li><strong>Frontend:</strong> HTML, CSS, JavaScript, Tailwind CSS</li>
  <li><strong>Backend:</strong> Python, Flask, Flask-Login, Flask-SQLAlchemy</li>
  <li><strong>Database:</strong> SQLite (can be extended to PostgreSQL)</li>
  <li><strong>PWA Support:</strong> Service Worker, Web App Manifest</li>
  <li><strong>Development Tools:</strong> Visual Studio Code (VS Code)</li>
  <li><strong>Version Control:</strong> GitHub</li>
</ul>

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/JoshTheCyberSecuritySpecialist/simple-pay-pwa.git
   cd simple-pay-pwa


# Set Up Virtual Environment (Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Flask App

```bash
flask run
```

## Access the App
Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Usage
- **User Authentication**: Sign up or log in to access your dashboard.
- **Pay Rent**: View rent amount and make payments directly within the app.
- **Receive Notifications**: Enable notifications to get rent reminders.
- **Install as PWA**: Add the app to your home screen for quick access.

---

## Screenshots
Add screenshots of the app in action, including the login screen, dashboard, and rent payment interface.

---

## Contributing
Contributions are welcome!

1. **Fork the repository.**  
2. **Create a new branch for your feature or bug fix:**

   ```bash
   git checkout -b feature-name
   ```

3. **Commit your changes and push them to your branch:**

   ```bash
   git commit -m "Add feature or fix"
   git push origin feature-name
   ```

4. **Open a pull request** with a detailed description of your changes.

---

## Future Improvements
- **Payment Integration**: Connect with third-party payment processors (e.g., Stripe or PayPal) to handle transactions.
- **Admin Dashboard**: Provide property managers with analytics and tools to track rent payments.
- **Multi-Language Support**: Add localization features for different languages.
- **Mobile App Version**: Develop a native mobile app using the same backend.

---

## Known Issues
- **Offline Notifications**: Notifications may not work consistently in offline mode.
- **Cross-Browser Compatibility**: Some UI elements may look different in older versions of certain browsers.
- **Database Migration**: Switching from SQLite to PostgreSQL will require additional configuration.

---

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## Contact
If you have any questions or want to contribute, feel free to reach out or open an issue on the repository.
