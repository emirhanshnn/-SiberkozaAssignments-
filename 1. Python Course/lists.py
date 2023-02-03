# A List is a collection which is ordered and changeable. Allows duplicate members.
top11_es = ["Muslera", "Boey", "Nelson", "Abdülkerim","Anholt", "Torreira", "Oliveira", "Kerem", "rashica","Mertens", "Icardi"]

#1)Get a value
print("\n\n1)")
print(top11_es[0])
print(len(top11_es))
print("\n\n2)")

#push_back & pop_back
top11_es.append("Kaan")
print(top11_es)
top11_es.pop()
print(top11_es)
print("\n\n3)")

#insert & remove
top11_es.remove("Anholt") #= top11_es.pop(4)
top11_es.insert(4,"Kaan")
print(top11_es)
print("\n\n4)")

#Sort
top11_es.reverse()
print(top11_es)
top11_es.sort()
print(top11_es)
top11_es.sort(reverse=True)
print(top11_es)