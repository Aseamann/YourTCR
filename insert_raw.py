import mysql.connector

# Source: https://www.tutorialspoint.com/python_data_access/python_mysql_insert_data.htm

# Connecting python to mysql
conn = mysql.connector.connect(
	user='austinseamann', password='Pandabear57', host='Austins-MacBook-Pro.local', database='aseamann')

# Creating a curson object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query for inserting raw PDB info
insert_stmt = (
	"INSERT INTO rawPDB( pdbID_raw, resolution, tcr_alpha, tcr_beta, peptide, mhc)"
	"VALUES (%s, %s, %s, %s, %s, $s)"
)

data = ('1a07', 3.0, 'D', 'E', 'C', 'A')

try:
	#Excuting the SQL command
	cursor.execute(insert_stmt, data)

	#Commit your changes in the database
	conn.commit()
except:
	# Rolling back in case of error
	conn.rollback()

print("Data inserted")

# Closing the connection
conn.close()


