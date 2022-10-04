import sqlite3
import webbrowser
import random
import time

db_name = "GroupProject.db"
connection = sqlite3.connect(db_name)
cur = connection.cursor()


def main():
	# ------ CONSTANTS ----------
	ADDVALUE   =  1
	UPDATEVALUE  =  2
	DELETEVALUE  =  3
	PRINTVALUE = 4
	GOOGLEMAP = 5
	EXIT       =  6
	ERROR      = -1	
	
	print ("--------------------------------------------------")
	print("\nWelcome to our Database!\n")
	print ("--------------------------------------------------")
	
	choice = -1  # bogus setting to get us started
	
	while (choice != EXIT):
		print ("\n\n----------------------------------------------")
		print ("  1  -  Add a new value to a table")
		print ("  2  -  Update a value from a table")
		print ("  3  -  Delete a value from a table")
		print ("  4  -  Print values")
		print ("  5  -  Look for a location in Google Maps")
		print ("  6  -  EXIT")
		print ("--------------------------------------------------")
		choice = input("ENTER: ")

		READDATA = -1
		
		# trap bad user input
		if ( (str(READDATA) <= choice) and (choice <= str(EXIT)) ):
			# force to an integer, for example "1" to 1
			choice = eval(choice)			
		else:
			badInput = choice
			# force to an integer to test below
			choice = ERROR		
			
		# ============ 1: ADD A VALUE =============================
		if ( choice == ADDVALUE):
			ADDREVIEW = 1
			ADDLOCATION = 2
			ADDUSER  = 3
			ADDUSERRATING = 4

			print ("  1  -  Add a new Review")
			print ("  2  -  Add a new Location")
			print ("  3  -  Add a new User")
			print ("  4  -  Add a new UserRating")
			secondChoice = int(input("ENTER: "))

			if(secondChoice == ADDREVIEW):
				addReview()
			elif(secondChoice == ADDLOCATION):
				addLocation()
			elif(secondChoice == ADDUSER):
				addUser()
			elif(secondChoice == ADDUSERRATING):
				addUserRating()
			else:
				print("Wrong Input, please try again.")

		
		# ============ 2: UPDATE VALUES  =============================
		elif (choice == UPDATEVALUE):
			print ("  1  -  update User Name")
			print ("  2  -  update User Followers")
			print ("  3  -  update User Rating")
			print ("  4  -  update Review Description")
			print ("  5  -  update User Rating(entity)")
			print ("  6  -  update Location Name")
			print ("  7  -  update Location Address")
			print ("  8  -  update Location Description")
			print ("  9  -  update Location Visitor Amount")
			secondChoice = int(input("ENTER: "))

			if(secondChoice == 1):
				updateUserName()
			elif(secondChoice == 2):
				updateUserFollowers()
			elif(secondChoice == 3):
				updateUserRating()
			elif(secondChoice == 4):
				updateReviewDesc()
			elif(secondChoice == 5):
				updateReviewTime()
			elif(secondChoice == 6):
				updateLocationName()
			elif(secondChoice == 7):
				updateLocationAddress()
			elif(secondChoice == 8):
				updateLocationDesc()
			elif(secondChoice == 9):
				updateLocationVisitorAmount()
			else:
				print("Wrong Input, please try again.")
		

		# ============ 3:DELETE VALUES =============================	
		elif (choice == DELETEVALUE):
			DELETEREVIEW = 1
			DELETELOCATION = 2
			DELETEUSER  = 3
			DELTEUSERRATING = 4

			print ("  1  -  Delete a Review")
			print ("  2  -  Delete a Location")
			print ("  3  -  Delete a User")
			print ("  4  -  Delete a UserRating")
			secondChoice = int(input("ENTER: "))

			if(secondChoice == DELETEREVIEW):
				Delete_review()
			elif(secondChoice == DELETELOCATION):
				Delete_location()
			elif(secondChoice == DELETEUSER):
				Delete_user()
			elif(secondChoice == DELTEUSERRATING):
				addUserRating()
			else:
				print("Wrong Input, please try again.")
		
		# ============ 4:PRINT VALUES =============================	
		elif (choice == PRINTVALUE):
			VIEWREVIEW = 1
			VIEWLOCATION = 2
			VIEWUSER  = 3
			VIEWRATING = 4

			print ("  1  -  View Reviews")
			print ("  2  -  View Locations")
			print ("  3  -  View Users")
			print ("  4  -  View UserRatings")
			secondChoice = int(input("ENTER: "))

			if(secondChoice == VIEWREVIEW):
				viewReviews()
			elif(secondChoice == VIEWLOCATION):
				viewLocations()
			elif(secondChoice == VIEWUSER):
				viewUsers()
			elif(secondChoice == VIEWRATING):
				viewUserRating()
			else:
				print("Wrong Input, please try again.")

		# ============ 5:GOOGLE ADRESS =============================	
		elif (choice == GOOGLEMAP):
			googleMap()

		# ============ 6: EXIT =====================================	
		elif (choice == EXIT):
			connection.close()
			print ("Goodbye ...")	
		
		
		# ============ ? HUH ? =====================================
		else:  
			print ("ERROR: ", badInput, "is an invalid input. Try again.")	
	
	# end WHILE input is not EXIT
	
	print ("\n\nDone.\n")
# end main	

#_________________________________________________ADD FUNCTIONS________________________________________________________________________________________
def addReview():
	global connection
	global cur
	locName = input('To add a new review, first enter the location Name: ')
	isValid = False
	while isValid == False: 
		try:
			cur.execute("SELECT COUNT(1) FROM Location WHERE Name =?", (locName,))
		except sqlite3.OperationalError as e:
			print(e)
		val = cur.fetchone()
		if int(val[0]) == 1:
			isValid = True
		else:
			locName = input("Invalid Name, please enter a valid location Name: ")
		
	try:
		cur.execute("SELECT locID FROM Location WHERE Name =?", (locName,))
	except sqlite3.OperationalError as e:
		print(e)
	
	locIDList = cur.fetchone()
	locID = locIDList[0] 

	isValid = False
	randomint = random.randrange(100000, 999999)
	revID = "r" + str(randomint)
	while isValid == False: 
		try:
			cur.execute("SELECT COUNT(1) FROM Review WHERE revID =?", (revID,))
		except sqlite3.OperationalError as e:
			print(e)
		val = cur.fetchone()
		if int(val[0]) == 0:
			isValid = True
		else:
			randomint = random.randrange(100000, 999999)
			revID = "r" + str(randomint)

	rating = int(input("Enter rating: "))
	while rating > 5 or rating < 0:
		rating = int(input("Invalid rating, please enter new rating: "))

	revDescription = input("Please add a description: ")

	isValid = False
	revName = input("Enter your user Name: ")
	while isValid == False: 
		try:
			cur.execute("SELECT COUNT(1) FROM User WHERE Name =?", (revName,))
		except sqlite3.OperationalError as e:
			print(e)
		val = cur.fetchone()
		if int(val[0]) == 1:
			isValid = True
		else:
			revName = input("Invalid Name, please enter a valid user Name: ")

	try:
		cur.execute("SELECT userID FROM User WHERE Name =?", (revName,))
	except sqlite3.OperationalError as e:
		print(e)
	
	revIDList = cur.fetchone()
	revUser = revIDList[0] 


	time2 = time.time() + 60
	newtime = time.ctime(time2)
	try:
		cur.execute("INSERT INTO Review (revID, locID, rating ,description, userID, time) VALUES (?,?,?,?,?,?)", (revID, locID, rating, revDescription, revUser, newtime))
	except sqlite3.OperationalError as e:
		print(e)

	connection.commit()
	cur.execute("SELECT * FROM Review WHERE revID = ?", (revID,))
	print("Your Review: "+str(cur.fetchone()))

	updateReview(locID, revID)
   

def addLocation():
	global connection
	global cur
	locName = input("Enter location name: ")
	randomInt = random.randrange(100000,999999)
	locID = "l" + str(randomInt)
	isValid = False
	while isValid == False: 
		try:
			cur.execute("SELECT COUNT(1) FROM Location WHERE locID =?", (locID,))
		except sqlite3.OperationalError as e:
			print(e)
		val = cur.fetchone()
		if int(val[0]) == 0:
			isValid = True
		else:
			randomInt = random.randrange(100000,999999)
			locID = "l" + str(randomInt)

	locAddress = input("Enter location address: ")

	locDesc = input("Enter location description: ")

	try:
		cur.execute("INSERT INTO Location (Name, locID, Address, Description) VALUES (?,?,?,?)", (locName,locID,locAddress,locDesc))
	except sqlite3.OperationalError as e:
		print(e)
	connection.commit()
	cur.execute("SELECT * FROM Location WHERE locID = ?", (locID,))
	print("Your Location: "+str(cur.fetchone()))

def addUser():
	global connection
	global cur
	uName = input("Enter user name: ")
	randomInt = random.randrange(100000,999999)
	uID = "u" + str(randomInt)
	isValid = False
	while isValid == False: 
		try:
			cur.execute("SELECT COUNT(1) FROM User WHERE userID =?", (uID,))
		except sqlite3.OperationalError as e:
			print(e)
		val = cur.fetchone()
		if int(val[0]) == 0:
			isValid = True
		else:
			randomInt = random.randrange(100000,999999)
			uID = "u" + str(randomInt)

	uGender = input("Enter user gender (0 for female, 1 for male): ")
	uAge = int(input("Enter user age: "))

	try:
		cur.execute("INSERT INTO User (Name, userID, Age, Gender) VALUES (?,?,?,?)", (uName,uID,uAge,uGender))
	except sqlite3.OperationalError as e:
		print(e)
	connection.commit()
	cur.execute("SELECT * FROM User WHERE userID = ?", (uID,))
	print("Your User: "+str(cur.fetchone()))


def addUserRating():
	global connection
	global cur
	isValid = False
	userName = input("Enter the user Name: ")
	while isValid == False: 
		try:
			cur.execute("SELECT COUNT(1) FROM User WHERE Name =?", (userName,))
		except sqlite3.OperationalError as e:
			print(e)
		val = cur.fetchone()
		if int(val[0]) == 1:
			isValid = True
		else:
			userName = input("Invalid Name, please enter a valid user Name: ")

	try:
		cur.execute("SELECT userID FROM User WHERE Name =?", (userName,))
	except sqlite3.OperationalError as e:
		print(e)
	
	userIDList = cur.fetchone()
	userID = userIDList[0] 


	isValid = False
	randomInt = random.randrange(100000, 999999)
	ratingID = "ur" + str(randomInt)
	while isValid == False: 
		try:
			cur.execute("SELECT COUNT(1) FROM UserRating WHERE uRatingID =?", (ratingID,))
		except sqlite3.OperationalError as e:
			print(e)
		val = cur.fetchone()
		if int(val[0]) == 0:
			isValid = True
		else:
			randomInt = random.randrange(100000, 999999)
			ratingID = "ur" + str(randomInt)

	rating = int(input("Enter rating: "))
	while rating > 5 or rating < 0:
		rating = int(input("Invalid rating, please enter new rating: "))

	try:
		cur.execute("INSERT INTO UserRating (userID, uRatingID, rating) VALUES (?,?,?)", (userID, ratingID, rating))
	except sqlite3.OperationalError as e:
		print(e)

	connection.commit()
	cur.execute("SELECT * FROM UserRating WHERE uRatingID = ?", (ratingID,))
	print("Your UserRating: "+str(cur.fetchone()))
	updateUser(userID)


#________________________________________________________________DELETE FUNCTIONS_____________________________________________________________________________________________________
def Delete_review():
   global connection
   global cur   
   
   revID = input("Please enter the review ID to delete: ")
   Delete_review_query = "DELETE FROM Review WHERE revID = ?"
   cur.execute(Delete_review_query, (revID,))  
   connection.commit()



def Delete_user():
   global connection
   global cur
   
   userID = input("Please enter the user ID to delete: ")
   Delete_user_query = "DELETE FROM User WHERE userID = ?"
   cur.execute(Delete_user_query, (userID,))
   connection.commit()

def Delete_location():
   global connection
   global cur
   
   locID = input("Please enter the location ID delete: ")
   Delete_loc_query = "DELETE FROM Location WHERE locID = ?"
   cur.execute(Delete_loc_query, (locID,))
   connection.commit()

#_______________________________________UPDATE FUNCTIONS_______________________________________________________________________________
def updateUserName():

    try:
        cur.execute("SELECT * FROM User")
    except sqlite3.OperationalError as e:
        print(e)
    
    userID = input("Enter userID: ")
    Name = input("Enter Name: ")
    
    query = "UPDATE User SET Name = '"+Name+"'""WHERE userID = '"+str(userID)+"'"
    cur.execute(query)
    connection.commit()
    
    
def updateUserFollowers():

    try:
        cur.execute("SELECT * FROM User")
    except sqlite3.OperationalError as e:
        print(e)

    userID = input("Enter userID: ")
    Followers = int(input("Enter Followers: "))
    
    query = "UPDATE User "\
            "SET Followers = '"+str(Followers)+"'"\
                "WHERE userID = '"+str(userID)+"'"
    cur.execute(query)
    connection.commit()
    
    
    
    
def updateReviewDesc():

    try:
        cur.execute("SELECT * FROM Review")
    except sqlite3.OperationalError as e:
        print(e)
    
    revID = input("Enter revID: ")
    Description = input("Enter Description: ")
    
    query = "UPDATE Review "\
            "SET Description = '"+Description+"'"\
                "WHERE revID = '"+str(revID)+"'"
    cur.execute(query)
    connection.commit()
    
    
    
def updateReviewTime():

    try:
        cur.execute("SELECT * FROM Review")
    except sqlite3.OperationalError as e:
        print(e)
    
    revID = input("Enter revID: ")
    Time = input("Enter Time: ")
    
    query = "UPDATE Review "\
            "SET Time = '"+Time+"'"\
                "WHERE revID = '"+str(revID)+"'"
    cur.execute(query)
    connection.commit()
    
   
def updateUserRating():
	try:
		cur.execute("SELECT * FROM User")
	except sqlite3.OperationalError as e:
		print(e)
	userID = input("Enter userID: ")
	UserRating = input("Enter UserRating: ")
	query = "UPDATE User "\
			"SET UserRating = '"+UserRating+"'"\
				"WHERE userID = '"+str(userID)+"'"
	cur.execute(query)
	query2 = "UPDATE UserRating "\
			"SET rating = '"+UserRating+"'"\
				"WHERE userID = '"+str(userID)+"'"
	cur.execute(query2)
	connection.commit()


    
   
def updateLocationName():

    try:
        cur.execute("SELECT * FROM Location")
    except sqlite3.OperationalError as e:
        print(e)
    
    locID = input("Enter locID: ")
    Name = input("Enter Name: ")
    
    query = "UPDATE Location "\
            "SET Name = '"+Name+"'"\
                    "WHERE locID = '"+str(locID)+"'"
    cur.execute(query)
    connection.commit()
    
    
def updateLocationAddress():

    try:
        cur.execute("SELECT * FROM Location")
    except sqlite3.OperationalError as e:
        print(e)
    
    locID = input("Enter locID: ")
    Address = input("Enter Address: ")
    
    query = "UPDATE Location "\
            "SET Address = '"+Address+"'"\
                "WHERE locID = '"+str(locID)+"'"
    cur.execute(query)
    connection.commit()
    
    
    
def updateLocationDesc():

    try:
        cur.execute("SELECT * FROM Location")
    except sqlite3.OperationalError as e:
        print(e)
    
    locID = input("Enter locID: ")

    Description = input("Enter Description: ")
    
    query = "UPDATE Location "\
            "SET Description = '"+Description+"'"\
                    "WHERE locID = '"+str(locID)+"'"
    cur.execute(query)
    connection.commit()
    
   
   
def updateLocationVisitorAmount():

    try:
        cur.execute("SELECT * FROM Location")
    except sqlite3.OperationalError as e:
        print(e)
    
    locID = input("Enter locID: ")
    VisitorAmount = input("Enter Visitor Amount: ")
    
    query = "UPDATE Location "\
            "SET VisitorAmount = '"+str(VisitorAmount)+"'"\
                "WHERE locID = '"+str(locID)+"'"
    cur.execute(query)
    connection.commit()
    
#_________________________________________________________Automatic Updates___________________________________________________________

def updateReview(locID, revID):
	updateLocationAverageReviews(locID)
	good_bad_reviews_update(locID, revID) 


def updateUser(userID):
	try:
		cur.execute("SELECT AVG(rating) FROM UserRating WHERE userID = ?", (str(userID),))
	except sqlite3.OperationalError as e:
		print(e)
	value = cur.fetchone()
	query2 = "UPDATE User SET UserRating = '"+str(value[0])+"'""WHERE userID = '"+str(userID)+"'"
	cur.execute(query2)
	connection.commit()

def good_bad_reviews_update(locID, revID):
	global connection
	global cur
	query = "SELECT Rating FROM  Review WHERE revID = '"+str(revID)+"'"
	cur.execute(query)
	value = cur.fetchone()
	if value[0] >= 2.5:
		query1 = "SELECT GoodReviews FROM Location WHERE locID = '"+str(locID)+"'"
		cur.execute(query1)
		GoodReview = cur.fetchone()
		rev = GoodReview[0] + 1
		Update_query = "UPDATE Location SET GoodReviews = '"+str(rev) +"' WHERE locID = '"+str(locID)+"'"
		cur.execute(Update_query)
		connection.commit()
	else:
		query1 = "SELECT BadReviews FROM Location WHERE locID = '"+str(locID)+"'"
		cur.execute(query1)
		BadReview = cur.fetchone()
		rev = BadReview[0] + 1
		Update_query = "UPDATE Location SET BadReviews = '"+ str(rev) +"' WHERE locID = '"+str(locID)+"'"
		cur.execute(Update_query)
		connection.commit()      

def delete_good_bad_reviews_update(locID, revID):
	global connection
	global cur
	query = "SELECT Rating FROM  Review WHERE revID = '"+str(revID)+"'"
	cur.execute(query)
	value = cur.fetchone()
	if value[0] >= 2.5:
		query1 = "SELECT GoodReviews FROM Location WHERE locID = '"+str(locID)+"'"
		cur.execute(query1)
		GoodReview = cur.fetchone()
		rev = GoodReview[0] - 1
		Update_query = "UPDATE Location SET GoodReviews = '"+str(rev) +"' WHERE locID = '"+str(locID)+"'"
		cur.execute(Update_query)
		connection.commit()
	else:
		query1 = "SELECT BadReviews FROM Location WHERE locID = '"+str(locID)+"'"
		cur.execute(query1)
		BadReview = cur.fetchone()
		rev = BadReview[0] - 1
		Update_query = "UPDATE Location SET BadReviews = '"+ str(rev) +"' WHERE locID = '"+str(locID)+"'"
		cur.execute(Update_query)
		connection.commit()      

def updateLocationAverageReviews(locID):

    try:
        cur.execute("SELECT * FROM Location")
    except sqlite3.OperationalError as e:
        print(e)
    
    query = "SELECT AVG(Rating) FROM Review "\
                "WHERE locID = '"+str(locID)+"'"
    cur.execute(query)
    
    value = cur.fetchone()

   
    query2 = "UPDATE Location SET AverageReviews = '"+str(value[0])+"'"\
                    "WHERE locID = '"+str(locID)+"'"
    cur.execute(query2)
    connection.commit()
    
#_____________________________________________________________VIEW FUNCTIONS_______________________________________________________________
def viewUsers():
    try:
        cur.execute("SELECT * FROM User")
    except sqlite3.OperationalError as e:
        print(e)
        
    names = cur.description
    
    for name in names:
        print("{: <20}".format(name[0]), end="")
    print()
    
    for row in cur.fetchmany(40):
        for item in row:
            if item != None:
                print("{: <20}".format(item), end="")
            else:
                print("{: <20}".format("None"), end="")
        print()
    print()
   
def viewLocations():
    try:
        cur.execute("SELECT * FROM Location")
    except sqlite3.OperationalError as e:
        print(e)
        
    names = cur.description
    
    for name in names:
        print("{: <30}".format(name[0]), end="")
    print()
    
    for row in cur.fetchmany(14):
        for item in row:
            if item != None:
                print("{: <30}".format(item), end="")
            else:
                print("{: <30}".format("None"), end="")
        print()
    print()
    
def viewReviews():
    try:
        cur.execute("SELECT * FROM Review")
    except sqlite3.OperationalError as e:
        print(e)
        
    names = cur.description
    
    for name in names:
        print("{: <40}".format(name[0]), end="")
    print()
    
    for row in cur.fetchmany(14):
        for item in row:
            if item != None:
                print("{: <40}".format(item), end="")
            else:
                print("{: <40}".format("None"), end="")
        print()
    print()
    
def viewUserRating():
    try:
        cur.execute("SELECT * FROM UserRating")
    except sqlite3.OperationalError as e:
        print(e)
        
    names = cur.description
    
    for name in names:
        print("{: <20}".format(name[0]), end="")
    print()
    
    for row in cur.fetchmany(14):
        for item in row:
            if item != None:
                print("{: <20}".format(item), end="")
            else:
                print("{: <20}".format("None"), end="")
        print()
    print()


#_______________________________________________________________________________________________________________________________________
def googleMap():
	global connection
	global cur
	url = "https://www.google.com/maps/dir/?api=1&destination="
	locName = input("Enter the name of the location:")
	query = "SELECT Address FROM Location WHERE Name =?"

	try:
		cur.execute(query, (locName,))
	except sqlite3.OperationalError as e:
		print(e)
	address = cur.fetchone()
	address[0].replace(" ", "+")
	address[0].replace(",", "%C2")
	webbrowser.open(url+address[0])
  
main()
