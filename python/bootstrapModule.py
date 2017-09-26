#!/usr/bin/env python
'''
file di partenza per script python
contiene preimpostazioni per
log
argparse

allanon

'''

import argparse


def set_easy_logger(name, verbosity, file=False):
    import logging
    level = getattr(logging, verbosity, None)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # create file handler
    if file:
        try:
            fh = logging.FileHandler(file)
            fh.setLevel(level)
            fh.setFormatter(formatter)
            # add the handler to logger
            logger.addHandler(fh)
        except IOError as e:
            print e

    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    # add the handler to logger
    logger.addHandler(ch)
    # finally, return the logger
    return logger


def options():
    parser = argparse.ArgumentParser(description='''
    place your description here
    '''
                                     )
    parser.add_argument(
        '-v',
        '--verbosity',
        help='set verbosity',
        choices=[
            'debug',
            'info',
            'warning',
            'error',
            'critical'],
        default='warning')
    parser.add_argument('-l', '--filelog', help='log output to a file',
                        default=False)
    return parser.parse_args()


def main():
    pass


if __name__ == "__main__":
    args = options()
    logger = set_easy_logger(
        'nome di prova',
        args.verbosity.upper(),
        args.filelog)

    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
    main()
