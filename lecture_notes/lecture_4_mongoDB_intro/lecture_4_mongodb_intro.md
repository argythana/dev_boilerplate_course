## Lecture 4: Introduction to MongoDB

Lecture objectives:
* Into to json, bson, wiredtiger file types.
* Install MongoDB, necessary additional tools.
* Connect to local mongoDB and intro to different command environments.  
* Dump a mongoDB database. Show Dump path directory.
* Restore a mongoDB database. Show restore path directory.
* Show basic mongo shell commands.
* Show filtering, sorting in Compass GUI and in mongosh.
* Show authentication in Compass GUI and in mongosh.  

You are encouraged to take the courses at [MongoDv University](https://learn.mongodb.com/)
Please check the free for students course that offers "Certificate of completion".  

Next lecture:  
* Use mongo via python modules.  
* Show basic pymongo usage, commands. 
* [For more reading please take the free mongoDB python course](https://learn.mongodb.com/learning-paths/using-mongodb-with-python)


### MongoDB file types
[json files](https://en.wikipedia.org/wiki/JSON)

[bson files](https://www.mongodb.com/basics/bson)

[Difference between json and bson files](https://www.mongodb.com/basics/bson-vs-json)

[Wiredtiger files](https://source.wiredtiger.com/develop/arch-data-file.html)

[Wiredtiger storage engine in MongoDB](https://docs.mongodb.com/manual/core/wiredtiger/#wiredtiger-file-types)


### Install MongoDB, Mongo Compass GUI, mongo shell, mongo database tools  

  
Show the difference between Mongo shell commands, CLI mongo commands, python pymongo module.  

[Install MongoDB on Windows](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)

[Install MongoDB on Ubuntu](https://www.mongodb.com/docs/manual/administration/install-on-linux/)


[Intro to DB backup and restore](https://www.mongodb.com/en/basics/backup-and-restore)

### Mongo "stand-alone" database tools
https://www.mongodb.com/docs/database-tools/   
[Install mongo database tools](https://www.mongodb.com/docs/database-tools/installation/installation/)

**Add mongo tools and mongo shell to PATH.**

### Mongo shell 
The MongoDB Shell, mongosh, is a JavaScript and Node.js REPL environment for interacting with MongoDB deployments in:  
* Atlas,
* locally,
* or on another remote host.    

Use the MongoDB Shell to test queries and interact with the data in your MongoDB database.  

[Read the docs](https://www.mongodb.com/docs/mongodb-shell/)

[Install mongosh](https://docs.mongodb.com/mongodb-shell/install/)

[Start mongosh to connect to a DB](https://www.mongodb.com/docs/mongodb-shell/connect/)


### Mongo config
To see mongo configs:  
`cat /etc/mongodb.conf`  

To see mongo stored files:  
`ls -l /var/lib/mongodb/`  


### Mongo [dump](https://www.mongodb.com/docs/database-tools/mongodump/)
 `mongodump` is a utility for creating backups of MongoDB databases.    
 It's not part of the ongoing operation of the `mongod` process.     
 It's a separate process that you run ad-hoc.  
 It's not a service or a daemon, and it doesn't run in the background.  

`mongodump` can connect to `mongod` and `mongosh` instances.  
Run mongodump from the system command line, not the mongo shell.


To dump the collection named `users` from a database named `mydb` and store it in `/home/user/backups`:
`mongodump --db mydb --collection users --out /home/user/backups`

e.g. (This is what I use in the `analytics` project):  
`mongodump --db r4mAcademy --collection first_collection --out /home/tharg/venv_projects/r4m/analytics/src/test_mongo_dump/`  

For large files zip the dump folder:  
`mongodump --db r4mAcademy --collection first_collection --archive=/home/tharg/venv_projects/r4m/analytics/src/test_mongo_dump/dump.gz --gzip`

Useful links: 
https://stackoverflow.com/questions/10128719/is-it-possible-to-specify-a-directory-folder-for-mongodump   

https://stackoverflow.com/a/11554877   


To rsync to a remote server:  
`rsync -avz -e ssh /home/tharg/venv_projects/r4m/analytics/src/test_mongo_dump/dump.gz tharg@remote_server:/remote/path/to/dump.gz`  

`rsync -avz /local/path/to/dump.gz user@remote_server:/remote/path/to/dump.gz`  

e.g.  from local `analytics/src` path:
`rsync -avz ./test_mongo_dump/dump.gz root@<CONTABO_IP:/home/projects/r4m/analytics/src/test_mongo_dump/`



If the directory does not exist:  
`ssh user@remote_server "mkdir -p /remote/path/dump_directory/" && rsync -avz /local/path/to/dump.gz user@remote_server:/remote/path/dump_directory/`

### Mongo [restore](https://www.mongodb.com/docs/database-tools/mongorestore/)

The mongorestore program loads data from either a binary database dump created by mongodump or the standard input into a mongod or mongos instance.  
Run mongorestore from the system command line, not the mongo shell.

To restore an unzipped dump:
`mongorestore --db r4mAcademy --collection first_collection /home/tharg/venv_projects/r4m/analytics/src/test_mongo_dump/r4mAcademy/first_collection.bson`

In Contabo server:
$ mongorestore --db r4mAcademy --collection first_collection /home/projects/r4m/analytics/src/test_mongo_dump/r4mAcademy/first_collection.bson
2024-01-05T16:17:40.017+0100	5593 document(s) restored successfully. 0 document(s) failed to restore.

[venv_analytics] root@vmi1309641:/home/projects/r4m/analytics/src (main) 
$ mongorestore --db analyticsProd --collection daily_users /var/lib/mongodb/analyticsProd/daily_users.bson --drop
The --drop option drops the collection before restoring the data from the input dump files.   
--drop is NOT the default for mongorestore when restoring to a non-empty collection using the --db --collection options.
--drop is NOT the default for mongorestore when restoring using nsInclude.

To restore a zipped dump:  
`mongorestore --db r4mAcademy --collection first_collection --gzip /home/tharg/venv_projects/r4m/analytics/src/test_mongo_dump/dump.gz/r4mAcademy/first_collection.bson.gz`

This works OK:  
[venv_analytics] root@vmi1309641:/home/projects/r4m/analytics/src (main) 
$ mongorestore --nsInclude 'analyticsProd.daily_acts' /var/lib/mongodb/analyticsProd/daily_acts.bson --drop | mongorestore --nsInclude 'analyticsProd.daily_users' /var/lib/mongodb/analyticsProd/daily_users.bson --drop


### Mondo commands, filtering, sorting aggregations. Compass GUI and mongosh.


### Intro to pymongo
