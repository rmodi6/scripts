alias ll="exa -lha --git"
alias ..="cd .."
alias colc="column -s, -t"
alias colt="column -s\t -t"
#alias oneplus6t="-p 8022 192.168.1.125"

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

# . /home/rmodi/torch/install/bin/torch-activate

function ssh_oneplus6t
	ssh -p 8022 192.168.1.125
end
