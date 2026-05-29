# The Study Lounge

> **LEARN • CONNECT • EXCEL**

A computer science focused study platform built for SC, HSC and BSc Computer Science students in Mauritius. The Study Lounge provides structured, well-written notes organised by level and chapter, paired with a community Q&A system where students can ask questions and get help.

![The Study Lounge](https://res.cloudinary.com/dq9jjz5tf/image/upload/v1780029735/The_Study_Lounge_logo_qplgdd.png)

---

## Live Demo

 **[https://the-study-lounge.onrender.com](https://the-study-lounge.onrender.com)**

> Note: The site is hosted on Render's free tier. If it hasn't been visited recently, the first load may take a few seconds to wake up.

---

## Features

### Notes Platform
- Browse notes by level — SC, HSC and BSc Computer Science
- SC & HSC notes organised by **chapter** following the official syllabus
- BSc notes organised by **module** (e.g. Computer Programming, Database Systems)
- Notes written in **Markdown** with full formatting support — headings, code blocks, tables, images
- Inline images stored and served via **Cloudinary CDN**
- **Table of contents** auto-generated from note headings
- **Previous / Next** note navigation within a chapter
- **Focus mode** — hides sidebars for distraction-free reading

### Community Q&A
- Ask questions directly on any note page
- Answer questions from other students
- **Upvote** helpful answers
- **Accept** the best answer (admin only)
- Site-wide Q&A board showing all questions

### Smart Access Control
- Visitors can read **one note for free** without an account
- A second note triggers a **blur gate** with a signup prompt
- Registered users get **unlimited access** to all notes
- Session-based free preview — no cookies or tracking needed

### Authentication
- User registration and login
- Admin panel for posting and managing all content
- Role-based access (admin vs student)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 4.2 |
| Frontend | HTML, Tailwind CSS, Vanilla JS |
| Database | PostgreSQL (Render) |
| Media storage | Cloudinary |
| Note editor | Markdown (django-markdownx) |
| Static files | Whitenoise |
| Web server | Gunicorn |
| Hosting | Render (free tier) |
| Version control | GitHub |

---

## Screenshots

| Home Page | Note Detail | Focus Mode |
|---|---|---|
| ![The Study Lounge - Home Page](https://res.cloudinary.com/dq9jjz5tf/image/upload/v1780029578/The_Study_Lounge_j4j5jx.png) | ![The Study Lounge - Note Detail](https://res.cloudinary.com/dq9jjz5tf/image/upload/v1780029887/The_Study_Lounge_-_Note_Details_ikozib.png) | ![The Study Lounge - Focus Mode](https://res.cloudinary.com/dq9jjz5tf/image/upload/v1780029880/The_Study_Lounge_-_Note_Details_Focus_Mode_wkugmc.png)|

---

## Getting Started (Local Development)

### Prerequisites
- Python 3.12+
- pip
- A virtual environment (conda or venv)
- A Cloudinary account (free)
- A PostgreSQL database (Render free tier or local)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/the-study-lounge.git
cd the-study-lounge
```

### 2. Create and activate a virtual environment

```bash
# Using conda
conda create -n my_django_env python=3.12
conda activate my_django_env

# Or using venv
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=your-db-host
DB_PORT=5432

# Cloudinary
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

> Never commit your `.env` file to GitHub. It is already listed in `.gitignore`.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## Project Structure

```
The-Study-Lounge/
├── core/                   # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── notes/                  # Notes app
│   ├── models.py           # Level, Chapter, Note models
│   ├── views.py            # Notes + auth views
│   ├── auth_views.py       # Register, login, logout
│   ├── admin.py            # Admin configuration
│   └── urls.py             # Notes + auth URL routing
├── community/              # Q&A app
│   ├── models.py           # Question, Answer models
│   ├── views.py            # Q&A views
│   └── urls.py             # Q&A URL routing
├── templates/              # HTML templates
│   ├── base.html           # Master template
│   ├── notes/              # Notes templates
│   ├── community/          # Q&A templates
│   └── auth/               # Login & register templates
├── static/                 # CSS, JS, images
├── .env                    # Environment variables (not committed)
├── .gitignore
├── build.sh                # Render build script
├── render.yaml             # Render deployment config
├── requirements.txt        # Python dependencies
└── manage.py
```

---

## Database Models

```
Level          → SC / HSC / BSc Computer Science
    └── Chapter    → belongs to Level (chapter or module)
        └── Note   → belongs to Chapter (markdown content + images)

User
    └── Question   → belongs to Note + User
        └── Answer → belongs to Question + User (upvotes, accepted)
```

---

## Deployment (Render)

The project is configured for one-click deployment on Render.

### Environment variables required on Render

| Key | Description |
|---|---|
| `SECRET_KEY` | Django secret key (generate a strong one) |
| `DEBUG` | Set to `False` in production |
| `DB_NAME` | PostgreSQL database name |
| `DB_USER` | PostgreSQL username |
| `DB_PASSWORD` | PostgreSQL password |
| `DB_HOST` | Internal Render hostname |
| `DB_PORT` | `5432` |
| `CLOUDINARY_CLOUD_NAME` | Cloudinary cloud name |
| `CLOUDINARY_API_KEY` | Cloudinary API key |
| `CLOUDINARY_API_SECRET` | Cloudinary API secret |

### Build command
```bash
./build.sh
```

### Start command
```bash
gunicorn core.wsgi:application
```

---

## Contributing

This is a personal project but suggestions and feedback are welcome! Feel free to open an issue or submit a pull request.

---

## Author

**Jenna** — CS student

Built with ❤️ to help fellow CS students ace their exams.

---

## License

This project is open source and available under the [MIT License](LICENSE).