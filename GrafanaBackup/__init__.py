import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest, outputblob: func.Out[bytes]) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')
    
# Here is where I need to setup the backup library

# Get the output and write to a byte array or stream.

# bloubout.set(<bytes>)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
