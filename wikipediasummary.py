import wikipedia

def getsumm(object):
    return wikipedia.summary(object, sentences=1)