Simple tutorial on how to create an API with Python/Flask


# create Test Db

python models.py 

This will create a main.db file which is a simple sqlite3 db.

Inside this there is a table called **notes**

I Inserted data manually

select * from notes;
1|tim|in hk|1-Jan-2009|Mr T|3


# Start the App 

Now exit the Models.py and

python app.py

You should see the "Connect to port on 127.0.0.0.1" Type of stuff....

If so  - Great.

In a browser open

   http://127.0.0.1:5000/notes/
   
 You should see the following data
 
 ```python
[
    {
        "id": 1,
        "title": "tim",
        "description": "in hk",
        "create_at": "1-Jan-2009",
        "create_by": "Mr T",
        "priority": 3
    }
]
```


## Query by a key

Assuming your data looks like above we now can query from

http://127.0.0.1:5000/notes/?id=1