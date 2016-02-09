DT 01-02-2016

Restful API on SQL database with flask

This is an implementation of a simple API on a sqlite database.
It also contains an import script that will import a csv file into the sqlite db.

Running the api will also load a simple search page that will use jquery /ajax
to call the api and search in the database (work in progress).
The idea is that a search query will return all matching record IDs. After that
subsequent calls can be made to retreive record info using the IDs.

Todo:
- build authorization on the API
- Finish basic search interface for demonstration purposes.
- implement relevancy ranking
