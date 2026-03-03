import os
import ldclient
from ldclient.config import Config
from ldclient import Context
from dotenv import load_dotenv

load_dotenv()

class LaunchDarklyService:
    def __init__(self):
        sdk_key = os.getenv("LD_SDK_KEY")
        if not sdk_key:
            raise ValueError("LD_SDK_KEY not found in environment")
        
        ldclient.set_config(Config(sdk_key))
        self.client = ldclient.get()

    def get_flag(self, flag_key, context, default=False):
        detail = self.client.variation_detail(flag_key, context, default)
        return detail.value, detail.reason

    def track_event(self, event_key, context):
        self.client.track(event_key, context)

    def close(self):
        self.client.close()

ld_service = LaunchDarklyService()
