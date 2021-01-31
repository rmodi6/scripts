alias ll="exa -lha --git"
alias ..="cd .."
alias colc="column -s, -t"
alias colt="column -s\t -t"

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
# export CUDADIR=/usr/local/cuda-10.0
# set -U fish_user_paths /usr/local/cuda-10.0/bin/ $fish_user_paths
set -U fish_user_paths /home/rmodi/.cargo/bin/ $fish_user_paths

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
eval /home/rmodi/anaconda3/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<

function hibernate
	sudo systemctl hibernate
end

function logout
	loginctl lock-session
end

# . /home/rmodi/torch/install/bin/torch-activate

function ssh_oneplus6t
	set IP (ip n | grep -i 'MAC_ADDRESS' | awk '{print $1}')
	ssh -p 8022 $IP
end
