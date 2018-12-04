def hilite(string, status, bold):
    attr = []
    if status:
        attr.append('32') # GREEN
    else:
        attr.append('31') # RED
    if bold:
        attr.append('1')
    return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
