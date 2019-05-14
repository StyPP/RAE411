#variables
tmp=$(($1+1))
light_red='\e[1;91m%s\e[0m\n'
light_green='\e[1;92m%s\e[0m\n'

#executes command
ping=`ping -c $1 $2`
rp=`echo $ping | grep "PING"`
rpp=$?

newping=`echo "$ping" | head -n $tmp | tail -n $1`

if [ $rpp -eq 0 ];
then
    #cuts the result
    time=`echo "$newping" | cut -d = -f 4 | cut -d ' ' -f 1`
    number=`echo "$newping" | cut -d = -f 2 | cut -d ' ' -f 1 | tail -n 1`

    #computes percentage
    percentage=$(($1/$number*100))

    #computes average
    average=0

    for t in $time
    do
        average=`bc <<< $average+$t`
    done
    
    average=$(echo "scale=2; $average/$1" | bc -l)
    
    #computes the standard derivation
    tmp2=0
    tmp3=0
    tmp4=0

    for t in $time
    do
        tmp2=`bc <<< $t-$average`
        tmp3=$(echo "$tmp2*$tmp2" | bc -l)
        tmp4=`bc <<< $tmp4+$tmp3`
    done

    tmp5=$(echo "scale=2; 1/$1" | bc -l)
    tmp6=$(echo "scale=2; $tmp5*$tmp4" | bc -l)
    sdev=$(echo "scale=2; sqrt($tmp6)" | bc -l)

    #defines max and min
    time=`for i in $time
    do
        echo $i
    done | sort -nu`
    

    max=`echo $time | cut -d ' ' -f $1`
    min=`echo $time | cut -d ' ' -f 1`

    #prints results
    echo "$newping"
    echo -----------------------------------------
    printf "$light_green" "$2 is AVAILABLE"
    echo There are $percentage% of paquets received.
    echo This ping takes $average ms on average.
    echo The minimum time of the ping is: $min ms.
    echo The maximum time of the ping is: $max ms.
    echo The standard derivation is: $sdev ms.

else
    printf "$light_red" "$2 is NOT AVAILABLE"
fi
