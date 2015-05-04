# Welcome to Pwitter
A Twitter clone in Python/Flask


##TweetsList resource <code>('/tweets') </code>

<strong>GET</strong> - see all tweets visible to you (yours and your broadcasters').  Include the 
optional parameter "search" to filter results by tweet body.

```
curl -u <user_sid>:<auth_token> http://127.0.0.1:5000/tweets?search=monkey
```

Response:
```
{
    "tweets": [
        {
            "body": "monkey fingers",
            "date_created": "Mon, 04 May 2015 06:55:52 -0000",
            "username": "trenton"
        },
        {
            "body": "monkey jungle",
            "date_created": "Mon, 04 May 2015 06:53:39 -0000",
            "username": "reneighbor"
        }
    ]
}
```

##UsersTweets resource <code>('/users/\<username\>/tweets') </code>

<strong>GET</strong> - see all your tweets.  Include the 
optional parameter "search" to filter results by tweet body.

```
curl -XDELETE -u <user_sid>:<auth_token> http://127.0.0.1:5000/users/reneighbor/tweets?search=monkey
```

Response:
```
{
    "tweets": [
        {
            "body": "monkey jungle",
            "date_created": "Mon, 04 May 2015 06:53:39 -0000",
            "username": "reneighbor"
        }
    ]
}
```
</br>
<strong>POST</strong> - write a new tweet. Must include the
parameter "body," for tweet body.

```
curl -XPOST -u <user_sid>:<auth_token> http://127.0.0.1:5000/users/reneighbor/tweets -d body=hello%20world```
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
curl -u <user_sid>:<auth_token> http://127.0.0.1:5000/users/reneighbor/followers
```

Response:
```
{
    "followers": [
        {
            "date_created": "Mon, 04 May 2015 06:10:07 -0000",
            "date_followed": "Mon, 04 May 2015 06:56:32 -0000",
            "username": "jess"
        }
    ]
}
```

##UsersBroadcasters List resource <code>('/users/\<username\>/broadcasters') </code>

<strong>GET</strong> - see everyone you follow.

```
curl -u <user_sid>:<auth_token> http://127.0.0.1:5000/users/reneighbor/broadcasters
```

Response:
```
{
    "broadcasters": [
        {
            "date_created": "Mon, 16 Feb 2015 18:43:49 -0000",
            "date_followed": "Mon, 04 May 2015 00:14:28 -0000",
            "username": "trenton"
        }
    ]
}
```

<strong>POST</strong> - start following someone. Must include parameter "username"
to indicate the username of the person you're trying to follow.

```
curl -XPOST -u <user_sid>:<auth_token> http://127.0.0.1:5000/users/reneighbor/broadcasters -d username="tartine"
```

Response:
```
{
    "broadcaster": 
        {
            "date_created": "Mon, 04 May 2015 00:14:20 -0000",
            "date_followed": "Mon, 04 May 2015 00:14:28 -0000",
            "username": "tartine"
        }
}
```

##UsersBroadcasters Instance resource <code>('/users/\<username\>/broadcasters/\<broadcaster_name\>') </code>

<strong>DELETE</strong> - stop following someone.

```
curl -u <user_sid>:<auth_token> http://127.0.0.1:5000/users/reneighbor/broadcasters/tartine
```

Response:
```
<HTTP/1.1 204 NO CONTENT>
```