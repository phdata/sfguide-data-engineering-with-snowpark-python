import configparser
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

    snowsql_config = configparser.ConfigParser()
    snowsql_config["connections.dev"] = {
        'accountname': account_name,
        'username': username,
        'password': password,
        'dbname': db_name,
        'rolename': role_name,
        'warehousename': warehouse_name}
    
    with open(config_location, 'w') as config_file:
        snowsql_config.write(config_file)

    toml_configs = {
        "./steps/05_fahrenheit_to_celsius_udf/app.toml": {
            'snowsql_config_path': '~/.snowsql/config',
            'snowsql_connection_name': 'dev',
            'default': {
                'input_parameters': '(temp_f float)',
                'return_type': 'float',
                'file': 'app.zip',
                'name': 'fahrenheit_to_celsius_udf',
                'handler': 'app.main',
                'execute_as_caller': True},
            'dev': {
                'database': db_name,
                'schema': 'ANALYTICS',
                'warehouse': warehouse_name,
                'role': role_name,
                'overwrite': True}},
        "./steps/06_orders_update_sp/app.toml": {
            'snowsql_config_path': '~/.snowsql/config',
            'snowsql_connection_name': 'dev',
            'default': {'input_parameters': '()',
                        'return_type': 'string',
                        'file': 'app.zip',
                        'name': 'orders_update_sp',
                        'handler': 'app.main',
                        'execute_as_caller': True},
            'dev': {'database': db_name,
                    'schema': 'HARMONIZED',
                    'warehouse': warehouse_name,
                    'role': role_name,
                    'overwrite': True}
        },
        "./steps/07_daily_city_metrics_update_sp/app.toml": {
            'snowsql_config_path': '~/.snowsql/config',
            'snowsql_connection_name': 'dev',
            'default': {'input_parameters': '()',
                        'return_type': 'string',
                        'file': 'app.zip',
                        'name': 'daily_city_metrics_update_sp',
                        'handler': 'app.main',
                        'execute_as_caller': True},
            'dev': {'database': db_name,
                    'schema': 'ANALYTICS',
                    'warehouse': warehouse_name,
                    'role': role_name,
                    'overwrite': True}}
    }

    for filename, config in toml_configs.items():
        with open(filename, 'w') as f:
            toml.dump(config, f)

if __name__ == "__main__":
    typer.run(main)
