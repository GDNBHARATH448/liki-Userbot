from dotenv import load_dotenv
from os import getenv

load_dotenv()

# Required Variables
API_ID = int(getenv("API_ID", "29896633"))
API_HASH = getenv("API_HASH", "7a8a6dd1c08f6ffc33645885bb3ecf77")
BOT_TOKEN = getenv("BOT_TOKEN", "7774813193:AAE4fvtbnth_53OIsxheB9AsLxrsskBMSxg")
STRING_SESSION = getenv("STRING_SESSION", "BQHIL7kAq14Mf16IxARSrnIF0BTO-e-DXBw_tGYVQHXiBoszcYeXRdn-Ldp1bywakvkbnks4YCZCjsB1C34kQzm_vcactqjp3o4S00gBwCibqTuykkIMwZAS-vGolqfvKUsmz5SfIGNG0Ra9MCkyY2ebEc7FKgwVrJ20_NE_uPdI1Aq8c3JEIUUql6TOc5VYRPrkP6n66XtroYoVBgbeW92gmPmc1Eq6PBCbLEjfX9LY7IwAqGZPJpaETNvL18wmIwAW7n0LkH6uMJzEg0C2O8ccGfkj5SQXiMYcA4Y4pU9DhikMMm6Z3yNKkD9_fNi3hAMxjdmII8NrsCSiNjsB6ZfX9ibm-AAAAAHg2_WeAA")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-4962500437"))


# Optional Variables
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())


# Don't Change After This Line.
COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')
