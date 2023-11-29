*Student Marksheet Management System*
---

**Project Description**

This project is made from one the Python Web-Frameworks ~ DJango

*-> Django is a free python open-source web-framework that follows the model-template-views system.*

* The Marksheet Management System is a comprehensive web application developed to efficiently manage and display student marksheet information. 
* This system is designed to automate and streamline the process of recording, calculating, and presenting student academic performance.
* Utilizing the Django framework, it incorporates best practices, robust error handling, and security considerations to ensure a reliable and secure user experience.
* The project uses:
    - A secure User Authentication System.
    - Student Information Management - users can add, edit or remove any student information.
    - Subject-Wise Marks/ Grades Entry.
    - Error Handling to handle all the possible errors which might cause to the system.
    - User Friendly Interface.
    - Audit Trail - The application records all the significant events such as user logins, changes in student information, and grade 
                    modifications.

**How to install/ view this project:**

-> You have to first have Django installed in your machine, follow the following steps:

    -- Install Django and create a new project and app as:

    pip install django
    django-admin startproject marksheet_project
    cd marksheet_project
    python manage.py startapp marksheet_app

    **After the above mentioned steps, update the files in your directory of the project with code I have written, in this repository.**

    -- Create and apply migrations:

       python manage.py makemigrations
       python manage.py migrate
    
    -- Create a superuser:

       python manage.py createsuperuser

    -- Run the development server:

       python manage.py runserver
       
    * Visit http://127.0.0.1:8000/admin and log in with the superuser credentials. Add some students through the admin interface.

    * Visit http://127.0.0.1:8000/marksheet/ to see the marksheet.

    * Visit http://127.0.0.1:8000/add_student/ to add a new student.

*Technologies & Tools Used for the Project*
```
- Microsoft Visual Studio (Windows)
- VS Code (Windows & Mac OSX)
- PyCharm IDE for Python web FrameWorks
```

*Academic Honesty/ Integrity Statement*
```
I declare that the code in this repository is entirely my own work.

NOTE: For others, this repo can be a good reference, if someone wants to learn &
understand the aspects of JAVA programming and it's topic but must not copy the
work completed by me!
```




