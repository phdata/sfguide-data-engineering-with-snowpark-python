import os

import toml
import typer
from rich.prompt import Prompt



def main():
    username = Prompt.ask("Enter your Snowflake username name")
    password = Prompt.ask("Enter your Snowflake password", password=True)
    account_name = Prompt.ask("Enter the Snowflake account you will use (e.g. fvb60466.us-east-1)")
    db_name = Prompt.ask("Enter the name of your Snowflake database")
    role_name = Prompt.ask("Enter the name of your Snowflake role")
    warehouse_name = Prompt.ask("Enter the name of your Snowflake warehouse")
    config_location = Prompt.ask("Enter the location of your SnowSQL config",
                                 default=os.path.join(os.path.expanduser('~'),
                                                      '.snowsql/config'))


    snowsql_config = {'accountname': account_name,
                      'username': username,
                      'password': password,
                      'dbname': db_name,
                      'rolename': role_name,
                      'warehousename': warehouse_name,
                      'connections.dev': {'accountname': account_name,
                                          'username': username,
                                          'password': password,
                                          'dbname': db_name,
                                          'rolename': role_name,
                                          'warehousename': warehouse_name}}
    
    print(toml.dumps(snowsql_config))
    with open(config_location, 'w') as config_file:
        toml.dump(snowsql_config, config_file,)

if __name__ == "__main__":
    typer.run(main)
