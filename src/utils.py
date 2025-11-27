from datetime import datetime
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger("orbis")




def now_iso():
return datetime.utcnow().isoformat() + 'Z'