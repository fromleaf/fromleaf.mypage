# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

##################
### MY ALIASES ###
##################

# Set Alias
## Colorize the grep command output for ease of use (good for log files)##
#   ------------------------------------------------------------
export GREP_OPTIONS='--color=auto'
#export GREP_COLOR='1;30;40'
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias ls='ls -vlGF'
alias lsd='ls -l | grep "^d" --color=auto'
alias l='ls -aGF'
alias ll='ls -aGF'
alias mv='mv -i'
alias rm='rm -i'
alias cp='cp -i'
alias cd1='cd ../'
alias cd2='cd ../../'
alias cd3='cd ../../../'

# temporally alias
alias p='python'
alias p3='python3'
alias manage='python3 manage.py'


# refresh shell
alias reload='source ~/.profile'

# tomcat command
alias tomcat='$TOMCATPATH/catalina'

# connect mypage-fromleaf in aws-elasticbeans
alias aws.connect='ssh -i "/Users/heoyun/Workspace/aws_privatekey/aws_private_key.pem"
ec2-user@ec2-52-78-11-93.ap-northeast-2.compute.amazonaws.com'
