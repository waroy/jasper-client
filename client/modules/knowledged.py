# -*- coding: utf-8-*-
import logging
import random
import re
import wolframalpha
import time
import sys
from sys import maxint

from client import jasperpath
WORDS = ["WHO", "WHAT", "HOW MUCH", "HOW MANY", "HOW OLD", "CALCULATE"]


def handle(text, mic, profile):
    app_id = profile['keys']['WOLFRAMALPHA']
    client = wolframalpha.Client(app_id)
    logger = logging.getLogger(__name__)
    query = client.query(text)
      
    #if len(query.pods) > 0:
    texts = next(query.results)
    #logger.debug( type(texts))
    if  texts is None:
	    texts = "I can not find anything"
    else:
	    texts = texts.text	       
	# pod = query.pods[1]
       # if pod.text:
       #     texts = pod.text
       # else:
       #     texts = "I can not find anything"
    mic.say(texts.replace("|",""))
    #else:
     #   mic.say("Sorry, Could you be more specific?.")




def isValid(text):
    # if re.search(r'\bwho\b', text, re.IGNORECASE):
    #     return True
    # elif re.search(r'\bwhat\b', text, re.IGNORECASE):
    #     return True
    # elif re.search(r'\bhow much\b', text, re.IGNORECASE):
    #     return True
    # elif re.search(r'\bhow MANY\b', text, re.IGNORECASE):
    #     return True
    # elif re.search(r'\bhow old\b', text, re.IGNORECASE):
    #     return True
    # elif re.search(r'\bcalculate\b', text, re.IGNORECASE):
    #     return True
    # else:
    #     return False
    return bool(re.search(r'\b(who?|what|how much|how many|how old|' +
                        r'calculate)\b', text, re.IGNORECASE))
