The flow of django Project

1: Install Django by command 'python -m pip install Django'

2: Made 'Django Project' folder.

3: Start project by comman 'python -m django startproject project-name'

4: Start App by command 'python manage.py startapp app-name'

5: Add 'app-name' in 'INSTALLED APP'

6:Run server by command 'python manage.py runserver'

7: Making models.py and write down the necesarry table info inside that file.

8: After mainking models.py, in command, call 'python manage.py  makemigrations'

9: After that, in command, call 'python manage.py migrate' in order to tell the database change I did such as columns settings.

10: Making views.py and write down the function which is to return some html file as we can call in urls.py.

11:after views.py, come to connect with path of all the files in urls.py in order to display them.

12: Under app, make folder named 'static' for image and style.css files and named 'templates' for html file as template.

13: Under templates folder, make one folder named 'pages' and one file named 'index.html' in which is written html tag.

14: Under pages folder, make several page template html file. 





Twitter Project

1: in /home, it displays 'no tweet is there' because database has no tweet info yet.

2: when you put a button at the bottom right, you will jump to /posttweet page.

3: you can input text and image file at tag and put Tweet button.

4: After pushing tweet button, you insert the info into database which columns are 'id', 'parent_tweet_id', 'name', 'text', 'created_at', 'image_path'.

5: After that, you jump back to /home page.

6: And you can reply each tweet by pushing the reply button at the bottom in each tweets.

7: And you can check the all replies per each tweet by putting the tweet icon.

You can tweet and reply and check the tweet detail.
