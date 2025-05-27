# Django
# 🎬 Movie Review API

This is a Django-based REST API project built to manage and display movie reviews.  
It serves as a foundation for further development of full movie review functionality, including review submissions, user authentication, and rating aggregation.

---

## 🚀 Features

- Django backend with RESTful API structure
- API endpoint to return a welcome message
- Easy to extend with new endpoints (movies, users, ratings)
- Clean project structure and ready for deployment

---

## 📁 Project Structure


---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/KusumaEswaravaka/skill_captain_Django.git
cd skill_captain_Django
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On Mac/Linux
pip install -r requirements.txt
pip install django
python manage.py migrate
python manage.py runserver
