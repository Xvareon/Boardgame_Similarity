# Boardgame_Similarity
An interface that takes two Board Game Geek usernames as input and returns some sort of similarity score as output.

# Dependencies:
Python 3.11+

# 1. Project Setup
Clone the repository in your designated folder (Open a terminal for this):
```
git clone https://github.com/Xvareon/Boardgame_Similarity.git
```

# 2. Packages installation
Set up the virtual environment
```
python -m venv venv
```
Activate the venv
```
source venv/Scripts/activate
```
Install the python packages
```
pip install -r requirements.txt
```

# 3. Getting the output
Run
```
python manage.py runserver
```

# 4. Test endpoints
Similarity between two users:
Example: http://127.0.0.1:8000/api/similarity/?user1=TomVasel&user2=rahdo

Top similar users
Example: http://127.0.0.1:8000/api/similar-users/?username=ZeeGarcia

Sanity check if we don't provide user1/user2
http://127.0.0.1:8000/api/similarity/