from handlers.rewards_handler import *

url_patterns = [
    (r'/rewards', RewardsHandler),
    (r'/customerdata',FetchCustomerDataHandler),
    (r'/add', AddCustomerDataHandler),
    (r'/test', TestHandler),
]
