import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

redis_client.set("key", "9999")
redis_client.set("id", "1234")
redis_client.set("name", "John Doe")
redis_client.set("name", "Jose Cortez")

name = redis_client.get("name")
id = redis_client.get("id")
print(id, name) # returns 1234, Jose Cortez