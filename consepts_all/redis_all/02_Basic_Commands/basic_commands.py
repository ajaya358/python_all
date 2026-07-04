# Redis Basic Commands - All data types with Python
# pip install redis
# Start: docker run -d -p 6379:6379 redis

import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

print("=== String Commands ===")
print("""
r.set('name', 'Ajay')           # SET name Ajay
r.get('name')                   # GET name → 'Ajay'
r.set('age', 25)
r.incr('age')                   # age = 26
r.incrby('age', 5)              # age = 31
r.decr('age')                   # age = 30
r.append('name', ' Kumar')      # 'Ajay Kumar'
r.strlen('name')                # length of string

# With TTL (expire after 60 seconds)
r.set('otp', '123456', ex=60)
r.ttl('otp')                    # seconds remaining
r.persist('otp')                # remove expiry
""")

print("=== Hash Commands (store objects) ===")
print("""
r.hset('user:1', mapping={'name': 'Ajay', 'age': '25', 'email': 'ajay@email.com'})
r.hget('user:1', 'name')        # 'Ajay'
r.hgetall('user:1')             # {'name': 'Ajay', 'age': '25', ...}
r.hmget('user:1', 'name', 'age')# ['Ajay', '25']
r.hset('user:1', 'age', '26')   # update one field
r.hdel('user:1', 'email')       # delete field
r.hexists('user:1', 'name')     # True
r.hkeys('user:1')               # ['name', 'age']
r.hlen('user:1')                # number of fields
""")

print("=== List Commands ===")
print("""
r.rpush('tasks', 'task1', 'task2', 'task3')  # push to right
r.lpush('tasks', 'task0')                    # push to left
r.lrange('tasks', 0, -1)                     # get all: ['task0','task1','task2','task3']
r.lpop('tasks')                              # pop from left → 'task0'
r.rpop('tasks')                              # pop from right → 'task3'
r.llen('tasks')                              # length
r.lindex('tasks', 0)                         # get by index
""")

print("=== Set Commands ===")
print("""
r.sadd('tags', 'python', 'fastapi', 'redis')
r.smembers('tags')              # {'python', 'fastapi', 'redis'}
r.sismember('tags', 'python')   # True
r.srem('tags', 'redis')         # remove member
r.scard('tags')                 # count members
r.sunion('tags', 'more_tags')   # union of two sets
r.sinter('tags', 'more_tags')   # intersection
""")

print("=== Sorted Set Commands (leaderboard) ===")
print("""
r.zadd('scores', {'Ajay': 100, 'Ravi': 85, 'Priya': 95})
r.zrange('scores', 0, -1, withscores=True)   # ascending
r.zrevrange('scores', 0, -1, withscores=True)# descending (leaderboard)
r.zscore('scores', 'Ajay')                   # 100.0
r.zrank('scores', 'Ajay')                    # rank (0-based)
r.zincrby('scores', 10, 'Ravi')              # Ravi score = 95
""")

print("=== Key Management ===")
print("""
r.exists('name')                # 1 if exists
r.delete('name')                # delete key
r.keys('user:*')                # find keys by pattern
r.expire('session', 3600)       # set TTL
r.ttl('session')                # time remaining
r.type('name')                  # 'string'
r.flushdb()                     # clear all keys (careful!)
""")
