#!/bin/bash

read -p "what's your age: " age

if [[ $age -gt 20 ]] && [[ $age -lt 100 ]]
then 
    echo "Good, You are a Major" 
    
elif [[ $age -lt 20 ]] &&  [[ $age -gt 0 ]]
then
    echo "Nah, You are a Minor"

else 
    echo "You are animal"
fi




function exec(){
    local params=$1
    echo "Inside Exec function:  $params" 
    return
}

exec "hi"