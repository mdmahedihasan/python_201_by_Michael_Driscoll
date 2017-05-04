def silly_generator():
    yield "python"
    yield "rocks"
    yield "so do you"

gen = silly_generator()
for item in gen:
    print(item)
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(silly_generator()))
#print(next(silly_generator()))