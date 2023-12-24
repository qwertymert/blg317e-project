import os
import argparse
import yaml

# get username and password arg

parser = argparse.ArgumentParser()
parser.add_argument("--username", help="MySQL username", default="root")
parser.add_argument("--password", help="MySQL password")
args = parser.parse_args()

yaml_config = {"user": args.username, "password": args.password,
                   "host": "localhost", "database": "formula1"}

yaml.dump(yaml_config, open('db.yaml', "w"))

scripts_path = "csv_to_database"

tables = ["drivers", "circuits", "races", "driverStandings",
          "pitStops", "lapTimes", "constructors", "constructorStandings",
          "constructorResults", "qualifying", "results", "status", "seasons"]

# Creates database and tables if they don't exist
os.system(f"python create_tables.py")

# Fills tables with data if they are empty
for table in tables:
    print("Inserting table " + table + "...")
    os.system(f"python {scripts_path}/crud_{table}.py")
    
os.remove('db.yaml')