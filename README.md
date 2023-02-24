# consul-tools

Intend to check-in cool tools along the way.


* get-kv-blocking.py 

  Getting started:
  ```
  / # python3 get-kv-blocking.py -k v -w 30s -i 10000
  http://127.0.0.1:8500/v1/kv/v?index=10000&wait=30s&consistent= | 200 | 2023-02-24 18:44:16.189651 | 2023-02-24 18:44:47.293173 | 0:00:31.103522 | {'LockIndex': 0, 'Key': 'v', 'Flags': 0, 'Value': 'eQ==', 'CreateIndex': 1452, 'ModifyIndex': 1452}
  / #
  ```
  
  *Info*:
  
    To get the blocking going -
  
      Set the index (-i) 
    
          E.g., I can wait for a change in the key 'v' and watch for index: 1452 from the above example.

    To wait for a specific time -
  
      Set wait (-w) to say '30s' or '9m' for 30 seconds or 9 minutes respectively.
