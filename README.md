# letsbloom-deepanshu
Following assignemnt works with Django framework of Python using postgreSQL database. Note that code will be ran in the localhost and user has to use their own database in their machine.

1. First of all we need to clone the repo from the link using the git clone commands

2. After cloning, we will integrate the database with the code.

   2.1. Download pgadmin4 for postgresql support from the following link : https://www.pgadmin.org/download/

   2.2. Install the application and create user. Make a new server in server tab and further create a new database in it with name of your choice

   2.3. Here i have created the database named 'library' with user named 'postgres'

   2.4. Now go to settings.py in letsbloom folder and find the DATABASE line

     ![image](https://github.com/Deepu-b/letsbloom-deepanshu/assets/139762254/38fb42ef-2439-4ea4-b237-ca687a608d24)

       add name pf your database in front of 'NAME'
       add you user in front of 'USER'
       add password of your postgres user in front of 'PASSWORD'

   2.5. Note that we are running it on localhost hence port and host remain unchanged

3. Now go terminal in letbloom and run command 'python manage.py runserver' to start django server

4. Now the server is live on port 8000 but since there is nothing to be shown it will show Page not found error

5. Go to postman or insomnia to check the working of our code. Make a post request of JSON type on the url 'http://127.0.0.1:8000/API/addbook' having attributes of id, name and author

6. Make get request on 'http://127.0.0.1:8000/API/books' and you will see that book added before has been added in the database

7. You can also update the information of book by doing a PATCH request on 'http://127.0.0.1:8000/API/updatebook' with a JSON file having attributes of id, name and author

8. Now you can play around with adding new books or updating older ones or by adding a book that already exits (which will give message that book already exist)

9. We can add more complexity by adding count of each book available in the library and manage more inforamation regarding the same.  



   
