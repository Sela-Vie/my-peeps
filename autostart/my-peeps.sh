#!/bin/bash
set -e  # stop on first error
LOG="$HOME/git/my-peeps/autostart/peeps_backend.log"
exec > >(tee -a "$LOG") 2>&1

tmux new -d -s peeps_backend || true # wont stop if tmux session notif already exists
tmux send-keys -t peeps_backend "cd ~"  C-m
tmux send-keys -t peeps_backend "source venv_api/bin/activate"  C-m
tmux send-keys -t peeps_backend "cd ~/git/my-peeps/backend" C-m
tmux send-keys -t peeps_backend "python3 main.py" C-m
