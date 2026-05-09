import argparse
import time
from pypresence import Presence

# Setup arguments
parser = argparse.ArgumentParser(description="Discord Quest Spoofer")
parser.add_argument("client_id", help="The Discord Application ID")
args = parser.parse_args()

try:
    RPC = Presence(args.client_id)
    RPC.connect()
    RPC.update(state="In-Game", details="Completing Quest")
    
    print(f"RPC Connected for ID {args.client_id}. Press Ctrl+C to stop.")
    
    while True:
        time.sleep(15)
except Exception as e:
    print(f"Failed to connect or run: {e}")