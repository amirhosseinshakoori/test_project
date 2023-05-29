import random
import uuid
import hashlib
import getpass
import json
import datetime
import re
from typing import List, Tuple

MIN_BALANCE = 10_000 # Minimum balance of 10_000T
FEE = 0.005 # 0.005T fee per transaction   