echo "This is the first shell script!"
@ y = 1;
@ x = $y + 1
@ x = ( 0644 & 022 ) + 1; echo $x
@ x = ( ~ 077 );          echo $x
@ x = ( ~ 077 | 022 );    echo $x
@ x = ( ! 0 );            echo $x