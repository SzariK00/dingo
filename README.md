# Basic django training.
>Author: Adrian Jelonek |  E-mail: ajelonek(at)gmail.com

### Apps:
#### 1. dingo - main app (project app).
#### 2. greetings - just to greet someone :)  
    Run server and type:
    - localhost:port/greetings/
    - localhost:port/greetings/name
#### 3. maths - a simple web url calculator.  
    Run server and type:
    - localhost:port/maths/add/1/1 
    - You can try another operations like: div, sub, mul. 
#### 4. sessions - small tool to check how sessions work.  
    Run server and type:
    - localhost:port/sessions/set and then localhost:port/sessions/get (in the same tab)  
#### 5. posts - a small exercise with migrations.  
    Check the database tables:
     - posts_author - stores authors of the posts
     - posts_post - stores posts with the relationship with posts_author table using author_id Foreign Key      
#### 6. forms - an exercise with forms.  
    Run server and type:
    - localhost:port/posts/ - to be able to see posts and add more
    - localhost:port/posts/authors - to be able to see posts' authors and add more of them