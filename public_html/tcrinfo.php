<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" name="viewpoint" content="width=device-width, initial-scale=1">
		<title>YourTCR</title>
		<style>
			table {
				font-family: arial, sans-serif;
				border-collapse: collapse;
				width: 80%;
				margin: 0 auto;
			}
			td, th {
				border: 1px solid #dddddd;
				text-align: middle;
				padding: 8px;
			}
			tr:nth-child(even) {
				background-color: #dddddd;
			}
			header {
				background: #E0823cc;
			}
			nav ul {
				list-stype: none;
			}
			nav li {
				display: inline-block;
				margin-left: 70px;
			}
			nav a {
				color: #444;
				text-decoration: none;
				text-transform: uppercase;
			}
			nav a:hover {
				color: #000;
			}
		</style>
	</head>
	<body>
		<?php
		// Connect to database
		$server="localhost";
		$username="aseamann";
		$password="";
		$database="aseamann";

		$connect = mysqli_connect($server,$username,"",$database);

		// Sets up body of page
		if($connect->connect_error){
			echo "Something has gone terribly wrong";
			echo "Connection error:" .$connect->connect_error;
		}else{
			// Header
			echo "<header>";
				echo "<div class='container'>";
				echo "<h1>YourTCR</h1>;";
				echo "<nav>";
					echo "<ul>";
						echo "<li><a href='home.php'>Home</a></li>";
						echo "<li>TCR Info<li>";
					echo "</ul>";
				echo "</nav>";
			echo "</header>";
			// Default query
			$query = "SELECT pdbID_raw, resolution, tcr_alpha, tcr_beta, peptide, mhc FROM rawPDB";
			$result = mysqli_query($connect, $query);
			echo "<br>";
			// Creates header of table
			echo "<table>";
				echo "<tr>";
					echo "<th>PDB id</th>";
					echo "<th>Resolution</th>";
					echo "<th>Alpha</th>";
					echo "<th>Beta</th>";
					echo "<th>Peptide</th>";
					echo "<th>MHC</th>";
			// Inserts each row of the table based on query
			while($row =mysqli_fetch_row($result)) {
				echo "<tr>";
					echo "<th>".$row[0]."</th>";
					echo "<th>".$row[1]."</th>";
					echo "<th>".$row[2]."</th>";
					echo "<th>".$row[3]."</th>";
					echo "<th>".$row[4]."</th>";
					echo "<th>".$row[5]."</th>";
				echo "</tr>";
			echo "</table>";
		mysqli_close($connect);
		?>
	</body>
</html>

