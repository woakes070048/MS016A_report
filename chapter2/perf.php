<?php
    $rounds = $_GET['rounds'];
    $sleep = $_GET['sleep'];
    $random = $rounds * rand(1,10);
    echo "Rounds $random";
    sleep($sleep);

?>
