# minesweeper_clips

## Config
```
{board_size}
{total_bomb}
{bomb_coordinate}
```
Example
```
10
8
0, 6
2, 2
2, 4
3, 3
4, 2
5, 6
6, 2
7, 8
```

## How to Run

1. Install dependencies
```
pip install -r requirements.txt
```
2. Run
```
python main.py
```

## Note
if you got this error:
```ModuleNotFoundError: No module named 'Tkinter'```<br/>
You might need to install for your specific version, because a virtualenv in python 3.7 may not importing tkinter. You would have to install it for that version specifically.
```sudo apt-get install python3-tk```