import string

while True:
    phrase = raw_input()
    if phrase == '.':
        break
    word_list = {}
    letters = ''
    for word in phrase.split():
        try:
            word_list[word[0]][word] += len(word) - 2
        except KeyError:
            try:
                word_list[word[0]][word] = len(word) - 2
            except Exception:
                word_list[word[0]] = {word : len(word) - 2}
        #print word_list[word[0]][word], word

    abbrv = []
    #print "hehehehehe"
    for key, subdict in word_list.items():
        best = 0
        #print key, subdict
        for key2, value in subdict.items():
            if value >= best:
                word = key2
                best = value
        if best > 0:
            abbrv.append(word)
            letters += word[0]

    # for letter in string.ascii_lowercase:
    #     try:
    #         word_list[letter].sort(key=len)
    #         count += 1
    #         letters += letter
    #     except KeyError:
    #         pass
    for word in phrase.split():
        if word in abbrv:
            print "%c." % word[0],
        else:
            print word,
    print
    print len(abbrv)
    for abb in sorted(abbrv):
        print "%c. = %s" % (abb[0], abb)
