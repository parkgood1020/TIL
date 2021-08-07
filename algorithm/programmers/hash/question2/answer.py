def solution(phone_book):
    phone_book = sorted(phone_book)
    answer = True
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return answer
