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
Similarity between two users example: http://127.0.0.1:8000/api/similarity/?user1=TomVasel&user2=rahdo
<img width="1419" height="508" alt="image" src="https://github.com/user-attachments/assets/e91ff573-50e7-40f3-92f3-7aa72b378e67" />


Top similar users example: http://127.0.0.1:8000/api/similar-users/?username=ZeeGarcia
<img width="1435" height="737" alt="image" src="https://github.com/user-attachments/assets/0ce4e616-5bda-4feb-a78c-2cd1315b87fa" />


Sanity check if we don't provide user1/user2: http://127.0.0.1:8000/api/similarity/
<img width="1481" height="503" alt="image" src="https://github.com/user-attachments/assets/90a8fade-4a42-4251-8670-bb365e40fa50" />
