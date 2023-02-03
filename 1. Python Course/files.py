import os

# Python has functions for creating, reading, updating, and deleting files.
test_es = open("test.txt", "w") # "w"->Dosyayı sıfırdan oluşturur eski dosyanın üzerine yazar

# Get some info
print("Name: ", test_es.name)
print("Is closed: ", test_es.closed)
print("Opening Mode: ", test_es.mode)

# Write to file
test_es.write("deneme")
test_es.write(" bir ki üç")
test_es.close()
print("Is closed: ", test_es.closed)

# Append to file
test_es=open("test.txt","a") # "a"-> Bulunan dosyaya ekleme yapar
test_es.write("\nŞarkımız bir bana çalsın")
test_es.close()

# Read from file
test_es = open("test.txt","r+")
text_es = test_es.read(100)
print(text_es)
test_es.close()

###os.remove("test.txt")    ->  # Remove file