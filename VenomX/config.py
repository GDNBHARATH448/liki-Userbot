from dotenv import load_dotenv
from os import getenv

load_dotenv()

# Required Variables
API_ID = int(getenv("API_ID", "29896633"))
API_HASH = getenv("API_HASH", "7a8a6dd1c08f6ffc33645885bb3ecf77")
BOT_TOKEN = getenv("BOT_TOKEN", "8086803748:AAH1sdJ8qNN-WhWMH-0142__DuNUOR_15wA")
STRING_SESSION = getenv("STRING_SESSION", "BQHIL7kAldBjt5SiZNWj2iDpiESaSnGHIs6cKbzEiU6mk2Cn14pM63L2LyhMAMUnTfVpxYU6PhqbjOUn1AFjFHivmT8m_gb1FhlEn2cem1H2cIRFaoNV6UHNqZIawILVJZP5VmQyYdz0LbHmJzbH19tUv89lKlAwlmnk5Y9F4EC2q1eHfyrlWzbiJMPCqeC1Yd8p2ULMcKBJK54LVUqJpOmYoxv2BOqqT1ikL265H-GImsHOPUWgDCC0hFxrMPOei6RPWowfowvJQNrHLjEPiIPyOnZIqzKbnKz-fe8IE3R73hY-fxWaozBYw-3r6dghTkW1GOjNiKdJ7AEckELd0W3444K7KQAAAAHHQbCyAA")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002861498908"))


# Optional Variables
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())


# Don't Change After This Line.
COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')
