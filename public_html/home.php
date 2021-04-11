<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>YourTCR</title>
		<style type="text/css">
	</head>
	<body>
		<?php
			$server="localhost";
			$username="aseamann";
			$password="";
			$database="aseamann";
			
			$connect = mysqli_connect($server,$username,"",$database);
		
			if($connect->connect_error){
				echo "Something has gone terribly wrong";
				echo "Connection error:" .$connect->connect_error;
			}else{
				echo "<h1>YourTCR</h1>";
			}

			$rawPDB = "SELECT rawPDB FROM rawPDB";
			$result = mysql_query($rawPDB);

			echo "<select name='rawPDB'>";
			while ($row = mysql_fetch_array($result)) {
				echo "<option value='" . $row['rawPDB'] . "'>" . $row['rawPDB'] . "</options>";
			}
			echo "</select>";
			
			/* Run a basic SQL query and throw
			 * an error if its unable to perform the query
			 */
			$query = "SELECT pdbID_raw FROM rawPDB";
			$result = mysqli_query($connect, $query) 
				or trigger_error("Query Failed! SQL: $query - Error: "
				. mysqli_error($connect), E_USER_ERROR);
			echo "Query is: $query <br>";
			
			/*Return file of PDB selected else print error*/
			if ($result = mysqli_query($connect, $query)) {
		    	while ($row = mysqli_fetch_row($result)) {
				printf("<br>%s<br>", $row[0]);
				printf('<p><a href="rawPDBs/%s.pdb" download>Here</a></p>', $row[0]);
		    	}
		    	mysqli_free_result($result);
			}else{
				echo "No results";
			}
			
			/*Always close your connection. 
			 * Its a courtesy to your fellow users.
			 */
			mysqli_close($connect);
		?>
	</body>
</html>

