def recite(start_verse, end_verse):
    text = [
        "I know an old lady who swallowed a fly.",
        "I don't know why she swallowed the fly. Perhaps she'll die.",
        "",
        "I know an old lady who swallowed a spider.",
        "It wriggled and jiggled and tickled inside her.",
        "She swallowed the spider to catch the fly.",
        "I don't know why she swallowed the fly. Perhaps she'll die.",
        "",
        "I know an old lady who swallowed a bird.",
        "How absurd to swallow a bird!",
        "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
        "She swallowed the spider to catch the fly.",
        "I don't know why she swallowed the fly. Perhaps she'll die.",
        "",
        "I know an old lady who swallowed a cat.",
        "Imagine that, to swallow a cat!",
        "She swallowed the cat to catch the bird.",
        "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
        "She swallowed the spider to catch the fly.",
        "I don't know why she swallowed the fly. Perhaps she'll die.",
        "",
        "I know an old lady who swallowed a dog.",
        "What a hog, to swallow a dog!",
        "She swallowed the dog to catch the cat.",
        "She swallowed the cat to catch the bird.",
        "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
        "She swallowed the spider to catch the fly.",
        "I don't know why she swallowed the fly. Perhaps she'll die.",
        "",
        "I know an old lady who swallowed a goat.",
        "Just opened her throat and swallowed a goat!",
        "She swallowed the goat to catch the dog.",
        "She swallowed the dog to catch the cat.",
        "She swallowed the cat to catch the bird.",
        "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
        "She swallowed the spider to catch the fly.",
        "I don't know why she swallowed the fly. Perhaps she'll die.",
        "",
        "I know an old lady who swallowed a cow.",
        "I don't know how she swallowed a cow!",
        "She swallowed the cow to catch the goat.",
        "She swallowed the goat to catch the dog.",
        "She swallowed the dog to catch the cat.",
        "She swallowed the cat to catch the bird.",
        "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
        "She swallowed the spider to catch the fly.",
        "I don't know why she swallowed the fly. Perhaps she'll die.",
        "",
        "I know an old lady who swallowed a horse.",
        "She's dead, of course!",
        "",
    ]
    indx_start = {1:0, 2:3, 3:8,4:14,5:21,6:29,7:38,8:48}
    indx_end = {1:2, 2:7, 3:13,4:20,5:28,6:37,7:47,8:50}
    start = indx_start[start_verse]
    end = indx_end[end_verse]
    a= text[start:end]
    return a


print(recite(1,8))


