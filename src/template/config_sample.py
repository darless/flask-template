# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI='sqlite:///{{project}}.db'

# Flask secret key
SECRET_KEY = 'vuudooh6ao2oojoon2bipheeK1phoo'

# Log configuration
LOG_PATH = '{{project}}.log'
LOG_CONFIG = {
  'version': 1,
  'formatters': {
    'default': {
      'format': '[%(asctime)s] %(levelname)-8s %(module)s - %(funcName)s - %(message)s',
    },
  },
  'handlers': {
    'file': {
      'class': 'logging.FileHandler',
      'formatter': 'default',
      'filename': LOG_PATH,
    },
  },
  'loggers': {
  },
  'root': { 'handlers': ['file'] },
}
