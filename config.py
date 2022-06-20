## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCnkq7VY5RnGyvY7tvCAu3lvLZxZ6hgzXAf1I2W0ujAzTKUUcv9Pm01INUtykmfr-r3hitHpYJwPxf_4q9mhy4ggbfiqtkreJFD0-x9WHr4KGObnmsjwadGk012X77yeFBe4nxrsCZKC4q8EvQMNJtiAkxzF0ufqICW__nfS7heDbT3BdEQez5Vijcll5fW52axR9JuL7aHtlbom3XqxeUWbic6NN4Scqu4_rb6KE7t_4ZOOTv5uP9x2KFLgEkWyqqyMfTJNqitQACtQAf0Uit2e8q5mVXuRj2-ohIF-84RsNRMpMuar_ASU_aH80fN8eGr7YAMX45Ha_wSNtYB5cAdAAAAATwL28gA")
BOT_TOKEN = getenv("BOT_TOKEN", "5564525715:AAGHRk7RhGicEOWG5Xz4t2Hsm6NKgmKL2pg")
BOT_NAME = getenv("BOT_NAME", "𓋾☾¹َِ♡𝐌𝐔𝐒𝐈𝐂 𝐈𝐑𝐀𝐎☽")
API_ID = int(getenv("API_ID", "9461038"))
API_HASH = getenv("API_HASH", "99a7ca8c907af2d5096dfd862787d2c5")
OWNER_NAME = getenv("OWNER_NAME", "⤿ 𓋾☾¹َِ♡☽ ⌯ عـﮧ͡ـ̷ٰ̯ــرآق ⤾")
OWNER_USERNAME = getenv("OWNER_USERNAME", "AM1FO")
ALIVE_NAME = getenv("ALIVE_NAME", "⤿ 𓋾☾¹َِ♡☽ ⌯ عـﮧ͡ـ̷ٰ̯ــرآق ⤾")
BOT_USERNAME = getenv("BOT_USERNAME", "musi_6cBoT")
OWNER_ID = getenv("OWNER_ID", "1854384004")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "a2ar2a")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "nbbn3")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "nbbn3")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1567676095").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
