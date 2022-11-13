to_watch_words = ['this', 'is', 'a', 'real', 'real', 'real', 'story']

watched_words = []
for i in to_watch_words:
    if i not in watched_words:
        watched_words.append(i)
print(watched_words)