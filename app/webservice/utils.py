import pathlib
import sys


class NoUvicornException(Exception):

    def __init__(self, port=5000):
        """Explain how to start webservice using uvicorn
        """
        self.port = port

    def __str__(self):
        return(
            f"It is recommended to run this program with the command:\n\n"
            f"    uvicorn main:app --reload --debug --host 0.0.0.0 --port {self.port}\n\n"
            f"Note: This command makes the service available to everyone in the network.\n"
            f"To restrict to connections only from the current host, change host to 127.0.0.1.\n"
        )
