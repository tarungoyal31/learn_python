def new(num_blocks = 256):
  aMap = []
  for i in range(0,num_blocks):
    aMap.append([])
  return aMap

def hash_key(aMap, key):
  return hash(key) % len(aMap)

def get_bucket(aMap, key):
  return aMap[hash_key(aMap, key)]

def get_slot(aMap, key):
  bucket = get_bucket(aMap, key)
  for i,kv in enumerate(bucket):
    k,v = kv
    if k == key:
      return i,k,v
  return -1,key,None

def get(aMap, key):
  i,k,v = get_slot(aMap, key)
  return v

def set(aMap, key, val):
  i,k,v = get_slot(aMap, key)
  hashKey = hash_key(aMap, key)
  if i>=0 and v != None:
    aMap[hashKey][i] = key, val
  else:
    aMap[hashKey].append((key, val))

def delete(aMap, key): #del is reserved for deleting
  i,k,v = get_slot(aMap,key)
  bucket = get_bucket(aMap, key)
  if i >= 0:
    del bucket[i]

def list(aMap):
  for x in aMap:
    for k,v in x:
      print k,v
