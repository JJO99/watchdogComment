from pythonDIR import json_analysis, url_return


class Analyse(json_analysis.check):
    def one_total_check(self):
        m = self.articlecheck()
        n = self.commentcheck()
        if m is None and n is None:
            return None
        else:
            a = self.articleid
            url = url_return.one_url_return(a)
            return url

    def list_total_check(self):
        idlist = []
        for i in self.articleid:
            cube = json_analysis.check(self.driver, i)
            n = cube.articlecheck()
            m = cube.commentcheck()
            if m is None and n is None:
                continue
            else:
                idlist.append(n)
                idlist.append(m)

        idlist = list(set(idlist))
        if not idlist is None:
            urllist = url_return.list_url_return(idlist)
            urllist = str(urllist)
            return urllist
        else:
            return "0"
