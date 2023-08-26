class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "17271772"
    API_HASH = "897542330c90728e4e7fef57f42f9c79"

    CASH_API_KEY = "0M8D88P4CFI5IRWV"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://whmsjwvo:TLSqRVV2CZUmcgucaUFCFHBgphae4FQJ@mahmud.db.elephantsql.com/whmsjwvo"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Aditya:Aditya@cluster0.c3pct2l.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/78fb5f72eed2924496fba.jpg"

    SUPPORT_CHAT = "Animes_Chats_Group"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6491711914:AAGp7ejZAJU22nM0di2WqAACev77uiNYLrE"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "LINEPYSL065A"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 2131967391  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
