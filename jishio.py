#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib2
import html2text


class JishioGrabber(object):
    def __init__(self):
        super(JishioGrabber, self).__init__()
        self.x = None
    #japword=u"岡".encode('utf-8')
    #engword=u"mother".encode('utf-8')
    def findword(self, japword=u"", engword=""):
        x = urllib2.urlopen("http://m.jisho.org/words?jap="+japword+"&eng="+engword+"&dict=edict")
        x = x.read()
        textfromhtml = html2text.html2text(x.decode('utf-8'))
        textfromhtml = textfromhtml.split(u'* * *'.encode('utf-8'))
        for i in range(len(textfromhtml)):
            try:
                textfromhtml[i-1] = textfromhtml[i-1].replace(u'\n'.encode('utf-8'), '')
            except:
                pass
        self.numberofwords = textfromhtml[1]
        self.wholewords = textfromhtml[2:len(textfromhtml)-3]
        print self.numberofwords
        print len(self.wholewords)
    def word(self, number=0):

        if (len(self.wholewords) < 5) and (number == 0):
            self.words = u'\n'.encode('utf-8').join(self.wholewords)
            return self.words

        if (len(self.wholewords) > 5) and (bool(number) is True):
            self.words = u'\n'.encode('utf-8').join(self.wholewords[:number])
            return self.words

        if (len(self.wholewords) > 5) and (number == 0):
            self.words = u'\n'.encode('utf-8').join(self.wholewords[:5])
            return self.words

        else:
            print "boo"


JishioGrabberX = JishioGrabber()
moe = "mother"
engw = u"%s".encode('utf-8') % moe
JishioGrabberX.findword(engword=engw)
print JishioGrabberX.word()