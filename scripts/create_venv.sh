#!/bin/bash
python -m venv .venv
source .venv/bin/activate 2>/dev/null || source .venv/Scripts/activate 2>/dev/null
python -m pip install --upgrade pip
pip install -r requirements.txt