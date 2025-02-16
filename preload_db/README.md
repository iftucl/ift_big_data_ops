# DB OPS: LOAD FROM RAPID-API


Operational script to keep teaching database up-to-date.


## HOWTO

to run this script, you will need to have a valid RapidApi key. To obtain, log-in to your personal account and get your personal key.

Once you obtain your personal key, you have two choices to pass the script to this app.

1. Export the key with naming.
2. setup a .env.dev file in the root directory of this folder.

Once this has been done, you can run the script by using the following commands:

```bash
cd preload_db
poetry install
poetry run main.py --env="dev" --

```

## CURRENT RELEASE

In current release, there is one option only which retrieves company statics from rapid api.