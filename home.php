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
			/* Start of Accordion*/
			echo "<button class='accordion'>Get Specific TCR</button>
				<div class='panel'>";
					$query = "SELECT pdbID_raw FROM rawPDB";
					$result = mysqli_query($connect, $query);
					echo "<br>";
					echo '<form>';
						echo '<label for="filename"> Select PDB id: </label>';
						echo "<select name='filename' id='pdbid_raw'>";
						while($row = mysqli_fetch_row($result)) {
							echo "<option value='/~aseamann/rawPDBs/".$row[0].".pdb'>".$row[0]."</option>";
						}
						echo "</select> ";
						echo '<input type="button"',
							' onclick="window.location.href=document.getElementById(\'pdbid_raw\').value"',
						      	' value="Download" class="grey-btn">';
					echo "</form>";
					echo '<br>';
			echo "</div>
				<button class='accordion'>All TCRs</button>
				<div class='panel'>";
					echo '<br>';
					// Python program that creates a compressed file of all PDBs in rawPDB
					// Returns a location of a compress file that's in /~aseamann/rawPDBs/
					$compress_run = exec("python3 /home/aseamann/public_html/python_help/compress.py");	
					echo '<input type="button"',
					       ' onclick="window.location.href=\''.$compress_run.'\'"',
					       ' value="Download" class="grey-btn">';
					echo '<br><br>';		
			echo "</div>

				<button class='accordion'>Advanced TCR with Modifications</button>
				<div class='panel'>";
					echo '<br>';
					echo "<form>";
						echo '<input type="checkbox" id="all"> All PDBs | ';
						echo '<label for="resolution">Min. Resolution Cutoff: </label>';
						echo '<input type="text" id="resolution" name="resolution" size="4"><br>';
						echo '<input type="checkbox" id="label" value="--relabel"> Relabel ';
						echo '<input type="checkbox" id="renumber" value="--renum"> Renumber ';
						echo '<input type="checkbox" id="trim" value="--trim"> Trim TCR ';
						echo '<input type="checkbox" id="tcronly" value="--tcr"> TCR Only ';
						echo '<br><br><input type="button" value="Download" class="grey-btn">';
					echo "</form>";
					echo '<br>';	
				echo "</div>";
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
					function download(d) {
						if (d =='PDB') return ;
						window.location = 'http://odin.unomaha.edu/~aseamann/' + d;
					}
				</script>";
		}
		
		/*Always close your connection. 
		 * Its a courtesy to your fellow users.
		 */
		mysqli_close($connect);
		?>
	</body>
</html>

