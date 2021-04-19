<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" name="viewpoint" content="width=device-width, initial-scale=1">
		<title>YourTCR</title>
		<style>
		/* Style the buttons that are used to open and close the accordion panel */
		.accordion {
			background-color: #eee;
			color: #444;
			cursor: pointer;
			padding: 18px;
			width: 100%;
			text-align: left;
			border: none;
			outline: none;
			transition: 0.4s;
		}

		/* Add a background color to the button if it is clicked on (add the .active class with JS), and when you move the mouse over it (hover) */
		.active, .accordion:hover {
			background-color: #ccc;
		}

		/* Style the accordion panel. Note: hidden by default */
		.panel {
			padding: 0 18px;
			background-color: white;
			display: none;
			overflow: hidden;
		}
		</style>
	</head>
	<body>
		<?php
		/* Connect to database */
		$server="localhost";
		$username="aseamann";
		$password="";
		$database="aseamann";
		
		$connect = mysqli_connect($server,$username,"",$database);

		/* Sets up body of page */
		if($connect->connect_error){
			echo "Something has gone terribly wrong";
			echo "Connection error:" .$connect->connect_error;
		}else{
			echo "<h1>YourTCR</h1>";
			echo "<form>";
			echo "<label for='resolution'>Min. Resolution: </label>";
			echo "<input type='text' id='resolution' name='resolution' size='4'> ";
			echo "<input type='submit' value='Submit'>";
			echo "</form>";
			echo "<button class='accordion'>Section 1</button>
				<div class='panel'>
					<p>Lorem ipsum...</p>
				</div>

				<button class='accordion'>Section 2</button>
				<div class='panel'>
					<p>Lorem ipsum...</p>
				</div>

				<button class='accordion'>Section 3</button>
				<div class='panel'>
					<p>Lorem ipsum...</p>
				</div>";
			echo "<script>
					var acc = document.getElementsByClassName('accordion');
					var i;

					for (i = 0; i < acc.length; i++) {
						acc[i].addEventListener('click', function() {
							this.classList.toggle('active');
							var panel = this.nextElementSibling;
							if (panel.style.display === 'block') {
								panel.style.display = 'none';
							} else {
							panel.style.display = 'block';
							}
						});
					}
				</script>";
		
		/* Run a basic SQL query and throw
		 * an error if its unable to perform the query
		 */
		$query = "SELECT pdbID_raw FROM rawPDB";
		$result = mysqli_query($connect, $query) 
			  or trigger_error("Query Failed! SQL: $query - Error: "
			  . mysqli_error($connect), E_USER_ERROR);
		if($result = mysqli_query($connect, $query)){
			$select= '<select name="select" id=pdbid_raw>';
			while($row = mysql_fetch_row($result)){
				echo $row[0];
				$select.='<option value="'.$row[0].'">'.$row[0].'</option>';
			}
		}
		$select.='</select>';
		echo $select;
		
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

