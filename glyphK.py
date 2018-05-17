#!/usr/bin/env python

# glyphK: touchscreen-less reimplementation of the Ingress glyph minigame
#
# (c) uglynewt,everald 2018
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
import random
import getopt
import sys
import math
import requests

sc_height = 600
sc_width = 800
beige = (220,220,200)
wrong = (255,0,0)
right = (0,200,200)


sequence_dicts = {
	1 : [
		 [ 'ADAPT'],
		 [ 'ABANDON'],
		 [ 'ADVANCE'],
		 [ 'AFTER'],
		 [ 'AGAIN'],
		 [ 'ALL'],
		 [ 'ANSWER'],
		 [ 'ATTACK'],
		 [ 'AVOID'],
		 [ 'BARRIER'],
		 [ 'BEFORE'],
		 [ 'BEGIN'],
		 [ 'BODY'],
		 [ 'BREATHE'],
		 [ 'CAPTURE'],
		 [ 'CHANGE'],
		 [ 'CHAOS'],
		 [ 'CIVILIZATION'],
		 [ 'CLEAR'],
		 [ 'CLEARALL'],
		 [ 'COMPLEX'],
		 [ 'CONFLICT'],
		 [ 'CONSEQUENCE'],
		 [ 'CONTEMPLATE'],
		 [ 'COURAGE'],
		 [ 'CREATE'],
		 [ 'DANGER'],
		 [ 'DATA'],
		 [ 'DEFEND'],
		 [ 'DESTINATION'],
		 [ 'DESTINY'],
		 [ 'DESTROY'],
		 [ 'DETERIORATE'],
		 [ 'DIE'],
		 [ 'DIFFICULT'],
		 [ 'DISCOVER'],
		 [ 'DISTANCE'],
		 [ 'EASY'],
		 [ 'END'],
		 [ 'ENLIGHTENMENT'],
		 [ 'EQUAL'],
		 [ 'ESCAPE'],
		 [ 'EVOLUTION'],
		 [ 'FAILURE'],
		 [ 'FEAR'],
		 [ 'FOLLOW'],
		 [ 'FORGET'],
		 [ 'FUTURE'],
		 [ 'GAIN'],
		 [ 'HARM'],
		 [ 'HARMONY'],
		 [ 'HAVE'],
		 [ 'HELP'],
		 [ 'HIDE'],
		 [ 'HUMAN'],
		 [ 'IDEA'],
		 [ 'IGNORE'],
		 [ 'IMPERFECT'],
		 [ 'IMPROVE'],
		 [ 'IMPURE'],
		 [ 'INSIDE'],
		 [ 'INTERRUPT'],
		 [ 'JOURNEY'],
		 [ 'KNOWLEDGE'],
		 [ 'LEAD'],
		 [ 'LEGACY'],
		 [ 'LESS'],
		 [ 'LIBERATE'],
		 [ 'LIE'],
		 [ 'LIVE AGAIN'],
		 [ 'LOSE'],
		 [ 'MESSAGE'],
		 [ 'MIND'],
		 [ 'MORE'],
		 [ 'MYSTERY'],
		 [ 'NATURE'],
		 [ 'NEW'],
		 [ 'NOURISH'],
		 [ 'N\'ZEER'],
		 [ 'OLD'],
		 [ 'OPEN'],
		 [ 'OPENALL'],
		 [ 'PAST'],
		 [ 'PATH'],
		 [ 'PERFECTION'],
		 [ 'PERSPECTIVE'],
		 [ 'PORTAL'],
		 [ 'POTENTIAL'],
		 [ 'PRESENCE'],
		 [ 'PRESENT'],
		 [ 'PURE'],
		 [ 'PURSUE'],
		 [ 'QUESTION'],
		 [ 'REACT'],
		 [ 'REBEL'],
		 [ 'REPAIR'],
		 [ 'RESISTANCE'],
		 [ 'RESTRAINT'],
		 [ 'RETREAT'],
		 [ 'SAFETY'],
		 [ 'SAVE'],
		 [ 'SEARCH'],
		 [ 'SEE'],
		 [ 'SELF'],
		 [ 'SEPARATE'],
		 [ 'SHAPERS'],
		 [ 'SIMPLE'],
		 [ 'SOUL'],
		 [ 'STABILITY'],
		 [ 'STRONG'],
		 [ 'THEM'],
		 [ 'TOGETHER'],
		 [ 'TRUTH'],
		 [ 'US'],
		 [ 'USE'],
		 [ 'VICTORY'],
		 [ 'WANT'],
		 [ 'WEAK'],
		 [ 'WORTH'],
		 [ 'XM'],
		 [ 'YOU']
	],
	2 : [
		 [ 'ABANDON', 'FEAR'],
		 [ 'ADAPT', 'TECHNOLOGY'],
		 [ 'ALL', 'CHAOS'],
		 [ 'ATTACK', 'CHAOS'],
		 [ 'ATTACK', 'DIFFICULT'],
		 [ 'CAPTURE', 'PORTAL'],
		 [ 'CHANGE', 'PERSPECTIVE'],
		 [ 'CIVILIZATION', 'CHAOS'],
		 [ 'CLEAR', 'CONSEQUENCE'],
		 [ 'CREATE', 'DANGER'],
		 [ 'DESTROY', 'LIVE AGAIN'],
		 [ 'DISCOVER', 'LIE'],
		 [ 'DISCOVER', 'PORTAL'],
		 [ 'DISCOVER', 'SAFETY'],
		 [ 'FUTURE', 'DESTINATION'],
		 [ 'HELP', 'THEM'],
		 [ 'INTERRUPT', 'EVOLUTION'],
		 [ 'LEAD', 'ENLIGHTENMENT'],
		 [ 'LIBERATE', 'XM'],
		 [ 'NOURISH', 'JOURNEY'],
		 [ 'OPENALL', 'TRUTH'],
		 [ 'PATH', 'PERFECTION'],
		 [ 'PORTAL', 'PRESENCE'],
		 [ 'PURE', 'BODY'],
		 [ 'PURE', 'HUMAN'],
		 [ 'PURE', 'TRUTH'],
		 [ 'PURSUE', 'TRUTH'],
		 [ 'PURSUE', 'XM'],
		 [ 'QUESTION', 'WAR'],
		 [ 'SEARCH', 'PAST'],
		 [ 'SEARCH', 'POTENTIAL'],
		 [ 'SEPARATE', 'WAR'],
		 [ 'YOU', 'ADAPT']
	],
	3: [
		 [ 'ABANDON', 'FEAR', 'TOGETHER'],
		 [ 'ACCEPT', 'HUMAN', 'WEAK'],
		 [ 'ADVANCE', 'PURE', 'TRUTH'],
		 [ 'ALL', 'CIVILIZATION', 'CHAOS'],
		 [ 'ANSWER', 'N\'ZEER', 'QUESTION'],
		 [ 'ATTACK', 'SHAPERS', 'CHAOS'],
		 [ 'AVOID', 'CHAOS', 'SOUL'],
		 [ 'AVOID', 'DESTINY', 'LIE'],
		 [ 'AVOID', 'PURE', 'CHAOS'],
		 [ 'BEGIN', 'NEW', 'STRUGGLE'],
		 [ 'CAPTURE', 'VICTORY', 'TOGETHER'],
		 [ 'CHANGE', 'PERSPECTIVE', 'TECHNOLOGY'],
		 [ 'CLEAR', 'YOUR', 'MIND'],
		 [ 'CONFLICT', 'GROW', 'WAR'],
		 [ 'COURAGE', 'DESTINY', 'REBEL'],
		 [ 'CREATE', 'TRUTH', 'LEGACY'],
		 [ 'DANGER', 'CHANGE', 'PAST'],
		 [ 'DEFEND', 'HUMAN', 'LIE'],
		 [ 'DESTROY', 'DIFFICULT', 'BARRIER'],
		 [ 'DESTROY', 'IMPURE', 'TRUTH'],
		 [ 'DISCOVER', 'RESISTANCE', 'TRUTH'],
		 [ 'DISCOVER', 'SHAPERS', 'ENLIGHTENMENT'],
		 [ 'DISCOVER', 'SHAPERS', 'LIE'],
		 [ 'DISCOVER', 'SHAPERS', 'MESSAGE'],
		 [ 'ESCAPE', 'IMPURE', 'EVOLUTION'],
		 [ 'ESCAPE', 'IMPURE', 'FUTURE'],
		 [ 'FEAR', 'IMPERFECT', 'TECHNOLOGY'],
		 [ 'FOLLOW', 'PURE', 'JOURNEY'],
		 [ 'GAIN', 'MORE', 'KNOWLEDGE'],
		 [ 'GROW', 'SHAPERS', 'PRESENCE'],
		 [ 'HARM', 'DANGER', 'AVOID'],
		 [ 'HELP', 'US', 'ALL'],
		 [ 'HUMAN', 'GAIN', 'SAFETY'],
		 [ 'HUMAN', 'KNOWLEDGE', 'LEGACY'],
		 [ 'IMPROVE', 'ADVANCE', 'PRESENT'],
		 [ 'IMPROVE', 'HUMAN', 'SHAPERS'],
		 [ 'INSIDE', 'XM', 'TRUTH'],
		 [ 'INTERRUPT', 'ENLIGHTENED', 'TECHNOLOGY'],
		 [ 'JOURNEY', 'INSIDE', 'SOUL'],
		 [ 'LEAD', 'ENLIGHTENMENT', 'CIVILIZATION'],
		 [ 'LIBERATE', 'HUMAN', 'FUTURE'],
		 [ 'LIE', 'EQUAL', 'FUTURE'],
		 [ 'N\'ZEER', 'TECHNOLOGY', 'PERFECTION'],
		 [ 'PEACE', 'SIMPLE', 'JOURNEY'],
		 [ 'PEACE', 'WORTH', 'MORE'],
		 [ 'PERFECTION', 'PATH', 'PEACE'],
		 [ 'PURSUE', 'PURE', 'BODY'],
		 [ 'QUESTION', 'HIDE', 'TRUTH'],
		 [ 'QUESTION', 'POTENTIAL', 'MYSTERY'],
		 [ 'REACT', 'IMPURE', 'CIVILIZATION'],
		 [ 'RETREAT', 'SEARCH', 'SAFETY'],
		 [ 'SHARE', 'ENLIGHTENMENT', 'KNOWLEDGE'],
		 [ 'SHARE', 'RESISTANCE', 'MESSAGE'],
		 [ 'TECHNOLOGY', 'CAPTURE', 'VICTORY'],
		 [ 'TOGETHER', 'END', 'MYSTERY'],
		 [ 'WAR', 'DESTROY', 'FUTURE'],
		 [ 'XM', 'GROW', 'CREATIVITY'],
		 [ 'XM', 'NOURISH', 'CIVILIZATION'],
		 [ 'YOU', 'HIDE', 'CHAOS']
	],
	4 : [
		 [ 'ABANDON', 'FEAR', 'DEFEND', 'FUTURE'],
		 [ 'ABANDON', 'FEAR', 'SEE', 'FUTURE'],
		 [ 'ADAPT', 'THOUGHT', 'DISCOVER', 'EVOLUTION'],
		 [ 'ALL', 'CHAOS', 'INSIDE', 'BODY'],
		 [ 'ATTACK', 'WEAK', 'SHAPERS', 'LIE'],
		 [ 'BEFORE', 'MYSTERY', 'AFTER', 'KNOWLEDGE'],
		 [ 'BEGIN', 'HUMAN', 'LEGACY', 'NOW'],
		 [ 'BEGIN', 'JOURNEY', 'BREATHE', 'XM'],
		 [ 'BREATHE', 'AGAIN', 'JOURNEY', 'AGAIN'],
		 [ 'BREATHE', 'NATURE', 'PERFECTION', 'HARMONY'],
		 [ 'CAPTURE', 'FEAR', 'DISCOVER', 'COURAGE'],
		 [ 'CHANGE', 'FUTURE', 'CAPTURE', 'DESTINY'],
		 [ 'CHANGE', 'HUMAN', 'POTENTIAL', 'USE'],
		 [ 'CHANGE', 'PERSPECTIVE', 'BEGIN', 'NEW'],
		 [ 'CHAOS', 'BARRIER', 'SHAPERS', 'PORTAL'],
		 [ 'CLEAR', 'MIND', 'OPEN', 'MIND'],
		 [ 'CLEARALL', 'OPENALL', 'DISCOVER', 'TRUTH'],
		 [ 'CONTEMPLATE', 'COMPLEX', 'SHAPERS', 'CIVILIZATION'],
		 [ 'CONTEMPLATE', 'SELF', 'PATH', 'TRUTH'],
		 [ 'COURAGE', 'ATTACK', 'SHAPERS', 'FUTURE'],
		 [ 'CREATE', 'DISTANCE', 'IMPURE', 'PATH'],
		 [ 'CREATE', 'FUTURE', 'NOT', 'WAR'],
		 [ 'CREATE', 'NEW', 'PORTAL', 'POTENTIAL'],
		 [ 'DEFEND', 'HUMAN', 'N\'ZEER', 'LIE'],
		 [ 'DEFEND', 'MESSAGE', 'ANSWER', 'IDEA'],
		 [ 'DESTROY', 'DESTINY', 'HUMAN', 'LIE'],
		 [ 'DETERIORATE', 'HUMAN', 'WEAK', 'REBEL'],
		 [ 'DIFFICULT', 'KNOWLEDGE', 'ADVANCE', 'MIND'],
		 [ 'ENLIGHTENED', 'CAPTURE', 'VICTORY', 'TOGETHER'],
		 [ 'ESCAPE', 'BEFORE', 'PURE', 'DEATH'],
		 [ 'ESCAPE', 'SIMPLE', 'HUMAN', 'FUTURE'],
		 [ 'FEAR', 'IMPERFECT', 'N\'ZEER', 'TECHNOLOGY'],
		 [ 'FOLLOW', 'SHAPERS', 'PORTAL', 'MESSAGE'],
		 [ 'FORGET', 'CONFLICT', 'ACCEPT', 'WAR'],
		 [ 'HARMONY', 'PATH', 'NOURISH', 'PRESENT'],
		 [ 'HELP', 'ENLIGHTENED', 'STRONG', 'VICTORY'],
		 [ 'HELP', 'GAIN', 'CREATE', 'PURSUE'],
		 [ 'HELP', 'RESISTANCE', 'STRONG', 'VICTORY'],
		 [ 'HELP', 'US', 'SAVE', 'US'],
		 [ 'HIDE', 'CHAOS', 'INSIDE', 'BODY'],
		 [ 'HIDE', 'IMPURE', 'HUMAN', 'THOUGHT'],
		 [ 'HUMAN', 'HAVE', 'IMPURE', 'CIVILIZATION'],
		 [ 'HUMAN', 'PAST', 'PRESENT', 'FUTURE'],
		 [ 'HUMAN', 'SOUL', 'STRONG', 'PURE'],
		 [ 'IGNORE', 'HUMAN', 'CHAOS', 'LIE'],
		 [ 'IMPROVE', 'BODY', 'MIND', 'SOUL'],
		 [ 'IMPROVE', 'BODY', 'PURSUE', 'JOURNEY'],
		 [ 'INSIDE', 'MIND', 'JOURNEY', 'PERFECTION'],
		 [ 'INTERRUPT', 'MESSAGE', 'GAIN', 'ADVANCE'],
		 [ 'JOURNEY', 'NOT', 'IMPROVE', 'SOUL'],
		 [ 'KNOWLEDGE', 'HELP', 'GAIN', 'VICTORY'],
		 [ 'LEAD', 'PURSUE', 'REACT', 'DEFEND'],
		 [ 'LESS', 'SOUL', 'MORE', 'MIND'],
		 [ 'LESS', 'TRUTH', 'MORE', 'CHAOS'],
		 [ 'LIBERATE', 'XM', 'PORTAL', 'TOGETHER'],
		 [ 'LIVE AGAIN', 'DIE', 'AGAIN', 'EVOLUTION'],
		 [ 'LOSE', 'DANGER', 'GAIN', 'SAFETY'],
		 [ 'NOURISH', 'XM', 'CREATE', 'THOUGHT'],
		 [ 'N\'ZEER', 'LEGACY', 'CREATE', 'FUTURE'],
		 [ 'N\'ZEER', 'SHAPERS', 'STRUGGLE', 'KNOWLEDGE'],
		 [ 'N\'ZEER', 'TECHNOLOGY', 'MIND', 'EVOLUTION'],
		 [ 'N\'ZEER', 'TECHNOLOGY', 'PERFECTION', 'TRUTH'],
		 [ 'PAST', 'AGAIN', 'PRESENT', 'AGAIN'],
		 [ 'PATH', 'RESTRAINT', 'STRONG', 'SAFETY'],
		 [ 'PORTAL', 'CHANGE', 'CIVILIZATION', 'END'],
		 [ 'PORTAL', 'DIE', 'CIVILIZATION', 'DIE'],
		 [ 'QUESTION', 'TRUTH', 'GAIN', 'FUTURE'],
		 [ 'RESTRAINT', 'FEAR', 'AVOID', 'DANGER'],
		 [ 'RESTRAINT', 'PATH', 'GAIN', 'HARMONY'],
		 [ 'SEARCH', 'DATA', 'DISCOVER', 'PATH'],
		 [ 'SEARCH', 'TRUTH', 'SAVE', 'CIVILIZATION'],
		 [ 'SEARCH', 'XM', 'DISTANCE', 'DESTINATION'],
		 [ 'SEARCH', 'XM', 'SAVE', 'PORTAL'],
		 [ 'SEE', 'TRUTH', 'SEE', 'FUTURE'],
		 [ 'SEPARATE', 'WEAK', 'IGNORE', 'TRUTH'],
		 [ 'SHAPERS', 'CHAOS', 'PURE', 'HARM'],
		 [ 'SHAPERS', 'MESSAGE', 'END', 'CIVILIZATION'],
		 [ 'SHAPERS', 'MIND', 'COMPLEX', 'HARMONY'],
		 [ 'SHAPERS', 'PAST', 'PRESENT', 'FUTURE'],
		 [ 'SHAPERS', 'SEE', 'POTENTIAL', 'EVOLUTION'],
		 [ 'SIMPLE', 'CIVILIZATION', 'IMPURE', 'WEAK'],
		 [ 'SIMPLE', 'MESSAGE', 'COMPLEX', 'IDEA'],
		 [ 'SIMPLE', 'TRUTH', 'BREATHE', 'NATURE'],
		 [ 'SOUL', 'REBEL', 'HUMAN', 'DIE'],
		 [ 'STAY', 'TOGETHER', 'DEFEND', 'TRUTH'],
		 [ 'STRONG', 'IDEA', 'PURSUE', 'TRUTH'],
		 [ 'STRONG', 'TOGETHER', 'AVOID', 'WAR'],
		 [ 'STRUGGLE', 'DEFEND', 'SHAPERS', 'DANGER'],
		 [ 'STRUGGLE', 'IMPROVE', 'HUMAN', 'SOUL'],
		 [ 'TOGETHER', 'DISCOVER', 'HARMONY', 'EQUAL'],
		 [ 'TRUTH', 'IDEA', 'DISCOVER', 'XM'],
		 [ 'WAR', 'NOT', 'WORTH', 'CONSEQUENCE'],
		 [ 'XM', 'DIE', 'CHAOS', 'LIVE'],
		 [ 'XM', 'NOURISH', 'STRONG', 'CREATIVITY'],
		 [ 'XM', 'SHARE', 'YOUR', 'CREATIVITY']
	],
	5 : [
		 [ 'ABANDON', 'ALL', 'TECHNOLOGY', 'SAVE', 'US'],
		 [ 'ABANDON', 'FEAR', 'DEFEND', 'FUTURE', 'TOGETHER'],
		 [ 'ABANDON', 'FEAR', 'SEE', 'FUTURE', 'DESTINATION'],
		 [ 'ADAPT', 'THOUGHT', 'DISCOVER', 'SIMPLE', 'SUCCESS'],
		 [ 'ADVANCE', 'CIVILIZATION', 'PURSUE', 'SHAPERS', 'PATH'],
		 [ 'AFTER', 'IMPERFECT', 'HUMAN', 'PRESENCE', 'CONSEQUENCE'],
		 [ 'ANSWER', 'N\'ZEER', 'QUESTION', 'POTENTIAL', 'KNOWLEDGE'],
		 [ 'ANSWER', 'QUESTION', 'DISCOVER', 'DIFFICULT', 'TRUTH'],
		 [ 'AVOID', 'CHAOS', 'AVOID', 'SHAPERS', 'LIE'],
		 [ 'AVOID', 'CHAOS', 'REPAIR', 'POTENTIAL', 'WAR'],
		 [ 'AVOID', 'PERFECTION', 'STAY', 'HUMAN', 'SELF'],
		 [ 'BEGIN', 'JOURNEY', 'BREATHE', 'XM', 'EVOLUTION'],
		 [ 'BREATHE', 'INSIDE', 'XM', 'LOSE', 'SELF'],
		 [ 'CAPTURE', 'PORTAL', 'DEFEND', 'PORTAL', 'COURAGE'],
		 [ 'CHANGE', 'PERSPECTIVE', 'BEGIN', 'NEW', 'STRUGGLE'],
		 [ 'CHAOS', 'WAR', 'CONFLICT', 'DISCOVER', 'PEACE'],
		 [ 'CIVILIZATION', 'DIE', 'NEW', 'CIVILIZATION', 'BEGIN'],
		 [ 'CLEAR', 'MIND', 'LIBERATE', 'BARRIER', 'BODY'],
		 [ 'CLEAR', 'YOUR', 'MIND', 'CREATIVITY(1216274548597A9A)', 'GROW'],
		 [ 'CLEAR', 'YOUR', 'MIND', 'MORE', 'BALANCE'],
		 [ 'CLEARALL', 'IDEA', 'PAST', 'PRESENT', 'FUTURE'],
		 [ 'CONTEMPLATE', 'FUTURE', 'NOT', 'SHAPERS', 'PATH'],
		 [ 'CONTEMPLATE', 'RESTRAINT', 'DISCOVER', 'MORE', 'COURAGE'],
		 [ 'COURAGE', 'ATTACK', 'SHAPERS', 'PORTAL', 'TOGETHER'],
		 [ 'CREATE', 'NEW', 'FUTURE', 'SEE', 'ALL'],
		 [ 'CREATE', 'NEW', 'PORTAL', 'POTENTIAL', 'FUTURE'],
		 [ 'CREATE', 'PURE', 'FUTURE', 'HUMAN', 'CIVILIZATION'],
		 [ 'CREATE', 'PURE', 'FUTURE', 'NOT', 'WAR'],
		 [ 'CREATE', 'SEPARATE', 'PATH', 'END', 'JOURNEY'],
		 [ 'DEFEND', 'DESTINY', 'DEFEND', 'HUMAN', 'CIVILIZATION'],
		 [ 'DEFEND', 'HUMAN', 'CIVILIZATION', 'XM', 'MESSAGE'],
		 [ 'DEFEND', 'HUMAN', 'CIVILIZATION', 'PORTAL', 'DATA'],
		 [ 'DEFEND', 'HUMAN', 'CIVILIZATION', 'SHAPERS', 'LIE'],
		 [ 'DEFEND', 'HUMAN', 'CIVILIZATION', 'SHAPERS', 'PORTAL'],
		 [ 'DESTROY', 'CIVILIZATION', 'END', 'CONFLICT', 'WAR'],
		 [ 'DESTROY', 'LIE', 'NOT', 'GAIN', 'SOUL'],
		 [ 'DISTANCE', 'SELF', 'AVOID', 'HUMAN', 'LIE'],
		 [ 'EASY', 'PATH', 'FUTURE', 'FOLLOW', 'SHAPERS'],
		 [ 'END', 'OLD', 'CIVILIZATION', 'CREATE', 'NEW'],
		 [ 'ESCAPE', 'BEFORE', 'DEATH', 'END', 'ALL'],
		 [ 'ESCAPE', 'BODY', 'JOURNEY', 'OUTSIDE', 'PRESENT'],
		 [ 'ESCAPE', 'BODY', 'MIND', 'SELF', 'WANT'],
		 [ 'FORGET', 'WAR', 'SEE', 'DISTANCE', 'HARMONY'],
		 [ 'FORGET', 'PAST', 'SEE', 'PRESENT', 'DANGER'],
		 [ 'GAIN', 'TRUTH', 'OPEN', 'HUMAN', 'SOUL'],
		 [ 'GROW', 'UNBOUNDED', 'CREATE', 'NEW', 'FUTURE'],
		 [ 'HAVE', 'HARMONY', 'TOGETHER', 'END', 'MYSTERY'],
		 [ 'HARM', 'PROGRESS', 'PURSUE', 'MORE', 'WAR'],
		 [ 'HELP', 'ENLIGHTENMENT', 'CAPTURE', 'ALL', 'PORTAL'],
		 [ 'HELP', 'GAIN', 'KNOWLEDGE', 'INSIDE', 'RESISTANCE'],
		 [ 'HELP', 'HUMAN', 'CIVILIZATION', 'PURSUE', 'DESTINY'],
		 [ 'HELP', 'US', 'PROGRESS', 'STRONG', 'VICTORY'],
		 [ 'HELP', 'US', 'SAVE', 'US', 'ALL'],
		 [ 'HELP', 'US', 'SAVE', 'US', 'DESTROY'],
		 [ 'HELP', 'RESISTANCE', 'CAPTURE', 'ALL', 'PORTAL'],
		 [ 'HIDE', 'STRUGGLE', 'ADVANCE', 'STRONG', 'TOGETHER'],
		 [ 'HIDE', 'THEM', 'INSIDE', 'COMPLEX', 'INTELLIGENCE'],
		 [ 'HUMAN', 'LEGACY', 'ABANDON', 'OLD', 'KNOWLEDGE'],
		 [ 'HUMAN', 'LEGACY', 'HAVE', 'ABANDON', 'NOW'],
		 [ 'HUMAN', 'NOT', 'TOGETHER', 'CIVILIZATION', 'DETERIORATE'],
		 [ 'HUMAN', 'SHAPERS', 'TOGETHER', 'CREATE', 'DESTINY'],
		 [ 'IMPERFECT', 'MESSAGE', 'BEGIN', 'HUMAN', 'CHAOS'],
		 [ 'IMPERFECT', 'TRUTH', 'ACCEPT', 'COMPLEX', 'ANSWER'],
		 [ 'IMPERFECT', 'XM', 'MESSAGE', 'HUMAN', 'CHAOS'],
		 [ 'INSIDE', 'MIND', 'INSIDE', 'SOUL', 'HARMONY'],
		 [ 'INTERRUPT', 'ENLIGHTENED', 'TECHNOLOGY', 'CAPTURE', 'VICTORY'],
		 [ 'INTERRUPT', 'MESSAGE', 'LOSE', 'COLLECTIVE', 'POTENTIAL'],
		 [ 'LIBERATE', 'PORTAL', 'LIBERATE', 'HUMAN', 'MIND'],
		 [ 'LIBERATE', 'SELF', 'LIBERATE', 'HUMAN', 'CIVILIZATION'],
		 [ 'LIVE AGAIN', 'DIE', 'REPEAT', 'EVOLUTION', 'FUTURE'],
		 [ 'LOSE', 'SHAPERS', 'MESSAGE', 'GAIN', 'CHAOS'],
		 [ 'MIND', 'BODY', 'SOUL', 'PURE', 'HUMAN'],
		 [ 'MIND', 'TECHNOLOGY', 'CAPTURE', 'HUMAN', 'SOUL'],
		 [ 'MORE', 'DATA', 'GAIN', 'PORTAL', 'ADVANCE'],
		 [ 'MYSTERY', 'BEFORE', 'PURE', 'KNOWLEDGE', 'AFTER'],
		 [ 'N\'ZEER', 'HIDE', 'US', 'EQUAL', 'THEM'],
		 [ 'OLD', 'NATURE', 'LESS', 'STRONG', 'PRESENT'],
		 [ 'PAST', 'CHAOS', 'CREATE', 'FUTURE', 'HARMONY'],
		 [ 'PAST', 'PATH', 'CREATE', 'FUTURE', 'JOURNEY'],
		 [ 'PORTAL', 'BARRIER', 'DEFEND', 'HUMAN', 'SHAPERS'],
		 [ 'PORTAL', 'CREATE', 'DANGER', 'PURSUE', 'SAFETY'],
		 [ 'PORTAL', 'IMPROVE', 'HUMAN', 'FUTURE', 'CIVILIZATION'],
		 [ 'PORTAL', 'POTENTIAL', 'HELP', 'HUMAN', 'FUTURE'],
		 [ 'PRESENCE', 'LIE', 'EQUAL', 'FUTURE', 'CONSEQUENCE'],
		 [ 'PRESENT', 'CHAOS', 'CREATE', 'FUTURE', 'CIVILIZATION'],
		 [ 'PRESENT', 'STRUGGLE', 'WORTH', 'STRONG', 'VICTORY'],
		 [ 'PURE', 'HUMAN', 'FAILURE', 'NOW', 'CHAOS'],
		 [ 'PURSUE', 'CONFLICT', 'WAR', 'ADVANCE', 'CHAOS'],
		 [ 'PURSUE', 'PATH', 'OUTSIDE', 'SHAPERS', 'LIE'],
		 [ 'QUESTION', 'LESS', 'FORGET', 'ALL', 'LIE'],
		 [ 'QUESTION', 'POTENTIAL', 'MYSTERY', 'JOURNEY', 'GROW'],
		 [ 'REACT', 'REBEL', 'QUESTION', 'SHAPERS', 'LIE'],
		 [ 'REBEL', 'THOUGHT', 'EVOLUTION', 'DESTINY', 'NOW'],
		 [ 'REPAIR', 'PRESENT', 'REPAIR', 'HUMAN', 'SOUL'],
		 [ 'REPAIR', 'SOUL', 'LESS', 'HUMAN', 'HARM'],
		 [ 'SAVE', 'HUMAN', 'CIVILIZATION', 'DESTROY', 'PORTAL'],
		 [ 'SEARCH', 'DESTINY', 'CREATE', 'PURE', 'FUTURE'],
		 [ 'SEE', 'TRUTH', 'SEE', 'FUTURE', 'BEGIN'],
		 [ 'SEPARATE', 'MIND', 'BODY', 'DISCOVER', 'ENLIGHTENMENT'],
		 [ 'SEPARATE', 'TRUTH', 'LIE', 'SHAPERS', 'FUTURE'],
		 [ 'SHAPERS', 'LEAD', 'HUMAN', 'COMPLEX', 'JOURNEY'],
		 [ 'SHAPERS', 'PORTAL', 'DATA', 'CREATE', 'CHAOS'],
		 [ 'SHAPERS', 'PORTAL', 'MESSAGE', 'DESTROY', 'CIVILIZATION'],
		 [ 'SHAPERS', 'SEE', 'COMPLEX', 'PATH', 'DESTINY'],
		 [ 'SHAPERS', 'WANT', 'HUMAN', 'MIND', 'FUTURE'],
		 [ 'SIMPLE', 'OLD', 'TRUTH', 'JOURNEY', 'INSIDE'],
		 [ 'SIMPLE', 'TRUTH', 'FORGET', 'EASY', 'SUCCESS'],
		 [ 'SIMPLE', 'TRUTH', 'SHAPERS', 'DESTROY', 'CIVILIZATION'],
		 [ 'STAY', 'STRONG', 'TOGETHER', 'DEFEND', 'RESISTANCE'],
		 [ 'STRONG', 'TOGETHER', 'WAR', 'TOGETHER', 'CHAOS'],
		 [ 'STRONG', 'TOGETHER', 'WAR', 'TOGETHER', 'DESTINY'],
		 [ 'TECHNOLOGY', 'INTELLIGENCE', 'SEE', 'ALL', 'UNBOUNDED'],
		 [ 'TOGETHER', 'PROGRESS', 'RECHARGE', 'PRESENT', 'JOURNEY'],
		 [ 'USE', 'MIND', 'USE', 'COURAGE', 'CHANGE'],
		 [ 'USE', 'RESTRAINT', 'FOLLOW', 'EASY', 'PATH'],
		 [ 'WANT', 'NEW', 'DESTINATION', 'IGNORE', 'CONSEQUENCE'],
		 [ 'WANT', 'TRUTH', 'PURSUE', 'DIFFICULT', 'PATH'],
		 [ 'WEAK', 'HUMAN', 'DESTINY', 'DESTROY', 'CIVILIZATION'],
		 [ 'XM', 'CREATE', 'COMPLEX', 'HUMAN', 'DESTINY'],
		 [ 'XM', 'PATH', 'FUTURE', 'DESTINY', 'HARMONY'],
		 [ 'XM', 'PORTAL', 'SHARE', 'YOUR', 'CREATIVITY'],
		 [ 'YOU', 'HIDE', 'CHAOS', 'INSIDE', 'BODY'],
		 [ 'YOUR', 'MESSAGE', 'CLEAR', 'USE', 'CHAOS']
	]
}

glyph_dict = {
	'ABANDON' : [ ['1','6'], ['3','4'], ['4','8'], ['6','a'], ['8','a'] ],
	'ADAPT' : [ ['5','8'], ['7','a'], ['8','a'] ],
	'ADVANCE' : [ ['0','9'], ['4','9'] ],
	'AFTER' : [ ['1','2'], ['1','6'], ['2','7'], ['6','a'], ['7','a'] ],
	'AGAIN' : [ ['4','9'], ['6','7'], ['6','a'], ['8','9'], ['8','a'] ],
	'REPEAT' : [ ['4','9'], ['6','7'], ['6','a'], ['8','9'], ['8','a'] ],
	'ALL' : [ ['0','1'], ['0','5'], ['1','2'], ['2','3'], ['3','4'], ['4','5'] ],
	'ANSWER' : [ ['6','7'], ['6','9'], ['7','a'] ],
	'ATTACK' : [ ['0','6'], ['0','9'], ['2','6'], ['4','9'] ],
	'WAR' : [ ['0','6'], ['0','9'], ['2','6'], ['4','9'] ],
	'AVOID' : [ ['0','5'], ['0','6'], ['1','6'], ['1','7'] ],
	'BARRIER' : [ ['0','a'], ['2','7'], ['7','a'] ],
	'OBSTACLE' : [ ['0','a'], ['2','7'], ['7','a'] ],
	'BEFORE' : [ ['4','5'], ['4','8'], ['5','9'], ['8','a'], ['9','a'] ],
	'BEGIN' : [ ['0','8'], ['3','7'], ['3','8'] ],
	'BEING' : [ ['3','7'], ['3','8'], ['6','7'], ['6','9'], ['8','9'] ],
	'HUMAN' : [ ['3','7'], ['3','8'], ['6','7'], ['6','9'], ['8','9'] ],
	'BODY' : [ ['6','9'], ['6','a'], ['9','a'] ],
	'SHELL' : [ ['6','9'], ['6','a'], ['9','a'] ],
	'BREATHE' : [ ['1','6'], ['5','9'], ['6','a'], ['9','a'] ],
	'LIVE' : [ ['1','6'], ['5','9'], ['6','a'], ['9','a'] ],
	'CAPTURE' : [ ['1','7'], ['3','4'], ['4','8'], ['7','a'], ['8','a'] ],
	'CHANGE' : [ ['3','7'], ['3','a'], ['8','a'] ],
	'MODIFY' : [ ['3','7'], ['3','a'], ['8','a'] ],
	'CHAOS' : [ ['0','1'], ['0','5'], ['1','6'], ['3','8'], ['4','5'], ['6','a'], ['8','a'] ],
	'DISORDER' : [ ['0','1'], ['0','5'], ['1','6'], ['3','8'], ['4','5'], ['6','a'], ['8','a'] ],
	'CLEAR' : [ ['0','a'], ['3','a'] ],
	'CLOSE ALL' : [ ['0','1'], ['0','5'], ['0','a'], ['1','2'], ['2','3'], ['3','4'], ['3','a'], ['4','5'] ],
	'CLEAR ALL' : [ ['0','1'], ['0','5'], ['0','a'], ['1','2'], ['2','3'], ['3','4'], ['3','a'], ['4','5'] ],
	'CLEARALL' : [ ['0','1'], ['0','5'], ['0','a'], ['1','2'], ['2','3'], ['3','4'], ['3','a'], ['4','5'] ],
	'COMPLEX' : [ ['6','9'], ['8','a'], ['9','a'] ],
	'CONFLICT' : [ ['2','6'], ['4','9'], ['6','7'], ['7','8'], ['8','9'] ],
	'CONSEQUENCE' : [ ['2','7'], ['5','9'], ['7','8'], ['8','9'] ],
	'CONTEMPLATE' : [ ['0','1'], ['1','2'], ['2','3'], ['3','8'], ['6','a'], ['8','9'], ['9','a'] ],
	'COURAGE' : [ ['4','9'], ['7','8'], ['8','9'] ],
	'CREATE' : [ ['1','6'], ['4','8'], ['6','a'], ['8','a'] ],
	'CREATION' : [ ['1','6'], ['4','8'], ['6','a'], ['8','a'] ],
	'CREATIVITY' : [ ['1','2'], ['1','6'], ['2','7'], ['4','5'], ['4','8'], ['5','9'], ['7','a'], ['9','a'] ],
	'IDEA' : [ ['1','2'], ['1','6'], ['2','7'], ['4','5'], ['4','8'], ['5','9'], ['7','a'], ['9','a'] ],
	'THOUGHT' : [ ['1','2'], ['1','6'], ['2','7'], ['4','5'], ['4','8'], ['5','9'], ['7','a'], ['9','a'] ],
	'CREATIVITY' : [ ['3','9'], ['3','a'], ['9','a'] ],
	'DANGER' : [ ['0','9'], ['3','a'], ['9','a'] ],
	'DATA' : [ ['0','6'], ['3','8'], ['6','a'], ['8','a'] ],
	'SIGNAL' : [ ['0','6'], ['3','8'], ['6','a'], ['8','a'] ],
	'DEFEND' : [ ['1','7'], ['3','7'], ['3','8'], ['5','8'] ],
	'DESTINY' : [ ['3','8'], ['6','7'], ['6','a'], ['7','8'], ['9','a'] ],
	'DESTINATION' : [ ['1','2'], ['2','3'] ],
	'DESTROY' : [ ['2','7'], ['5','9'], ['7','a'], ['9','a'] ],
	'DESTRUCTION' : [ ['2','7'], ['5','9'], ['7','a'], ['9','a'] ],
	'DETERIORATE' : [ ['4','8'], ['8','a'], ['9','a'] ],
	'ERODE' : [ ['4','8'], ['8','a'], ['9','a'] ],
	'EASY' : [ ['3','8'], ['6','a'], ['8','a'] ],
	'DIE' : [ ['2','7'], ['4','8'], ['7','a'], ['8','a'] ],
	'DEATH' : [ ['2','7'], ['4','8'], ['7','a'], ['8','a'] ],
	'DIFFICULT' : [ ['1','6'], ['6','7'], ['7','a'], ['8','a'] ],
	'DISCOVER' : [ ['1','2'], ['2','3'], ['3','4'] ],
	'DISTANCE' : [ ['0','5'], ['4','5'] ],
	'OUTSIDE' : [ ['0','5'], ['4','5'] ],
	'END' : [ ['0','1'], ['0','a'], ['1','7'], ['3','7'], ['3','a'] ],
	'CLOSE' : [ ['0','1'], ['0','a'], ['1','7'], ['3','7'], ['3','a'] ],
	'ENLIGHTENED' : [ ['0','1'], ['0','9'], ['1','2'], ['2','3'], ['6','9'], ['6','a'], ['9','a'] ],
	'ENLIGHTENMENT' : [ ['0','1'], ['0','9'], ['1','2'], ['2','3'], ['6','9'], ['6','a'], ['9','a'] ],
	'EQUAL' : [ ['6','7'], ['6','9'], ['8','9'] ],
	'ESCAPE' : [ ['0','1'], ['1','6'], ['6','9'], ['8','9'] ],
	'EVOLUTION' : [ ['0','a'], ['8','9'], ['9','a'] ],
	'PROGRESS' : [ ['0','a'], ['8','9'], ['9','a'] ],
	'SUCCESS' : [ ['0','a'], ['8','9'], ['9','a'] ],
	'FAILURE' : [ ['0','a'], ['6','7'], ['6','a'] ],
	'FEAR' : [ ['1','7'], ['6','7'], ['6','9'] ],
	'FOLLOW' : [ ['0','6'], ['1','2'], ['1','6'] ],
	'FORGET' : [ ['4','8'] ],
	'FUTURE' : [ ['1','6'], ['2','7'], ['6','7'] ],
	'GAIN' : [ ['5','8'] ],
	'GOVERNMENT' : [ ['1','6'], ['5','9'], ['6','7'], ['7','8'], ['8','9'] ],
	'CITY' : [ ['1','6'], ['5','9'], ['6','7'], ['7','8'], ['8','9'] ],
	'CIVILIZATION' : [ ['1','6'], ['5','9'], ['6','7'], ['7','8'], ['8','9'] ],
	'STRUCTURE' : [ ['1','6'], ['5','9'], ['6','7'], ['7','8'], ['8','9'] ],
	'GROW' : [ ['4','9'], ['8','9'] ],
	'HARM' : [ ['0','6'], ['0','9'], ['2','7'], ['6','a'], ['7','a'], ['9','a'] ],
	'HARMONY' : [ ['0','6'], ['0','9'], ['3','7'], ['3','8'], ['6','a'], ['7','a'], ['8','a'], ['9','a'] ],
	'PEACE' : [ ['0','6'], ['0','9'], ['3','7'], ['3','8'], ['6','a'], ['7','a'], ['8','a'], ['9','a'] ],
	'HAVE' : [ ['3','8'], ['7','a'], ['8','a'] ],
	'HELP' : [ ['5','9'], ['7','8'], ['8','a'], ['9','a'] ],
	'HIDE' : [ ['1','6'], ['1','7'], ['6','9'], ['7','8'] ],
	'I' : [ ['3','6'], ['3','9'], ['6','9'] ],
	'ME' : [ ['3','6'], ['3','9'], ['6','9'] ],
	'IGNORE' : [ ['2','7'] ],
	'IMPERFECT' : [ ['6','8'], ['6','a'], ['8','9'], ['8','a'], ['9','a'] ],
	'IMPROVE' : [ ['1','6'], ['6','a'], ['7','a'] ],
	'IMPURE' : [ ['3','a'], ['8','9'], ['8','a'], ['9','a'] ],
	'INTELLIGENCE' : [ ['1','6'], ['4','8'], ['6','a'], ['8','9'], ['9','a'] ],
	'INTERRUPT' : [ ['0','a'], ['3','a'], ['4','5'], ['4','8'], ['5','9'], ['8','a'], ['9','a'] ],
	'JOURNEY' : [ ['1','6'], ['3','4'], ['4','5'], ['5','9'], ['6','a'], ['9','a'] ],
	'KNOWLEDGE' : [ ['3','6'], ['3','9'], ['6','a'], ['9','a'] ],
	'LEAD' : [ ['0','5'], ['3','8'], ['4','5'], ['4','8'] ],
	'LEGACY' : [ ['0','1'], ['0','5'], ['1','6'], ['2','7'], ['4','8'], ['5','9'], ['6','7'], ['8','9'] ],
	'LESS' : [ ['6','a'], ['9','a'] ],
	'LIBERATE' : [ ['0','1'], ['1','6'], ['4','9'], ['6','a'], ['9','a'] ],
	'LIE' : [ ['6','7'], ['6','a'], ['7','a'], ['8','9'], ['9','a'] ],
	'LIVE AGAIN' : [ ['1','6'], ['4','9'], ['6','a'], ['8','9'], ['8','a'] ],
	'REINCARNATE' : [ ['1','6'], ['4','9'], ['6','a'], ['8','9'], ['8','a'] ],
	'LOSE' : [ ['1','7'] ],
	'MESSAGE' : [ ['1','7'], ['4','9'], ['7','a'], ['9','a'] ],
	'MIND' : [ ['3','8'], ['3','a'], ['8','9'], ['9','a'] ],
	'MORE' : [ ['7','a'], ['8','a'] ],
	'MYSTERY' : [ ['0','6'], ['0','9'], ['5','9'], ['6','9'], ['8','9'] ],
	'N\'ZEER' : [ ['0','6'], ['0','9'], ['0','a'], ['3','a'], ['6','a'], ['9','a'] ],
	'NATURE' : [ ['2','7'], ['4','8'], ['6','7'], ['6','9'], ['8','9'] ],
	'NEW' : [ ['2','7'], ['6','7'] ],
	'NOT' : [ ['6','7'], ['6','9'] ],
	'INSIDE' : [ ['6','7'], ['6','9'] ],
	'NOURISH' : [ ['3','4'], ['3','a'], ['4','8'], ['8','a'] ],
	'OLD' : [ ['5','9'], ['8','9'] ],
	'OPEN' : [ ['3','7'], ['3','8'], ['7','8'] ],
	'ACCEPT' : [ ['3','7'], ['3','8'], ['7','8'] ],
	'OPEN ALL' : [ ['0','1'], ['0','5'], ['1','2'], ['2','3'], ['3','4'], ['3','7'], ['3','8'], ['4','5'], ['7','8'] ],
	'OPENALL' : [ ['0','1'], ['0','5'], ['1','2'], ['2','3'], ['3','4'], ['3','7'], ['3','8'], ['4','5'], ['7','8'] ],
	'PORTAL' : [ ['1','2'], ['1','6'], ['2','7'], ['4','5'], ['4','8'], ['5','9'], ['6','9'], ['7','8'] ],
	'PAST' : [ ['4','8'], ['5','9'], ['8','9'] ],
	'PATH' : [ ['0','a'], ['4','8'], ['8','a'] ],
	'PERFECTION' : [ ['0','a'], ['2','3'], ['2','7'], ['3','4'], ['4','8'], ['7','a'], ['8','a'] ],
	'BALANCE' : [ ['0','a'], ['2','3'], ['2','7'], ['3','4'], ['4','8'], ['7','a'], ['8','a'] ],
	'PERSPECTIVE' : [ ['0','6'], ['0','9'], ['2','7'], ['4','8'], ['6','a'], ['7','a'], ['8','a'], ['9','a'] ],
	'POTENTIAL' : [ ['0','a'], ['1','2'], ['2','7'], ['7','a'] ],
	'PRESENCE' : [ ['3','7'], ['3','8'], ['6','7'], ['6','a'], ['7','8'], ['8','9'], ['9','a'] ],
	'PRESENT' : [ ['6','7'], ['7','8'], ['8','9'] ],
	'NOW' : [ ['6','7'], ['7','8'], ['8','9'] ],
	'PURE' : [ ['0','a'], ['6','7'], ['6','a'], ['7','a'] ],
	'PURSUE' : [ ['0','6'], ['0','9'], ['5','9'] ],
	'CHASE' : [ ['0','a'], ['4','8'], ['8','9'], ['9','a'] ],
	'QUESTION' : [ ['0','6'], ['6','9'], ['8','9'] ],
	'REACT' : [ ['2','7'], ['6','9'], ['7','a'], ['9','a'] ],
	'REBEL' : [ ['1','2'], ['1','6'], ['5','8'], ['6','a'], ['8','a'] ],
	'RECHARGE' : [ ['0','5'], ['0','a'], ['5','9'], ['9','a'] ],
	'REPAIR' : [ ['0','5'], ['0','a'], ['5','9'], ['9','a'] ],
	'REDUCE' : [ ['2','6'], ['6','7'] ],
	'RESIST' : [ ['0','9'], ['0','a'], ['3','8'], ['3','a'], ['6','9'] ],
	'RESISTANCE' : [ ['0','9'], ['0','a'], ['3','8'], ['3','a'], ['6','9'] ],
	'STRUGGLE' : [ ['0','9'], ['0','a'], ['3','8'], ['3','a'], ['6','9'] ],
	'RESTRAINT' : [ ['2','3'], ['2','7'], ['5','9'], ['7','a'], ['9','a'] ],
	'RETREAT' : [ ['0','6'], ['2','6'] ],
	'SAFETY' : [ ['2','6'], ['4','9'], ['6','9'] ],
	'SAVE' : [ ['1','7'], ['7','a'], ['8','a'] ],
	'SEE' : [ ['0','9'] ],
	'SEEK' : [ ['6','9'], ['6','a'], ['7','8'], ['8','9'] ],
	'SEARCH' : [ ['6','9'], ['6','a'], ['7','8'], ['8','9'] ],
	'SELF' : [ ['2','3'], ['3','4'] ],
	'INDIVIDUAL' : [ ['2','3'], ['3','4'] ],
	'SEPARATE' : [ ['2','7'], ['5','9'], ['6','7'], ['6','a'], ['8','9'], ['8','a'] ],
	'SHAPERS' : [ ['0','6'], ['0','9'], ['2','7'], ['4','8'], ['6','7'], ['8','9'] ],
	'COLLECTIVE' : [ ['0','6'], ['0','9'], ['2','7'], ['4','8'], ['6','7'], ['8','9'] ],
	'SHARE' : [ ['2','7'], ['3','4'], ['4','8'], ['7','8'] ],
	'SIMPLE' : [ ['7','8'] ],
	'SOUL' : [ ['3','7'], ['3','a'], ['6','7'], ['6','a'] ],
	'STABILITY' : [ ['2','7'], ['4','8'], ['7','8'] ],
	'STAY' : [ ['2','7'], ['4','8'], ['7','8'] ],
	'STRONG' : [ ['6','7'], ['6','9'], ['7','8'], ['8','9'] ],
	'SUSTAIN' : [ ['0','a'], ['1','2'], ['1','6'], ['2','7'], ['3','a'], ['6','a'], ['7','a'] ],
	'SUSTAIN ALL' : [ ['0','1'], ['0','5'], ['0','a'], ['1','2'], ['1','6'], ['2','3'], ['2','7'], ['3','4'], ['3','a'], ['4','5'], ['6','a'], ['7','a'] ],
	'TECHNOLOGY' : [ ['1','6'], ['2','7'], ['6','a'], ['7','a'], ['8','9'], ['8','a'], ['9','a'] ],
	'THEM' : [ ['0','8'], ['7','8'] ],
	'TOGETHER' : [ ['4','8'], ['6','9'], ['6','a'], ['8','a'], ['9','a'] ],
	'TRUTH' : [ ['6','7'], ['6','a'], ['7','a'], ['8','9'], ['8','a'], ['9','a'] ],
	'UNBOUNDED' : [ ['0','1'], ['0','5'], ['1','7'], ['2','3'], ['3','4'], ['4','5'], ['6','9'], ['6','a'], ['7','8'], ['8','9'] ],
	'USE' : [ ['1','7'], ['7','a'] ],
	'VICTORY' : [ ['0','6'], ['0','9'], ['3','6'], ['3','9'] ],
	'WANT' : [ ['3','7'], ['3','8'], ['4','8'] ],
	'WE' : [ ['3','6'], ['6','9'] ],
	'US' : [ ['3','6'], ['6','9'] ],
	'WEAK' : [ ['5','9'], ['6','7'], ['6','9'] ],
	'WORTH' : [ ['1','7'], ['5','8'], ['7','a'], ['8','a'] ],
	'XM' : [ ['6','7'], ['6','9'], ['7','a'], ['8','9'], ['8','a'] ],
	'YOU' : [ ['0','7'], ['0','8'], ['7','8'] ],
	'YOUR' : [ ['0','7'], ['0','8'], ['7','8'] ],
	'OTHER' : [ ['0','7'], ['0','8'], ['7','8'] ],
	' ' : []
	}

#mapping from portal level to number of glyphs
#0-based (Tecthulhu returns 0 for neutral portals)
glyphcount = [ 1,1,2,3,3,3,4,4,5 ]

#rearrange arc so nodes appear in ascending order
def sort_pair(a):
	if a[0] > a[1]:
		return [a[1],a[0]]
	return [a[0],a[1]]

def glyph_match(target,result):
	#check every required arc was drawn
	for arc in target:
		if arc not in result:
			if debug:
				print("{} undrawn".format(arc))
			return False
	#...and that there was nothing else
	for arc in result:
		if arc not in target:
			if debug:
				print("{} superfluous".format(arc))
			return False
	return True

#list of surfaces
#screen: actual display that flip() redraws
#counter: indicates glyph numbers: current and total
#glyph: where the nodes and arcs appear (TODO: split up more)
#halo: highlight the currently-pressed nodes
#kbhelp: optional key indicators, for debug mode
#rbox: results page; individual text surfaces get blitted to it


#use current display size to calculate node positions
def init_nodes(width, height):
	global node_pos
	global spotsize, fontheight
	global centre_x, centre_y
	global kbhelp, glyphsurf, countsurf, halo

	glyphsurf = pygame.Surface((width,height),flags=pygame.SRCALPHA)
	countsurf = pygame.Surface((width,height),flags=pygame.SRCALPHA)
	halo = pygame.Surface((width,height),flags=pygame.SRCALPHA)

	# leave border big enough for spot to overflow edge of hexagon
	unit = 10 * height/22
	spotsize = int(unit/20)

	# sides of half-triangle
	dx = unit * 0.866 # sin 60
	dy = unit/2

	centre_x = width/2
	centre_y = height/2

	#suitably sized boxes for results
	fontheight = height/8

	node_pos = {
		'0': [int(centre_x), int(centre_y - unit )],
		'1': [int(centre_x + dx), int(centre_y - dy )],
		'2': [int(centre_x + dx), int(centre_y + dy )],
		'3': [int(centre_x), int(centre_y + unit )],
		'4': [int(centre_x - dx), int(centre_y + dy )],
		'5': [int(centre_x - dx), int(centre_y - dy )],
		'6': [int(centre_x + dx/2), int(centre_y - dy/2 )],
		'7': [int(centre_x + dx/2), int(centre_y + dy/2 )],
		'8': [int(centre_x - dx/2), int(centre_y + dy/2 )],
		'9': [int(centre_x - dx/2), int(centre_y - dy/2 )],
		'a': [int(centre_x), int(centre_y )]
	}

	#show the glyph names to help keyboard users
	if showkeys:
		kbhelp = pygame.Surface((width,height),flags=pygame.SRCALPHA)
		helpfont = pygame.font.Font(None,int(spotsize*1.5))
		for k,p in node_pos.items():
			label = helpfont.render(k,True,right)
			kbhelp.blit(label,(p[0]+spotsize,p[1]))

	clearglyph()

#list of arcs in the current glyph
arcs = []

#list of glyphs in entered sequence
sequence = []

#timestamps of start and finish
times = [0]*5

#list of currently-pressed nodes
pressed = {}

def refresh():
	#clear the canvas
	surface.lock()
	surface.fill((0,0,0))
	surface.unlock()

	#draw each layer at a time
	surface.blit(countsurf,(0,0))
	surface.blit(glyphsurf,(0,0))
	surface.blit(halo,(0,0))

	if showkeys:
		surface.blit(kbhelp,(0,0))

	pygame.display.flip()

def progress(current):
	countsurf.lock()
	countsurf.fill((0,0,0,0))

	#current = 0: yet to start
	#current = n+1 : all done

	if current and current<=needed:
		#start at bottom and work round clockwise
		#generate a polygon approximating the pie slice

		#how smooth to draw the outside (needs to be multiple of 60)
		circlepoints = 360

		a1 = int((current-1) * circlepoints/needed)
		a2 = int(current * circlepoints/needed)

		r = centre_y*2/3
		if debug:
			print("sector {} to {}".format(a1,a2) )

		#one at centre
		polygon = [ (centre_x,centre_y) ]

		for angle in range(a1,a2+1):
			x=centre_x - int(r*math.sin (math.pi * 2 * angle/circlepoints) )
			y=centre_y + int(r*math.cos (math.pi * 2 * angle/circlepoints) )
			polygon.append( (x,y) )

		pygame.draw.polygon( countsurf, (0,64,64), polygon, 3)
		pygame.draw.polygon( countsurf, (0,32,32), polygon)

	countsurf.unlock()

#draw a halo around each pressed node
def haloes():
	#refresh and start over
	halo.lock()
	halo.fill((0,0,0,0))

	rgba = (255,255,255)

	#ring needs to go around the node; circle+width makes lots of hoops,
	#smoother fill by drawing a big circle then erasing a smaller one
	outer = int(spotsize*2.5)
	inner = int(spotsize*1.25)

	for p in pressed.values():
		pygame.draw.circle(halo, rgba, node_pos[p], outer, 0)
		pygame.draw.circle(halo, (0,0,0,0), node_pos[p], inner, 0)
	halo.unlock()

def clearglyph():
	global surface
	glyphsurf.lock()
	glyphsurf.fill((0,0,0,0))
	w = (255,255,255)
	for k,n in node_pos.items():
		pygame.draw.circle(glyphsurf, w, n, spotsize, 1)
	glyphsurf.unlock()
	refresh()

def light_node(node,rgba):
	glyphsurf.lock()
	pygame.draw.circle(glyphsurf, rgba, node_pos[node], spotsize, 0)
	glyphsurf.unlock()

def light_arc(start,end,rgba):
	glyphsurf.lock()
	pygame.draw.line(glyphsurf, rgba, node_pos[start], node_pos[end], spotsize)
	glyphsurf.unlock()
	
def drawglyph(arclist, rgba):
	#erase glyph surface first
	clearglyph()
	#draw every arc, and highlight every node hit
	for a in arclist:
		light_arc(a[0], a[1], rgba)
		light_node(a[0],rgba)
		light_node(a[1],rgba)
		
def input(e):
	global pressed, arcs, sequence

	glyphsdone = len(sequence)

	if e.type == pygame.KEYUP:
		# remove key from pressed list
		key = e.key
		if key in pressed:
			name = pressed[key]
			del pressed[key]
			haloes()
		else:
			#key wasn't for a (pressed) node, ignore
			return
		#if list now empty, end glyph
		if not pressed:
			times[glyphsdone][1] = pygame.time.get_ticks()
			sequence.append(arcs)
			glyphsdone = len(sequence)
			arcs = []
			clearglyph()
			#tell user which one they're about to start
			if glyphsdone < needed:
				progress(glyphsdone+1)
	if e.type == pygame.KEYDOWN:
		key = e.key

		if key == pygame.K_BACKSPACE:
			if pressed:
				#mid-glyph, reset it
				if debug:
					print("abandoning current glyph")
				pressed = {}
				arcs = []
			elif sequence:
				#between glyphs, undo previous
				if debug:
					print("abandoning previous glyph")
				del sequence[-1]
				glyphsdone = len(sequence)
				progress(glyphsdone+1)
			clearglyph()
			haloes()
			refresh()
			return

		# only allow two keys at a time
		if len(pressed) == 2:
			return

		name = e.unicode
		if name not in node_pos:
			#key not a node
			if debug:
				print("ignoring key {}".format(key))
			return
		# add to currently-pressed list
		pressed[key] = name
		light_node(name,beige)
		haloes()

		#new glyph, start timer
		if len(pressed) == 1:
			times[glyphsdone] = [ pygame.time.get_ticks() , 0 ]

		# create arc to any other pressed nodes
		for k,src in pressed.items():
			if src==name:
				continue
			else:
				#add the arc to the list
				arcs.append(sort_pair([src,name]))
				light_arc(src,name,beige)
	refresh()

def read_options():
	global requested, level, debug, showkeys, url
	requested = 0
	level = None
	url = ''
	debug = False
	showkeys = False
	opts, args = getopt.getopt(sys.argv[1:],"g:kl:u:v")
	for o,a in opts:
		if o == '-g':
			requested=int(a)
		elif o == '-k':
			showkeys=True
		if o == '-l':
			level=int(a)
		elif o == '-u':
			url=a
		elif o == '-v':
			debug=True

def main():
	global surface, needed, requested, level
	pygame.init()

	pygame.display.set_caption("Glyph Hack")

	read_options()

	screen = pygame.display.set_mode((sc_width,sc_height))
	surface = screen

	init_nodes(sc_width, sc_height)

	waiting = True
	#await start signal (or screen resize)
	pygame.event.set_allowed((pygame.QUIT, pygame.KEYDOWN, pygame.VIDEORESIZE))
	while waiting:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.VIDEORESIZE:
				screen = pygame.display.set_mode((event.size))
				init_nodes(event.w, event.h)
			if event.type == pygame.KEYDOWN:
				#start when pad pressed
				if event.unicode in node_pos:
					waiting = False
		pygame.time.wait(33)

	if url:
		if debug:
			print("querying Tecthulhu...")
		r = requests.get(url)
		if r.status_code != 200:
			print("Error {} retrieving url {}".format(r.status_code,url))
			quit()
		j = r.json()
		level = j['result']['level']
		if debug:
			print("portal level {}".format(level))
	if level is not None:
		if 0<=level<=8:
			requested = glyphcount[level]
		else:
			print("Unexpected portal level {}".format(level))
			quit()
	if not requested:
		requested = random.randint(1,5)
	target_list = sequence_dicts[requested]
	target_phrase = target_list[random.randrange(len(target_list))]

	needed = len(target_phrase)

	#show glyphs
	for i in range(0,needed):
		glyphname=target_phrase[i]
		arclist = glyph_dict[glyphname]
		drawglyph(arclist, beige)
		progress(i+1)
		refresh()
		pygame.event.pump()
		pygame.time.wait(300)

	progress(0)
	clearglyph()
	if showkeys:
		surface.blit(kbhelp,(0,0))

	#ignore anything entered during animation

	pygame.event.clear((pygame.KEYDOWN,pygame.KEYUP))
	#read user input
	pygame.event.set_allowed((pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP))
	glyphing = True
	progress(1)
	while glyphing:
		refresh()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
				input(event)
		
		if len(sequence) == needed:
			glyphing = False
		pygame.time.wait(33)

	if debug:
		print("checking results")

	rfont = pygame.font.Font(None,int(fontheight))

	#check how much space the results will take
	rwidth=0
	twidth=0
	rheight=0
	for n in range(0,needed):
		#first column: glyph name
		name = target_phrase[n]
		box = rfont.size(name)
		if rwidth < box[0]:
			rwidth=box[0]

		#second column: times (when correct)
		ms = float(times[n][1] - times[n][0])/1000
		tbox = rfont.size("  {:.2f}s".format(ms))
		if twidth < tbox[0]:
			twidth=tbox[0]

		#vertically
		if box[1] > tbox[1]:
			rheight += box[1]
		else:
			rheight += tbox[1]

	#now make a big enough box and write each line into it
	rbox = pygame.Surface((rwidth+twidth,rheight))
	rbox.fill((0,0,0))
	ry = 0
	for n in range(0,needed):
		name = target_phrase[n]
		target_arcs = glyph_dict[name]
		if glyph_match(target_arcs, sequence[n]):
			ms = float(times[n][1] - times[n][0])/1000
			if debug:
				print("{} : correct, {:.2f}s".format(name,ms))
			rcol = right
		else:
			ms = 0
			if debug:
				print("{} : wrong".format(name))
			rcol = wrong
		rline = rfont.render(name,True,rcol)
		rbox.blit(rline, (0, ry) )
		#display times next to correct glyphs
		if ms:
			tline=rfont.render("  {:.2f}s".format(ms),True,rcol)
			rbox.blit(tline, (rwidth,ry))
		ry += rline.get_size()[1]

	surface.lock()
	surface.fill((0,0,0))
	surface.unlock()
	surface.blit(rbox, (int(centre_x - (rwidth+twidth)/2), int(centre_y - rheight/2)) )
	pygame.display.flip()
	pygame.event.pump()

	pygame.time.wait(2000)


if __name__ == '__main__':
	main()
