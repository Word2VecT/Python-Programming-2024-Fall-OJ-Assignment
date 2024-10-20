def lru_cache(n, pages):
    cache = []
    load_count = 0

    for page in pages:
        if page in cache:
            cache.remove(page)
            cache.append(page)
        else:
            load_count += 1
            if len(cache) >= n:
                cache.pop(0)
            cache.append(page)

    print(load_count)
    print(" ".join(map(str, sorted(cache))))


n, m = map(int, input().split())
pages = list(map(int, input().split()))
lru_cache(n, pages)
