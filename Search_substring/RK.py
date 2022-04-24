def substr_search(str, substr):
    if len(str) < len(substr):
        raise Exception
    p = 223  # простое число , 223 для уменьшения числа коллизий
    p_pow = [1, ]
    for i in range(len(str) - 1):
        p_pow.append(p_pow[i] * p)

    hash_p = [0] * len(str)
    for i in range(len(str)):
        hash_p[i] = (ord(str[i]) - ord('a') + 1) * p_pow[i]
        if i != 0:
            hash_p[i] += hash_p[i - 1]

    """Хэш подстроки"""
    hash_substr = 0
    for i in range(len(substr)):
        hash_substr += (ord(substr[i]) - ord('a') + 1) * p_pow[i]

    """перебираем все подстроки и сравниваем их"""
    i = 0
    while i + len(substr) - 1 < len(str):
        current = hash_p[i - 1 + len(substr)]
        if i:
            current -= hash_p[i - 1]
        # приводим хэши к одной степени и сравниваем
        if current == hash_substr * p_pow[i]:
            return i
        i += 1
