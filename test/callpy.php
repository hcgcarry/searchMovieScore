<?php
function callpy() {

	$jsondata= exec("/usr/bin/python test.py fuck");
   return $jsondata ;
   }

	$jsondata= callpy();
    echo $jsondata ;
    $obj = json_decode($jsondata)  ; 
    echo "fuck:".$obj-> { 'fuck'} .',' ;
    echo "carry:".$obj-> { 'carry'}  ;
?>
