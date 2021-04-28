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
		.container {
			width: 80%;
			margin: 0 auto;
		}
		header {
			background: #E0823cc;
		}
		nav ul {
			list-style: none;
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
			// Start of header
			echo "<header>";
				echo "<div class='container'>";
				echo "<h1>YourTCR</h1>";
				echo "<nav>";
					echo "<ul>";
						echo "<li>Home</li>";
						echo "<li><a href='tcrinfo.php'>TCR Info</a></li>";
					echo "</ul>";
				echo "</nav>";
			echo "</header>";
			/* Start of Accordion*/
			echo "<button class='accordion'>Get Specific TCR</button>
				<div class='panel'>";
					// Accordion Panel 1
					$query = "SELECT pdbID_raw FROM rawPDB";
					$result = mysqli_query($connect, $query);
					echo "<br>";
					echo '<form>';
						// Dropdown menu
						echo '<label for="filename"> Select PDB id: </label>';
						echo "<select name='filename' id='pdbid_raw'>";
						while($row = mysqli_fetch_row($result)) {
							echo "<option value='/~aseamann/rawPDBs/".$row[0].".pdb'>".$row[0]."</option>";
						}
						echo "</select> ";
						// Download Button
						echo '<input type="button"',
							' onclick="window.location.href=document.getElementById(\'pdbid_raw\').value"',
						      	' value="Download" class="grey-btn">';
					echo "</form>";
					echo '<br>';
			echo "</div>
				<button class='accordion'>All TCRs</button>
				<div class='panel'>";
					// Accordion Panel 2
					echo '<br>';
					// Python program that creates a compressed file of all PDBs in rawPDB
					// Returns a location of a compress file that's in /~aseamann/rawPDBs/
					// NOT USED CURRENTLY, CAN MAKE COMPRESSION ADAPTIVE BUT TAKES LONG ON PAGE LOAD TIME
					// $compress_run = exec("python3 /home/aseamann/public_html/python_help/compress.py");	
					$compress_run = "/~aseamann/rawPDBs.tar.gz";
					echo '<input type="button" id="ALL_TCRs"',
					       	' onclick="window.location.href=\''.$compress_run.'\'"',
					       	' value="Download" class="grey-btn">';
					echo '<br><br>';		
			echo "</div>

				<button class='accordion'>Advanced TCR with Modifications</button>
				<div class='panel'>";
					// Accordion Panel 3
					echo '<br>';
					echo "<form method='post' id='advance'i action =''>";
						$query = "SELECT pdbID_raw FROM rawPDB";
						$result = mysqli_query($connect, $query);
						echo '<label for="modname"> Select PDB id: </label>';
						echo '<select name="modname" id="pdbid_mod">';
						while($row = mysqli_fetch_row($result)) {
							echo "<option value='".$row[0]."'>".$row[0]."</option>";
						}
						echo "</select><br>";
						// Start of options
						// Value = parameter for run_mod.py
						echo '<input type="checkbox" id="renum" value="--renum"> Renumber <br>';
						echo '<input type="radio" id="all_chains" value="" name="run"> All Chains ';
						echo '<input type="radio" id="trimmed" value="--trim" name="run"> Trimmed TCR Only ';
						echo '<input type="radio" id="tcr_only" value="--tcr_split" name="run"> TCR Only ';
						echo '<input type="radio" id="p_only" value="--peptide_split" name="run"> Peptide Only ';
						echo '<input type="radio" id="m_only" value="--mhc_split" name="run"> MHC Only ';
						echo '<br><br><input type="button" name="download" value="Download" onclick="runMod()" class="grey-btn">';
					echo "</form>";
					echo '<br>';
					// Attempting to capture from Javascript in the form of the cookie
					// My goal however was to do it without refreshing the page as the accordion closes
					echo $_Cookie;
				echo "</div>";
				echo "<script>
					// Accordion script
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
					// Download script
					function download(d) {
						if (d =='PDB') return ;
						window.location = 'http://odin.unomaha.edu/~aseamann/' + d;
					}
					// Script for pulling from Panel 3 form wihtout refreshing the page
					function runMod() {
						// Holds options from form
						var results = [];
						// Holds rawPDB_id selected
						const modname = document.getElementById('pdbid_mod').value;
						console.log(modname);
						// Holds if renum is selected
						const renum = document.querySelector('input[id=\"renum\"]');
						if (renum.checked) {
							console.log(renum.value);
							results.push(renum.value);
						}
						// Updates results and adds the options selected in form to list
						const choices = document.querySelectorAll('input[name=\"run\"]');
						let selectedValue;
						for (const choice of choices) {
							if (choice.checked) {
								if (choice.value != '') {
									selectedValue = choice.value;
									console.log(selectedValue);
									results.push(selectedValue);
									break;
								}
							}
						}
						// Creating statement to send to be exectured
						mod_exec = 'python3 /home/aseamann/public_html/python_help/run_mod.py --rawPDB ' + modname;
						mod_exec += ' --modPDB ' + '0000';
						for (each of results) {
							mod_exec += ' ' + each;
						}
						// Trying to return mod_exec to PHP to run on server
						console.log(mod_exec);
						createCookie(mod_exec);
					}
					// Creates a cookie
					function createCookie(value) {
						document.cookie = escape(value);
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

