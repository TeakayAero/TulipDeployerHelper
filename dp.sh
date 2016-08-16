#!/bin/bash
branch=${4:-master}
status=${5:-progress}

read -p "type a message >" message
message=${message// /*__*}
if [ -z $message ]; then
    message="&empty^_flag$"
fi

gitName=$(git config user.name)
fn=$(echo "$gitName" | { read first _ ; echo $first ; })

pyreturn="Init pyreturn variable"
if [ $branch = "master" ]; then
    pyreturn=$(python messageController.py $1 $2 $3 $branch $fn $message)
else
    pyreturn=$(python messageController.py $1 $2 $3 $branch $fn $status $message)
fi
if ! [ $status = "done" ]; then
	echo "$pyreturn"
	bundle=$(which bundle)
	msg="cap $1:$2 deploy -S branch=origin/$branch"
	if [ -n bundle ]; then
	    cmd="bundle exec $msg"
	fi
	cd ~/workspace/deployer && eval $cmd
fi

