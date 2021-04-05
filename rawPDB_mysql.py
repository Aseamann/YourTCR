import MySQLdb
import sys

# Connecting python to mysql
try:
    conn = MySQLdb.connect(
            user="aseamann",
            password="",
            host="localhost",
            port=3306)
except MySQLdb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Instantiate Cursor
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


