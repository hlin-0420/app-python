from flask import Flask, current_app

# tag::import[]
from neo4j import GraphDatabase
# end::import[]
import os

"""
Initiate the Neo4j Driver
"""
# tag::initDriver[]
def init_driver(uri, username, password):
    # TODO: Create an instance of the driver here
    NEO4J_URI=os.getenv('NEO4J_URI')
    NEO4J_USERNAME=os.getenv('NEO4J_USERNAME')
    NEO4J_PASSWORD=os.getenv('NEO4J_PASSWORD')
    current_app.driver = GraphDatabase.driver(
        NEO4J_URI,
        auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
    )

    return current_app
# end::initDriver[]


"""
Get the instance of the Neo4j Driver created in the `initDriver` function
"""
# tag::getDriver[]
def get_driver():
    return current_app.driver

# end::getDriver[]

"""
If the driver has been instantiated, close it and all remaining open sessions
"""

# tag::closeDriver[]
def close_driver():
    if current_app.driver != None:
        current_app.driver.close()
        current_app.driver = None

        return current_app.driver
# end::closeDriver[]
