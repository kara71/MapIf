#!/usr/bin/python3
# -!- encoding:utf8 -!-

# ------------------------------------------------------------------------------------------
#                                    IMPORTS & GLOBALS
# ------------------------------------------------------------------------------------------

import configparser
import os
from src.utils import logger

_CONFIG_ = None

# ------------------------------------------------------------------------------------------
#                               EXTERN FUNCTIONS
# ------------------------------------------------------------------------------------------


def init_config(filename):
    global _CONFIG_
    ok = False
    if not _CONFIG_:
        _CONFIG_ = configparser.ConfigParser()
        if len(_CONFIG_.read(filename)) > 0:
            logger.mprint('Configuration file {0} successfully loaded !'.format(filename))
            ok = True
        else:
            logger.log_error("Configuration file {0} can't be loaded !".format(filename))
    else:
        logger.mprint('Configuration file has already been loaded !')
    return ok


def getenv(env_var):
    return os.getenv(varname, None)


def config(section, option, env_var=None, default=None, boolean=False):
    res = None
    # try to search for environement var if not None
    if env_var:
        res = getenv(env_var)
    # then search in INI config if env var not found
    if not res:
        if _CONFIG_:
            if section in _CONFIG_.sections():
                if option in _CONFIG_[section]:
                    if boolean:
                        res = _CONFIG_[section].getboolean(option)
                    else:
                        res = _CONFIG_[section][option]
                else:
                    logger.mprint("Missing option {0} in section {1} in configuration file !".format(option, section))
                    if default:
                        logger.mprint("Using default configuration value: {0}".format(default))
                        res = default
            else:
                logger.mprint("Missing section {0} in configuration file".format(section))
                if default:
                    logger.mprint("Using default configuration value: {0}".format(default))
                    res = default
        else:
            logger.mprint("Configuration file must be loaded to use config(section, option) function ! Call init_config(filename) before !")
            if default:
                logger.mprint("Using default configuration value: {0}".format(default))
                res = default
    # finally return res
    return res

# ------------------------------ TEST ZONE BELOW THIS LINE ---------------------------------

if __name__ == '__main__':
    logger.mprint('TESTS NOT IMPLEMENTED')