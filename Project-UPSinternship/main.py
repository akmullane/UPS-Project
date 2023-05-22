
from ALL import check_for_updates
import time



while True:
    check_for_updates()
    time.sleep(5)# Sleep for 1 minute before checking again
    print("===========================================")
