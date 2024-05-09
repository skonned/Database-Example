#docstring- Darren Leung- animal database application
#imports
import sqlite3

#constants and variables
DATABASE = "animals.db"


#functions
def print_all_animals():
    '''print all the animals nicely'''
    db = sqlite3.connect("animals.db")
    cursor = db.cursor()
    sql = "SELECT * FROM animal;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Name                Species                       Habitat                                 Diet                                    Average_lifespan              Average_weight                Status")
    for animal in results:
        print(f"{animal[1]:<20}{animal[2]:<30}{animal[3]:<40}{animal[4]:<40}{animal[5]:<30}{animal[6]:<30}{animal[7]:<30}")
    #loop finished here
    db.close()




#main code
print_all_animals()