#2. Create a list of your five favorite movies. Write a for loop that prints each movie along with its position in the list (e.g., "1. Inception").
movies=["RRR","Pushpa","Bahubali","KGF","Bareliki Barfi"]
for i,movie in enumerate(movies,1):
    print(f"{i}.{movie}")