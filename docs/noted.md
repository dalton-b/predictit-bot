## 2021.10.21
-So now that I have the database imported, I need to figure out how to efficiently access the data in it
-I think I'm struggling because I don't even know what I want. I think I need to write a spec



## 2021.10.20
-To install MongoDB, I had to download stuff from here: https://www.mongodb.com/try/download/community
-Then to import from JSON, I started with the Python tutorial here: https://www.mongodb.com/compatibility/json-to-mongodb
-Instead of the pip3 install command given, I had to run: `pip3 install 'pymongo[srv]'`
-I imported the Python script from the tutorial, changing the name
-I need to check here to replace the connection string: https://docs.mongodb.com/guides/cloud/connectionstring/
-I think I'm going to install MongoDB with homebrew, it's being finnicky: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
-Start the service with: `brew services start mongodb-community@5.0`
-I edited the python script so that connection_string = mongodb//localhost, database = predictit-bot, and collection = 2021-10-20
-I got an error, so I updated the syntax of that script based on this answer: https://stackoverflow.com/questions/49510049/how-to-import-json-file-to-mongodb-using-python
-I also had to use the raw json with everything on one line, not the fancy looking multi-line thing
-This executes without errors, but there doesn't appear to be anything in the database
-The following command worked: `mongoimport --db "predictit-bot" --collection "2021-10-20" --type json --file "2021-10-20-15-14-38.json"`
-To see the results, run `mongod`, `use predictit-bot`, `db["2021-10-20"].find().pretty()`
-I'm not sure why `show dbs` still says that there's nothing (0.00B) in the database, but it looks like there is indeed information in the database
