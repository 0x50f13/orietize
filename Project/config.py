import logging
import os
import threading
from storage import Storage

API_KEY = "******"
DB_FILE = "bot.db"
BASE_DIR=os.path.dirname(os.path.realpath(__file__))
DEBUG=True
storage=Storage("Storagefile")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

