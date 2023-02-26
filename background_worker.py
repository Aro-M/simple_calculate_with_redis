import redis

with redis.Redis() as client:
    while True:
        answer_numbers = client.brpop('input_numbers')[1].decode('utf-8')
        answer = eval(answer_numbers)
        print(client.lpush("answers", answer))