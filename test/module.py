class Test():
    def lis(self,chars):
        res = []
        for ele in chars:
            if ele.strip():
                res.append(ele)
        # chars1 = chars.replace(" ", "")
        # print(len(res))
        return res

    def hash(self,cha):
        q = "ad!@s"
        w = "asd$2#"
        e = "fgs*%$d"
        r = "h2s!gn"
        t = "sd%@fd2gh"
        y = "shfs2@b^"
        u = "s@1ggjsf"
        i = "shsrgb"
        o = "sthf(0%#@gb"
        p = "s&@@$thsgb"
        a = "sthb#$%@`"
        s = "sthjt%3@sd"
        d = "srusrtz$@#5gb"
        f = "6ujnx#!4rf"
        g = "sruhsr"
        h = "stuy&%@hsr"
        j = "sruj)(^n"
        k = "s5#^hb"
        l = "srt$%^u"
        z = "s#$%y#$hg"
        x = "shtb"
        c = "srtbh"
        v = "sthbr"
        b = "rujsrt"
        n = "sdthr"
        m = "seth"
        ooo = []

        for xa in cha:
            if xa == "a":
                ooo.append(a)
            elif xa == "b":
                ooo.append(b)
            elif xa == "c":
                ooo.append(c)
            elif xa == "d":
                ooo.append(d)
            elif xa == "e":
                ooo.append(e)
            elif xa == "f":
                ooo.append(f)
            elif xa == "g":
                ooo.append(g)
            elif xa == "h":
                ooo.append(h)
            elif xa == "i":
                ooo.append(i)
            elif xa == "j":
                ooo.append(j)
            elif xa == "k":
                ooo.append(k)
            elif xa == "l":
                ooo.append(l)
            elif xa == "m":
                ooo.append(m)
            elif xa == "n":
                ooo.append(n)
            elif xa == "o":
                ooo.append(o)
            elif xa == "p":
                ooo.append(p)
            elif xa == "q":
                ooo.append(q)
            elif xa == "r":
                ooo.append(r)
            elif xa == "s":
                ooo.append(s)
            elif xa == "t":
                ooo.append(t)
            elif xa == "u":
                ooo.append(u)
            elif xa == "v":
                ooo.append(v)
            elif xa == "w":
                ooo.append(w)
            elif xa == "x":
                ooo.append(x)
            elif xa == "y":
                ooo.append(y)
            elif xa == "z":
                ooo.append(z)
            else:
                ooo.append(xa)


        ok = str(ooo)
        ok1 = ok.replace("[", "")
        ok2 = ok1.replace("]", "")
        ok3 = ok2.replace("'", "")
        ok4 = ok3.replace(",", "")
        ok5 = ok4.replace(" ", "")
        
        return ok5