#!/bin/bash
set -e  # stop on first error
LOG="$HOME/git/My-Peeps/autostart/auto-cibo.log"
exec > >(tee -a "$LOG") 2>&1

tmux new -d -s peeps_backend || true # wont stop if tmux session notif already exists
tmux send-keys -t cibo "cd ~"  C-m
tmux send-keys -t cibo "source venv_api/bin/activate"  C-m
tmux send-keys -t cibo "cd ~/git/My-Peeps/backend" C-m
tmux send-keys -t cibo "python3 main.py" C-m
