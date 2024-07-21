# -*- coding: utf-8 -*-
""" 
@file:      dlc1.py
@time:      2024/7/21 上午12:18
@author:    sMythicalBird
"""
import time
from typing import Dict
from schema import Position
from utils import control, screenshot
from utils.task import task
from re import template
from pydirectinput import (
    press,
    click,
    moveTo,
    mouseDown,
    mouseUp,
    keyDown,
    keyUp,
    scroll,
    moveRel,
)

fflag = 0


# def get_pos(text: str):
#     text = template(text)
#     img = screenshot()  # 截图
#     ocr_Results = task.ocr(img)  # OCR识别
#     # print(ocr_Results)
#     positions = []
#     for ocr_result in ocr_Results:
#         if text.search(ocr_result.text):
#             # print(ocr_result)
#             positions.append(
#                 [
#                     (ocr_result.position[0] + ocr_result.position[2]) / 2,
#                     (ocr_result.position[1] + ocr_result.position[3]) / 2,
#                 ]
#             )
#     return positions


def money_fight():
    moveRel(110, 0, relative=True)
    time.sleep(0.3)
    keyDown("w")
    keyDown("shift")
    time.sleep(0.1)
    mouseDown()
    time.sleep(0.1)
    mouseUp()
    time.sleep(0.1)
    press("space", duration=0.1)


def money_go(t1: float, t2: float, t3: int):
    time.sleep(t1)
    keyDown("d")
    time.sleep(t2)
    keyUp("d")
    for i in range(t3):
        time.sleep(0.1)
        press("f", duration=0.1)
    keyUp("shift")
    keyUp("w")


# 战斗
@task.page(name="战斗中", target_texts=["^Space$"])
def action():
    global fflag
    # 击碎箱子
    money_fight()
    # 交付任务
    money_go(3.2, 0.5, 5)
    fflag = 1
    for i in range(5):
        control.click(1020, 440)
        time.sleep(0.2)
    press("esc", duration=0.1)


# 选择委托
@task.page(name="选择委托", target_texts=["^战斗委托$"])
def action(positions: Dict[str, Position]):
    pos = positions.get("^战斗委托$")
    control.click(pos.x, pos.y)
    time.sleep(0.1)
    control.click(pos.x, pos.y)


# 选择关卡
@task.page(name="选择关卡", target_texts=["真·拿命验收$", "^下一步$"])
def action(positions: Dict[str, Position]):
    time.sleep(0.3)
    pos = positions.get("真·拿命验收$")
    control.click(pos.x, pos.y)
    time.sleep(0.5)
    pos = positions.get("^下一步$")
    control.click(pos.x, pos.y)


@task.page(name="出战", target_texts=["^出战$"])
def action(positions: Dict[str, Position]):
    global fflag
    # time.sleep(0.3)
    pos = positions.get("^出战$")
    control.click(pos.x, pos.y)
    fflag = 0


# 通关
@task.page(name="通关", target_texts=["^完成$"])
def action(positions: Dict[str, Position]):
    pos = positions.get("^完成$")
    control.click(pos.x, pos.y)
    time.sleep(0.1)
    control.click(pos.x, pos.y)


# 重新开始
@task.page(name="重新开始", target_texts=["^重新开始$"])
def action(positions: Dict[str, Position]):
    pos = positions.get("^重新开始$")
    control.click(pos.x, pos.y)
    global fflag
    fflag = 0


@task.page(name="确认", target_texts=["^确认"])
def action(positions: Dict[str, Position]):
    pos = positions.get("^确认")
    control.click(pos.x, pos.y)


@task.page(name="休息_离开", target_texts=["^离开$"])
def action(positions: Dict[str, Position]):
    pos = positions.get("^离开$")
    control.click(pos.x, pos.y)


@task.page(name="主界面", target_texts=["^影像档案架$"])
def action():
    time.sleep(0.5)
    moveRel(400, 0, relative=True)
    time.sleep(0.5)
    press("w", duration=0.2)
    time.sleep(0.5)
    moveRel(380, 0, relative=True)
    time.sleep(0.5)
    press("w", duration=0.8)
    time.sleep(0.5)
    moveRel(-400, 0, relative=True)
    time.sleep(0.5)
    press("w", duration=0.6)
    time.sleep(0.3)
    press("f", duration=0.1)


@task.page(name="可能对话", priority=0)
def action():
    global fflag
    if fflag:
        press("space", duration=0.1)
    time.sleep(0.2)