#coding:utf-8

import logging
logging.basicConfig(filename='log1.log',
                    format='%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.DEBUG)

while True:
    option = input("input a digit:")
    if option.isdigit():
        print("hehe", option)
        logging.info('option correct')
    else:
        logging.error("Must input a digit!")
