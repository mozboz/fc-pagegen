<?php

/*
 * I <3 PHP. No, really.
 *
 * This calls a python script, and echos out stdout and stderror.
 */

if ($_GET['recompile'] == 'go') {
    exec("python " . __DIR__ . "/rundmc.py 2>&1", $out, $status);
    print_r($out);
    print_r($status);
    echo "<br>recompiled";
} else {
    echo "nope";
}

?>