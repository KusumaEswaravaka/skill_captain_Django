1. Clone the Repository
git clone https://github.com/KusumaEswaravaka/skill_captain_Django.git
cd skill_captain_Django

2. Set Up Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On macOS/Linux

3. Install Dependencies
pip install -r requirements.txt
# If requirements.txt is missing, run:
pip install django

4. Run Database Migrations
python manage.py migrate

5. Start the Development Server
python manage.py runserver

# Open your browser at http://127.0.0.1:8000 to see your project running
