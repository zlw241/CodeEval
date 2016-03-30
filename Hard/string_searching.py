

def isSubstring(string, sub):
    if '\*' in sub:
        sub = sub.split('\*')
        sub = '[*]'.join(sub)
    if '*' in sub:
        sub = sub.split('*')
        sub = '.*'.join(sub)
    re_match = re.compile(r'%s' % sub)
    mo = re_match.search(string)
    if mo:
        return 'true'
    else:
        return 'false'
