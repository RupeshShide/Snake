#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import random

def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()

    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(1)
    win.timeout(120)

    # initial snake
    snk_x = sw // 4
    snk_y = sh // 2

    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    # food
    food = [sh // 2, sw // 2]
    win.addch(food[0], food[1], '*')

    key = ord('6')  # default → right
    score = 0

    while True:
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        # exit
        if key == ord('0'):
            break

        # game over conditions
        if (snake[0][0] in [0, sh] or
            snake[0][1] in [0, sw] or
            snake[0] in snake[1:]):
            break

        new_head = [snake[0][0], snake[0][1]]

        # 🎮 NUMBER CONTROLS
        if key == ord('2'):   # UP
            new_head[0] -= 1
        elif key == ord('8'): # DOWN
            new_head[0] += 1
        elif key == ord('4'): # LEFT
            new_head[1] -= 1
        elif key == ord('6'): # RIGHT
            new_head[1] += 1

        snake.insert(0, new_head)

        # food logic
        if snake[0] == food:
            score += 1
            food = None

            while food is None:
                nf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = nf if nf not in snake else None

            win.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.addch(snake[0][0], snake[0][1], '#')

        # UI
        stdscr.addstr(0, 2, f"Score: {score}  Controls: 2↑ 8↓ 4← 6→ 0=Exit ")

    stdscr.addstr(sh//2, sw//2 - 5, "GAME OVER")
    stdscr.refresh()
    stdscr.getch()

# run
curses.wrapper(main)
