import os
import logging
from dotenv import load_dotenv
import ldclient
from ldclient.config import Config
from ldclient import Context

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

class LaunchDarklyService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LaunchDarklyService, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        sdk_key = os.getenv('LD_SDK_KEY')
        
        if not sdk_key:
            logger.error("LD_SDK_KEY not found --> Check your .env file.")
            self.client = None
            return

        ldclient.set_config(Config(sdk_key))
        self.client = ldclient.get()
        
        if self.client.is_initialized():
            logger.info("LaunchDarkly SDK successfully initialized.")
        else:
            logger.error("LaunchDarkly SDK failed to initialize.")

    def get_flag(self, flag_key: str, context: Context, default: bool = False) -> tuple:
        if not self.client:
            return default, {"kind": "ERROR", "errorKind": "CLIENT_NOT_INITIALIZED"}
        
        detail = self.client.variation_detail(flag_key, context, default)
        return detail.value, detail.reason

    def track_event(self, event_key: str, context: Context):
        if self.client:
            self.client.track(event_key, context)

    def close(self):
        if self.client:
            self.client.close()
            logger.info("LaunchDarkly connection closed.")

ld_service = LaunchDarklyService()
