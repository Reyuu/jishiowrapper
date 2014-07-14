#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib2


class JishioGrabber(object):
    def __init__(self):
        super(JishioGrabber, self).__init__()
        self.x = None

    def findword(self, japword="", engword=""):
        x = urllib2.urlopen("http://m.jisho.org/words?jap="+japword+"&eng="+engword+"&dict=edict")
        x = x.read()
        if x.find(" <!-- Found no words -->") != -1:
            sys.exit()
        x = x.split(' <!-- Found words -->')
        x = x[1]
        y = """<MENU>
                        <LI><A href="/words/">Words</A>
                        <LI><A href="/kanji/">Kanji</A>
                        <LI><A href="/sentences/">Sentences</A>
                    </MENU>
                </P>

                <P>
                    Denshi Jisho uses dictionaries provided by the <A HREF="http://www.edrdg.org/edrdg/licence.html">Electronic Dictionary Research and Development Group</A>.
            </BODY>
        </HTML>
        """
        index_len = len(x)-(len(y)+43+30)
        x = x[:index_len-6]
        x = x.split("<HR>")
        x = x[1:]
        for i in range(len(x)):
            x[i] = x[i].replace("\n", "")
            x[i] = x[i].split('<BR>')
            try:
                x[i].remove(x[i][1])
                for j in (0, 1):
                    x[i][j] = x[i][j].replace("<P>", "")
                    x[i][j] = x[i][j].replace("</P>", "")
            except:
                pass
            x[i][0] = x[i][0].replace("<A href=\'", "")
            x[i][0] = x[i][0].replace("</A>", "")
            x[i][0] = x[i][0].split("\'>")
            x[i].append(x[i][0][0])
            x[i][0].pop(0)
            x[i][1] = x[i][1].replace("<span class=\"tags mn_tags\" title=\"arch\">", "")
            x[i][1] = x[i][1].replace("<span class=\"tags mn_tags\" title=\"ksb:\">", "")
            x[i][1] = x[i][1].replace("</span>", "")
            x[i][1] = x[i][1].replace("   ", " ")
            self.x = x
            #kanji = x[i][0][0]
            #link = x[i][2]
            #meaning = x[i][1]

    def kanji(self, y):
        return self.x[y][0][0]

    def link(self, y):
        httpjishio = "http://jishio.org"
        return httpjishio+str(self.x[y][2])

    def meaning(self, y):
        return self.x[y][1]

Jishio = JishioGrabber()
Jishio.findword(engword="mother")
print Jishio.kanji(0)
print Jishio.link(0)
print Jishio.meaning(0)
