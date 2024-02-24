#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def example_of_use():
    """python-dotenv package
    https://pypi.org/project/python-dotenv/
    """

    # Load .env file using:
    from dotenv import load_dotenv
    # load_dotenv()
    load_dotenv(verbose=True)   # with increased verbosity

    #  find_dotenv() method that will try to find a .env file by
    # (a) guessing where to start using __file__ or the working directory
    #     -- allowing this to work in non-file contexts such as IPython
    #     notebooks and the REPL, and then
    # (b) walking up the directory tree looking for the specified file
    #     -- called .env by default.
    from dotenv import find_dotenv
    load_dotenv(find_dotenv())


if __name__ == '__main__':
    # invoke the example
    example_of_use()

    import os
    SECRET_KEY = os.getenv("EMAIL")
    print(SECRET_KEY)
    redis = os.getenv('REDIS_ADDRESS')
    print(redis)
    meaning = os.getenv('MEANING_OF_LIFE')
    print(meaning)

    import settings
    print(settings.SECRET_KEY)
    print(settings.OTHER_PASSWORD)
    print(settings.csd_staging_api_username)
