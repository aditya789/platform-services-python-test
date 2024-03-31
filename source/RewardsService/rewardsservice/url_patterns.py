from handlers.rewards_handler import *

url_patterns = [
    (r'/rewards', RewardsHandler),
    (r'/test', TestHandler),
]
