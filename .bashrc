#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='exa --icons -a'
PS1='[\u@\h \W]\$ '

# nnn
export NNN_PLUG='p:preview-tui'

exec fish
