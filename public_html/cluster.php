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
			.container {
				width: 80%;
				margin: 0 auto;
			}
			header {
				background: #55d6aa;
			}
			header::after {
				content: '';
				display: table;
				clear: both;
			}
			.logo {
				float: left;
				margin: 0;
				padding: 10px 0;
			}
			nav {
				float: right;
			}
			nav ul {
				margin: 0;
				padding: 0;
				list-style: none;
			}
			nav li {
				display: inline-block;
				margin-left: 40px;
				padding-top: 25px;

				position: relative;
			}
			nav a {
				color: #444;
				text-decoration: none;
				text-transform: uppercase;
			}
			nav a:hover {
				color: #000;
			}
			nav a::before {
				content: '';
				display: block;
				height: 5px;
				width: 100%;
				background-color: #444;
				position: absolute;
				top: 0;
				width: 0%;
			}
			nav a:hover::before {
				width: 100%;
			}
			body {
				text-align: center;
			}
			form {
				display: inline-block;
			}
		</style>
	</head>
	<body>
		<header>
			<div class='container'>
			<h1 alt='logo' class='logo'>YourTCR</h1>
			<nav>
				<ul>
					<li><a href='home.php'>Home</a></li>
					<li><a href='tcrinfo.php'>TCR Info</a></li>
					<li><a>Clusters</a></li>
				</ul>
			</nav>
		</header><br>
		<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
			Percent Similiarity: <select name='percent' id='percent'>
				<option value=99>99</option>
				<option value=90>90</option>
				<option value=80>80</option>
				<option value=70>70</option>
			</select>
			<input type="submit">
		</form><br>
		<?php
		$percent = 99;  // Default percent
		if ($_SERVER["REQUEST_METHOD"] == "POST") {
			$percent = $_POST['percent'];
		}
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
			// Default query
			$query = "SELECT percentID, clust, pdbID FROM clustered WHERE percentID=".$percent;
			$result = mysqli_query($connect, $query);
			echo "<br>";
			// Creates header of table
			echo "<table>";
				echo "<tr>";
					echo "<th>Percent Similarity</th>";
					echo "<th>Cluster #</th>";
					echo "<th>PDB id</th>";
			// Inserts each row of the table based on query
			while($row =mysqli_fetch_row($result)) {
				echo "<tr>";
					echo "<th>".$row[0]."</th>";
					echo "<th>".$row[1]."</th>";
					echo "<th>".$row[2]."</th>";
				echo "</tr>";
			}
			echo "</table>";
		}
		mysqli_close($connect);
		?>
	</body>
</html>

