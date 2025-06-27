import logging
import os
# ALL COMMON FUNCTIONS THAT WE REUSE IN PROJECT GOES HERE
def setup_logging():
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
   
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s'
    )
   
    # Add console handler for Flask output
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger('').addHandler(console)
 