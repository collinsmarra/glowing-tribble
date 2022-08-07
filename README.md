#### Implement "likes" with flask

This example repo is used to implement 'likes' feature for an example blog in flask and python

Get started:
    
    flask shell
    
    >>>> db.create_all()

Usage:
    
    flask fake --help

some commands requires arguements and they are integers

> Examples
> Generate 30 Fake users
    
    flask fake users 30

> Generate 200 Fake blog posts for random users

    flask fake posts 200

> Get the number of likes for 20  random posts

    flask fake liked 20

> Get all posts liked by a user with id=3

    flask fake all-posts 3

You can also use postman
all the request bodies require json data type


The routes are:

```
Endpoint         Methods  Rule
---------------  -------  ------------------------------
auth.login       POST     /login
auth.logout      POST     /logout
posts.delete     DELETE   /posts/posts/<int:id>/delete
posts.like       GET      /posts/posts/<int:id>/like
posts.likes      GET      /posts/posts/<int:id>/likes
posts.new        POST     /posts/new
posts.unlike     GET      /posts/posts/<int:id>/unlike
static           GET      /static/<path:filename>
users.has_liked  GET      /users/posts/<int:id>/hasliked
users.new        POST     /users/new
```
