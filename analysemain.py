from pythonDIR import jsonanalyse, alertURLback


class Analyse(jsonanalyse.check):
    def one_total_check(self):
        m = self.articlecheck()
        n = self.commentcheck()
        if m is None and n is None:
            return None
        else:
            url = alertURLback.urlBack(self.articleid)
            return url

    def list_total_check(self):
        idlist = []
        for i in self.articleid:
            cube = jsonanalyse.check(self.driver, i)
            n = cube.articlecheck()
            m = cube.commentcheck()
            if m is None and n is None:
                continue
            else:
                idlist.append(n)
                idlist.append(m)

        idlist = list(set(idlist))
        if not idlist is None:
            urllist = alertURLback.urlBack(idlist)
            urllist = str(urllist)
            return urllist
        else:
            return "0"
