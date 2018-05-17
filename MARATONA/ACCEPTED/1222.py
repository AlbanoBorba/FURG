while True:
    try:
        N, L, C = map(int, raw_input().split())
    except EOFError:
        break
    words = raw_input()
    chars_this_line = 0
    lines = 0
    pages = 1
    for word in words.split():
        if len(word) + chars_this_line <= C:
            chars_this_line += len(word) + 1
            #print word,
        else:
            lines += 1
            #print
            chars_this_line = len(word) + 1
            #print word,
            if lines == L:
                lines = 0
                pages += 1
                
    print pages