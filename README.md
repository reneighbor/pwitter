# Welcome to Pwitter
A Twitter clone in Python/Flask


##TweetsList resource <code>('/tweets') </code>

<strong>GET</strong> - see all tweets visible to you (yours and your broadcasters').  Include the 
optional parameter "search" to filter results by tweet body.

```
curl -u <username>:<auth_token> http://127.0.0.1:5000/tweets?search=monkey
```

Response:
```
{
    "tweets": [
        {
            "body": "monkey jungle",
            "date_created": "Mon, 04 May 2015 00:03:07 -0000",
            "username": "reneighbor"
        },
        {
            "body": "monkey fingers",
            "date_created": "Sun, 26 Apr 2015 23:07:28 -0000",
            "username": "trenton"
        },
      ]
}
```

##UsersTweets resource <code>('/users/\<username\>/tweets') </code>

<strong>GET</strong> - see all your tweets.  Include the 
optional parameter "search" to filter results by tweet body.

```
curl -u <username>:<auth_token> http://127.0.0.1:5000/users/reneighbor/tweets?search=monkey
```

Response:
```
{
    "tweets": [
        {
            "body": "monkey jungle",
            "date_created": "Mon, 04 May 2015 00:03:07 -0000",
            "username": "reneighbor"
        }
}
```
</br>
<strong>POST</strong> - write a new tweet. Must include the
parameter "body," for tweet body.

```
curl -XPOST -u <username>:<auth_token> http://127.0.0.1:5000/users/reneighbor/tweets -d body=hello%20world```
```
Response:
```
{
    "tweet":  {
            "body": "hello world",
            "date_created": "Mon, 04 May 2015 00:14:28 -0000",
            "username": "reneighbor"
        }
}
```

##UsersFollowers List resource <code>('/users/\<username\>/followers') </code>

<strong>GET</strong> - see everyone following you.

```
curl -u <username>:<auth_token> http://127.0.0.1:5000/users/reneighbor/followers
```

Response:
```
{
    "followers": [
        {
            "date_created": "Mon, 16 Feb 2015 18:43:36 -0000",
            "date_followed": "Mon, 04 May 2015 00:14:28 -0000",
            "username": "mont.e.python"
        }
    ]
}
```

##UsersBroadcasters List resource <code>('/users/\<username\>/broadcasters') </code>

<strong>GET</strong> - see everyone you follow.

```
curl -u <username>:<auth_token> http://127.0.0.1:5000/users/reneighbor/broadcasters
```

Response:
```
{
    "broadcasters": [
        {
            "date_created": "Mon, 16 Feb 2015 18:43:36 -0000",
            "date_followed": "Mon, 16 Feb 2015 18:55:00 -0000",
            "username": "trenton"
        }
    ]
}
```

<strong>POST</strong> - start following someone. Must include parameter "username"
to indicate the username of the person you're trying to follow.

```
curl -XPOST -u <username>:<auth_token> http://127.0.0.1:5000/users/reneighbor/broadcasters -d username="ailey"
```

Response:
```
{
    "broadcaster": 
        {
            "date_created": "Mon, 04 May 2015 00:14:20 -0000",
            "date_followed": "Mon, 04 May 2015 00:14:28 -0000",
            "username": "ailey"
        }
}
```

##UsersBroadcasters Instance resource <code>('/users/\<username\>/broadcasters/\<broadcaster_name\>') </code>

<strong>DELETE</strong> - stop following someone.

```
curl -u <username>:<auth_token> http://127.0.0.1:5000/users/reneighbor/broadcasters/ailey
```

Response:
```
<HTTP/1.1 204 NO CONTENT>
```
