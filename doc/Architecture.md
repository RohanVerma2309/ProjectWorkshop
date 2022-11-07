
title: System Architecture
created at: Tue Nov 01 2022 04:36:15 GMT+0000 (Coordinated Universal Time)
updated at: Mon Nov 07 2022 03:34:33 GMT+0000 (Coordinated Universal Time)
---

# System Architecture

-   Saroj - Ravanpreet - Pranav - Pranay - Rohan
-   06/11/2022

## **Backend**

### Framework: DJANGO

## **Packages:**

-   **django.contrib.auth: **Used for authentication of users
-   **django.contrib.session: **Used for session management
-   **django-thumbnails: **Used for thumbnail generation

## Frontend

-   Pure HTML/CSS - UI
-   Javascript - functionalities like login pop-up, image grid,

### Editing Tools:

-   Cropper.JS -Image Crop
-   PhotoEditorSDK - Image Color modification

### Database to be used : SQLite

### Models:

-   User (For Photographer details)

    -   Name
    -   Email (Foreign Key associated to primary key of thumbnails)
    -   Password

-   Image

    -   title
    -   random number (Primary key associated with thumbnail foreign key)

-   Thumbnail
    -   Title
    -   Date
    -   Email (Primary key associated to User's foreign key)
    -   Random no (Foreign key associated with image primary key)

## Functions :

### Home (for every user)

-   For logged-in users, it will display explore, my space and logout.  
    Explore tab will display all the thumbnails.  
    My Space will be different for each user, and displays the images of that particular photographer only. URL for the same will be dynamic: /photographer Name
-   else, it will display explore tab as well as an option to login/register.

### **Login **

-   This is the interface for those users who have signed up in our application**.**
-   They just have to entered their email and password to log in to the server, whose authentication will be done with the Django package as mentioned above.
-   A session will be created with the help of the Django package which will monitor the working of user, and it will help us to restore the sessions of those users who forgot to log out from our site.

### **Sign up**

-   The user who is new to our server has to entered few of the details for accessing our site.
-   The user will enter the following details:
    -   Name
    -   Email
    -   Password
-   Then the data of the user will be stored in the database of our server and will help the user to login into our site for easy access of our tools available.

### Upload

-   Only the users who are logged in can upload photos.
-   On uploading photos, thumbnails are generated simultaneously and uploaded in a different database which is mapped together using primary key.
-   On successful upload, the user is prompted the same message,

### Image View

-   Users, who are logged in, will have an option to edit the images and save it by either replacing the image in the database or uploading another copy of it.  
    URL for the same will be /photographer Name/Image Title
-   Users who are not logged in, can only view the image and not modify it.  
    URL will be /Image Title

### Logout

-   A button will be available to the user to end their session from our site and all these will be maintained with the help of the session package of Django which will end the sessions after a particular time when there is no work going on from the client side.
-   Then this will show the pop-up to the user from the client side that "You are successfully logged out" and will redirect to the home page with the explore tab showing to the not logged-in users.

### Sort

-   Sorting is done on the explore tab, where the photographer's name will be displayed in a dropdown box and photos are displayed according to the selection.

![image.png](media_System%20Architecture/image.png)

![WhatsApp Image 2022-11-03 at 10.46.23 AM.jpeg](media_System%20Architecture/WhatsApp%20Image%202022-11-03%20at%2010.46.23%20AM.jpeg)

* * *

[\[https://www.figma.com/file/9o6epWqWUmpVBtToMBSxJa/Architecture-Flow?node-id=0%3A1\]](https://www.figma.com/file/9o6epWqWUmpVBtToMBSxJa/Architecture-Flow?node-id=0%3A1)

**======================================================================**

* * *

          
