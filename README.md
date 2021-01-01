# twitter_django-project

- This is made by Django, Python framework.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## The flow of django Project

- Install Django by command 'python -m pip install Django'

- Made 'Django Project' folder.

- Start project by comman 'python -m django startproject project-name'

- Start App by command 'python manage.py startapp app-name'

- Add 'app-name' in 'INSTALLED APP'

- Run server by command 'python manage.py runserver'

- Making models.py and write down the necesarry table info inside that file.

- After mainking models.py, in command, call 'python manage.py  makemigrations'

- After that, in command, call 'python manage.py migrate' in order to tell the database change I did such as columns settings.

- Making views.py and write down the function which is to return some html file as we can call in urls.py.

- after views.py, come to connect with path of all the files in urls.py in order to display them.

- Under app, make folder named 'static' for image and style.css files and named 'templates' for html file as template.

- Under templates folder, make one folder named 'pages' and one file named 'index.html' in which is written html tag.

- Under pages folder, make several page template html file. 





## Twitter Project

- in /home, it displays 'no tweet is there' because database has no tweet info yet.

- when you put a button at the bottom right, you will jump to /posttweet page.

- you can input text and image file at tag and put Tweet button.

- After pushing tweet button, you insert the info into database which columns are 'id', 'parent_tweet_id', 'name', 'text', 'created_at', 'image_path'.

- After that, you jump back to /home page.

- And you can reply each tweet by pushing the reply button at the bottom in each tweets.

- And you can check the all replies per each tweet by putting the tweet icon.

## You can tweet and reply and check the tweet detail.
