<?php
$server="localhost";
$username="aseamann";
$password="";
$database="aseamann";

/*Connect to my database*/
$connect = mysqli_connect($server,$username,"",$database);

if($connect->connect_error){
		echo "Something has gone terribly wrong";
		echo "Connection error:" .$connect->connect-error;
}else{
		echo "<p>Hellow World, How Are You Today?</p>;
}

$query = "SELECT pdbID_raw FROM rawPDB";
$result = mysqli_query($connect, $query)
	or trigger_error("Query Failed! SQL: $query - Error: "
	. mysqli_error($connect), E_USER_ERROR);
echo "Query is: $query <br>";

if ($result = mysqli_query($connect, $query)) {
	while ($row = mysqli_fetch_row($results)) {
		printf("<br>%s", $row[0]);
	}
	mysqli_free_results($results);
}else{
	echo "That did not work";
}
mysqli_close($connect);
?>

