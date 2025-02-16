import argparse

def arg_parse_cmd():
    parser = argparse.ArgumentParser(
        description = 'Equity Database Refresher'
    )
    parser.add_argument(
        '--env_type',
        required=True,
        choices=['dev', 'local'],        
        type=str,
        help='''Provide environment type:
        dev or local where dev is your local machine.
        This is used to get the yaml config node specific to an environment and to correctly export secrets from env variables or .env.`env_type` file.'''
    )
    parser.add_argument(
        '--request_type',
        required=True,
        choices=['statistics'],        
        type=str,
        help='Whether the database refresher should run for general company statistics or other types. With current release only company statistics are requested.'
    )
    parser.add_argument(        
        '--secrets_env',
        required=False,
        choices=[True, False],
        default=False,
        type=bool,
        help='''Whether this app should use env file for secrets load.
        Defaults to False. When False make sur you exported the rapid api key as RAPIDAPI_KEY.
        If set to True make sure a file is present in the root folder of this project.
        In the .env.dev or .env.local file place RAPIDAPI_KEY value.'''
)
    return parser