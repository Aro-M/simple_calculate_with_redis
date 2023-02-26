import redis

with redis.Redis() as client:
    while True:
        input_numbers = input("Input numbers and operator::: ") # For example 2-5 or 2+5+5-8/7*25
        client.lpush("input_numbers", input_numbers)

        answer = client.brpop('answers')[1].decode('utf-8')
        print(f"Answer: {answer}")
