
import json
import redis


class redis_driver():
    def __init__(self) -> None:
        self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        pass

    def insert_history(self, conversation_key, conversation):
        for d in conversation:
            self.r.rpush(conversation_key, json.dumps(d))
        pass

    def get_history(self, conversation_key):
        json_list = self.r.lrange(conversation_key, 0, -1)
        return [json.loads(item) for item in json_list]
    