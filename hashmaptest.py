import hashmap

aMap = hashmap.new()
hashmap.set(aMap,10,"ten")
hashmap.set(aMap,20,"twenty")
print hashmap.get(aMap,10)
print "Old hashmap:"
hashmap.list(aMap)
hashmap.delete(aMap,10)
hashmap.set(aMap,20,"2*10")
print "New hashmap:"
hashmap.list(aMap)


