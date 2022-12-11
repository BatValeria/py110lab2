def pow_gen(base: int):
    num_ = 0
    while True:
            yield base ** num_
            num_ += 1
    return  None
    ...  # TODO записать функцию-генератор


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))