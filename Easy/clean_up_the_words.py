

def cleanup(rough):
    alpha = str.isalpha
    lower = str.lower
    clean = ''.join((lower(i) if alpha(i) else " " for i in rough))
    cleaner = clean.split()
    cleanest = ' '.join(cleaner)
    return cleanest


test = "_3lbcy<XTR&XWB[u,G':/<Jj2J~0yQz1z:%J'f,P6tIv?u:b,Le$:rBT"
print(cleanup(test))

