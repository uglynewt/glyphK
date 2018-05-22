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
		 [ 'CLEAR', 'YOUR', 'MIND', 'CREATIVITY', 'GROW'],
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
	'ABANDON' : [ [1,6], [3,4], [4,8], [6,10], [8,10] ],
	'ADAPT' : [ [5,8], [7,10], [8,10] ],
	'ADVANCE' : [ [0,9], [4,9] ],
	'AFTER' : [ [1,2], [1,6], [2,7], [6,10], [7,10] ],
	'AGAIN' : [ [4,9], [6,7], [6,10], [8,9], [8,10] ],
	'REPEAT' : [ [4,9], [6,7], [6,10], [8,9], [8,10] ],
	'ALL' : [ [0,1], [0,5], [1,2], [2,3], [3,4], [4,5] ],
	'ANSWER' : [ [6,7], [6,9], [7,10] ],
	'ATTACK' : [ [0,6], [0,9], [2,6], [4,9] ],
	'WAR' : [ [0,6], [0,9], [2,6], [4,9] ],
	'AVOID' : [ [0,5], [0,6], [1,6], [1,7] ],
	'BARRIER' : [ [0,10], [2,7], [7,10] ],
	'OBSTACLE' : [ [0,10], [2,7], [7,10] ],
	'BEFORE' : [ [4,5], [4,8], [5,9], [8,10], [9,10] ],
	'BEGIN' : [ [0,8], [3,7], [3,8] ],
	'BEING' : [ [3,7], [3,8], [6,7], [6,9], [8,9] ],
	'HUMAN' : [ [3,7], [3,8], [6,7], [6,9], [8,9] ],
	'BODY' : [ [6,9], [6,10], [9,10] ],
	'SHELL' : [ [6,9], [6,10], [9,10] ],
	'BREATHE' : [ [1,6], [5,9], [6,10], [9,10] ],
	'LIVE' : [ [1,6], [5,9], [6,10], [9,10] ],
	'CAPTURE' : [ [1,7], [3,4], [4,8], [7,10], [8,10] ],
	'CHANGE' : [ [3,7], [3,10], [8,10] ],
	'MODIFY' : [ [3,7], [3,10], [8,10] ],
	'CHAOS' : [ [0,1], [0,5], [1,6], [3,8], [4,5], [6,10], [8,10] ],
	'DISORDER' : [ [0,1], [0,5], [1,6], [3,8], [4,5], [6,10], [8,10] ],
	'CLEAR' : [ [0,10], [3,10] ],
	'CLOSE ALL' : [ [0,1], [0,5], [0,10], [1,2], [2,3], [3,4], [3,10], [4,5] ],
	'CLEAR ALL' : [ [0,1], [0,5], [0,10], [1,2], [2,3], [3,4], [3,10], [4,5] ],
	'CLEARALL' : [ [0,1], [0,5], [0,10], [1,2], [2,3], [3,4], [3,10], [4,5] ],
	'COMPLEX' : [ [6,9], [8,10], [9,10] ],
	'CONFLICT' : [ [2,6], [4,9], [6,7], [7,8], [8,9] ],
	'CONSEQUENCE' : [ [2,7], [5,9], [7,8], [8,9] ],
	'CONTEMPLATE' : [ [0,1], [1,2], [2,3], [3,8], [6,10], [8,9], [9,10] ],
	'COURAGE' : [ [4,9], [7,8], [8,9] ],
	'CREATE' : [ [1,6], [4,8], [6,10], [8,10] ],
	'CREATION' : [ [1,6], [4,8], [6,10], [8,10] ],
	'CREATIVITY' : [ [1,2], [1,6], [2,7], [4,5], [4,8], [5,9], [7,10], [9,10] ],
	'IDEA' : [ [1,2], [1,6], [2,7], [4,5], [4,8], [5,9], [7,10], [9,10] ],
	'THOUGHT' : [ [1,2], [1,6], [2,7], [4,5], [4,8], [5,9], [7,10], [9,10] ],
	'DANGER' : [ [0,9], [3,10], [9,10] ],
	'DATA' : [ [0,6], [3,8], [6,10], [8,10] ],
	'SIGNAL' : [ [0,6], [3,8], [6,10], [8,10] ],
	'DEFEND' : [ [1,7], [3,7], [3,8], [5,8] ],
	'DESTINY' : [ [3,8], [6,7], [6,10], [7,8], [9,10] ],
	'DESTINATION' : [ [1,2], [2,3] ],
	'DESTROY' : [ [2,7], [5,9], [7,10], [9,10] ],
	'DESTRUCTION' : [ [2,7], [5,9], [7,10], [9,10] ],
	'DETERIORATE' : [ [4,8], [8,10], [9,10] ],
	'ERODE' : [ [4,8], [8,10], [9,10] ],
	'EASY' : [ [3,8], [6,10], [8,10] ],
	'DIE' : [ [2,7], [4,8], [7,10], [8,10] ],
	'DEATH' : [ [2,7], [4,8], [7,10], [8,10] ],
	'DIFFICULT' : [ [1,6], [6,7], [7,10], [8,10] ],
	'DISCOVER' : [ [1,2], [2,3], [3,4] ],
	'DISTANCE' : [ [0,5], [4,5] ],
	'OUTSIDE' : [ [0,5], [4,5] ],
	'END' : [ [0,1], [0,10], [1,7], [3,7], [3,10] ],
	'CLOSE' : [ [0,1], [0,10], [1,7], [3,7], [3,10] ],
	'ENLIGHTENED' : [ [0,1], [0,9], [1,2], [2,3], [6,9], [6,10], [9,10] ],
	'ENLIGHTENMENT' : [ [0,1], [0,9], [1,2], [2,3], [6,9], [6,10], [9,10] ],
	'EQUAL' : [ [6,7], [6,9], [8,9] ],
	'ESCAPE' : [ [0,1], [1,6], [6,9], [8,9] ],
	'EVOLUTION' : [ [0,10], [8,9], [9,10] ],
	'PROGRESS' : [ [0,10], [8,9], [9,10] ],
	'SUCCESS' : [ [0,10], [8,9], [9,10] ],
	'FAILURE' : [ [0,10], [6,7], [6,10] ],
	'FEAR' : [ [1,7], [6,7], [6,9] ],
	'FOLLOW' : [ [0,6], [1,2], [1,6] ],
	'FORGET' : [ [4,8] ],
	'FUTURE' : [ [1,6], [2,7], [6,7] ],
	'GAIN' : [ [5,8] ],
	'GOVERNMENT' : [ [1,6], [5,9], [6,7], [7,8], [8,9] ],
	'CITY' : [ [1,6], [5,9], [6,7], [7,8], [8,9] ],
	'CIVILIZATION' : [ [1,6], [5,9], [6,7], [7,8], [8,9] ],
	'STRUCTURE' : [ [1,6], [5,9], [6,7], [7,8], [8,9] ],
	'GROW' : [ [4,9], [8,9] ],
	'HARM' : [ [0,6], [0,9], [2,7], [6,10], [7,10], [9,10] ],
	'HARMONY' : [ [0,6], [0,9], [3,7], [3,8], [6,10], [7,10], [8,10], [9,10] ],
	'PEACE' : [ [0,6], [0,9], [3,7], [3,8], [6,10], [7,10], [8,10], [9,10] ],
	'HAVE' : [ [3,8], [7,10], [8,10] ],
	'HELP' : [ [5,9], [7,8], [8,10], [9,10] ],
	'HIDE' : [ [1,6], [1,7], [6,9], [7,8] ],
	'I' : [ [3,6], [3,9], [6,9] ],
	'ME' : [ [3,6], [3,9], [6,9] ],
	'IGNORE' : [ [2,7] ],
	'IMPERFECT' : [ [6,8], [6,10], [8,9], [8,10], [9,10] ],
	'IMPROVE' : [ [1,6], [6,10], [7,10] ],
	'IMPURE' : [ [3,10], [8,9], [8,10], [9,10] ],
	'INTELLIGENCE' : [ [1,6], [4,8], [6,10], [8,9], [9,10] ],
	'INTERRUPT' : [ [0,10], [3,10], [4,5], [4,8], [5,9], [8,10], [9,10] ],
	'JOURNEY' : [ [1,6], [3,4], [4,5], [5,9], [6,10], [9,10] ],
	'KNOWLEDGE' : [ [3,6], [3,9], [6,10], [9,10] ],
	'LEAD' : [ [0,5], [3,8], [4,5], [4,8] ],
	'LEGACY' : [ [0,1], [0,5], [1,6], [2,7], [4,8], [5,9], [6,7], [8,9] ],
	'LESS' : [ [6,10], [9,10] ],
	'LIBERATE' : [ [0,1], [1,6], [4,9], [6,10], [9,10] ],
	'LIE' : [ [6,7], [6,10], [7,10], [8,9], [9,10] ],
	'LIVE AGAIN' : [ [1,6], [4,9], [6,10], [8,9], [8,10] ],
	'REINCARNATE' : [ [1,6], [4,9], [6,10], [8,9], [8,10] ],
	'LOSE' : [ [1,7] ],
	'MESSAGE' : [ [1,7], [4,9], [7,10], [9,10] ],
	'MIND' : [ [3,8], [3,10], [8,9], [9,10] ],
	'MORE' : [ [7,10], [8,10] ],
	'MYSTERY' : [ [0,6], [0,9], [5,9], [6,9], [8,9] ],
	'N\'ZEER' : [ [0,6], [0,9], [0,10], [3,10], [6,10], [9,10] ],
	'NATURE' : [ [2,7], [4,8], [6,7], [6,9], [8,9] ],
	'NEW' : [ [2,7], [6,7] ],
	'NOT' : [ [6,7], [6,9] ],
	'INSIDE' : [ [6,7], [6,9] ],
	'NOURISH' : [ [3,4], [3,10], [4,8], [8,10] ],
	'OLD' : [ [5,9], [8,9] ],
	'OPEN' : [ [3,7], [3,8], [7,8] ],
	'ACCEPT' : [ [3,7], [3,8], [7,8] ],
	'OPEN ALL' : [ [0,1], [0,5], [1,2], [2,3], [3,4], [3,7], [3,8], [4,5], [7,8] ],
	'OPENALL' : [ [0,1], [0,5], [1,2], [2,3], [3,4], [3,7], [3,8], [4,5], [7,8] ],
	'PORTAL' : [ [1,2], [1,6], [2,7], [4,5], [4,8], [5,9], [6,9], [7,8] ],
	'PAST' : [ [4,8], [5,9], [8,9] ],
	'PATH' : [ [0,10], [4,8], [8,10] ],
	'PERFECTION' : [ [0,10], [2,3], [2,7], [3,4], [4,8], [7,10], [8,10] ],
	'BALANCE' : [ [0,10], [2,3], [2,7], [3,4], [4,8], [7,10], [8,10] ],
	'PERSPECTIVE' : [ [0,6], [0,9], [2,7], [4,8], [6,10], [7,10], [8,10], [9,10] ],
	'POTENTIAL' : [ [0,10], [1,2], [2,7], [7,10] ],
	'PRESENCE' : [ [3,7], [3,8], [6,7], [6,10], [7,8], [8,9], [9,10] ],
	'PRESENT' : [ [6,7], [7,8], [8,9] ],
	'NOW' : [ [6,7], [7,8], [8,9] ],
	'PURE' : [ [0,10], [6,7], [6,10], [7,10] ],
	'PURSUE' : [ [0,6], [0,9], [5,9] ],
	'CHASE' : [ [0,10], [4,8], [8,9], [9,10] ],
	'QUESTION' : [ [0,6], [6,9], [8,9] ],
	'REACT' : [ [2,7], [6,9], [7,10], [9,10] ],
	'REBEL' : [ [1,2], [1,6], [5,8], [6,10], [8,10] ],
	'RECHARGE' : [ [0,5], [0,10], [5,9], [9,10] ],
	'REPAIR' : [ [0,5], [0,10], [5,9], [9,10] ],
	'REDUCE' : [ [2,6], [6,7] ],
	'RESIST' : [ [0,9], [0,10], [3,8], [3,10], [6,9] ],
	'RESISTANCE' : [ [0,9], [0,10], [3,8], [3,10], [6,9] ],
	'STRUGGLE' : [ [0,9], [0,10], [3,8], [3,10], [6,9] ],
	'RESTRAINT' : [ [2,3], [2,7], [5,9], [7,10], [9,10] ],
	'RETREAT' : [ [0,6], [2,6] ],
	'SAFETY' : [ [2,6], [4,9], [6,9] ],
	'SAVE' : [ [1,7], [7,10], [8,10] ],
	'SEE' : [ [0,9] ],
	'SEEK' : [ [6,9], [6,10], [7,8], [8,9] ],
	'SEARCH' : [ [6,9], [6,10], [7,8], [8,9] ],
	'SELF' : [ [2,3], [3,4] ],
	'INDIVIDUAL' : [ [2,3], [3,4] ],
	'SEPARATE' : [ [2,7], [5,9], [6,7], [6,10], [8,9], [8,10] ],
	'SHAPERS' : [ [0,6], [0,9], [2,7], [4,8], [6,7], [8,9] ],
	'COLLECTIVE' : [ [0,6], [0,9], [2,7], [4,8], [6,7], [8,9] ],
	'SHARE' : [ [2,7], [3,4], [4,8], [7,8] ],
	'SIMPLE' : [ [7,8] ],
	'SOUL' : [ [3,7], [3,10], [6,7], [6,10] ],
	'STABILITY' : [ [2,7], [4,8], [7,8] ],
	'STAY' : [ [2,7], [4,8], [7,8] ],
	'STRONG' : [ [6,7], [6,9], [7,8], [8,9] ],
	'SUSTAIN' : [ [0,10], [1,2], [1,6], [2,7], [3,10], [6,10], [7,10] ],
	'SUSTAIN ALL' : [ [0,1], [0,5], [0,10], [1,2], [1,6], [2,3], [2,7], [3,4], [3,10], [4,5], [6,10], [7,10] ],
	'TECHNOLOGY' : [ [1,6], [2,7], [6,10], [7,10], [8,9], [8,10], [9,10] ],
	'THEM' : [ [0,8], [7,8] ],
	'TOGETHER' : [ [4,8], [6,9], [6,10], [8,10], [9,10] ],
	'TRUTH' : [ [6,7], [6,10], [7,10], [8,9], [8,10], [9,10] ],
	'UNBOUNDED' : [ [0,1], [0,5], [1,7], [2,3], [3,4], [4,5], [6,9], [6,10], [7,8], [8,9] ],
	'USE' : [ [1,7], [7,10] ],
	'VICTORY' : [ [0,6], [0,9], [3,6], [3,9] ],
	'WANT' : [ [3,7], [3,8], [4,8] ],
	'WE' : [ [3,6], [6,9] ],
	'US' : [ [3,6], [6,9] ],
	'WEAK' : [ [5,9], [6,7], [6,9] ],
	'WORTH' : [ [1,7], [5,8], [7,10], [8,10] ],
	'XM' : [ [6,7], [6,9], [7,10], [8,9], [8,10] ],
	'YOU' : [ [0,7], [0,8], [7,8] ],
	'YOUR' : [ [0,7], [0,8], [7,8] ],
	'OTHER' : [ [0,7], [0,8], [7,8] ],
	' ' : []
	}

#mapping from portal level to number of glyphs
#0-based (Tecthulhu returns 0 for neutral portals)
glyphcount = [ 1,1,2,3,3,3,4,4,5 ]

#keyboard mapping for node numbers
# must match the ".unicode" member of keydown events
# shown on screen by kbhelp
node_keys = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a' ]


#list of arcs in the current glyph
arcs = []

#dictionary of currently-pressed nodes
#key = "key" member of events (keydown and keyup)
#value = node number; index into node_pos
pressed = {}

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

def init_sounds():
	global press,release
	pygame.mixer.init()

	press = pygame.mixer.Sound("sounds/down.wav")
	release = pygame.mixer.Sound("sounds/up.wav")

#list of surfaces to be combined during refresh()
#screen: actual display that flip() redraws
#counter: indicates glyph numbers: current and total
#spots: the circles for each node
#glyph: where the lines of the glyph appear
#halo: highlight the currently-pressed nodes
#kbhelp: optional key indicators, for debug mode
#msg: messages ("incoming glyph")

#other surfaces
#rbox: results page; individual text surfaces get blitted to it


#calculate node positions to fit within the provided surface
def init_nodes(surf, np):
	width,height = surf.get_size()

	if width > height:
		unit = 10 * height/22
	else:
		unit = 10 * width/22

	cx = width/2
	cy = height/2

	# sides of half-triangle
	dx = unit * 0.866 # sin 60
	dy = unit/2

	np[0] = (int(cx), int(cy - unit ))
	np[1] = (int(cx + dx), int(cy - dy ))
	np[2] = (int(cx + dx), int(cy + dy ))
	np[3] = (int(cx), int(cy + unit ))
	np[4] = (int(cx - dx), int(cy + dy ))
	np[5] = (int(cx - dx), int(cy - dy ))
	np[6] = (int(cx + dx/2), int(cy - dy/2 ))
	np[7] = (int(cx + dx/2), int(cy + dy/2 ))
	np[8] = (int(cx - dx/2), int(cy + dy/2 ))
	np[9] = (int(cx - dx/2), int(cy - dy/2 ))
	np[10] = (int(cx), int(cy ))

#hexagon to go round the nodes
def init_hex(surf, hp):
	width,height = surf.get_size()

	if width > height:
		unit = height/2
	else:
		unit = width/2

	cx = width/2
	cy = height/2

	# sides of half-triangle
	dx = unit * 0.866 # sin 60
	dy = unit/2

	hp[0] = (int(cx), int(cy - unit ))
	hp[1] = (int(cx + dx), int(cy - dy ))
	hp[2] = (int(cx + dx), int(cy + dy ))
	hp[3] = (int(cx), int(cy + unit ))
	hp[4] = (int(cx - dx), int(cy + dy ))
	hp[5] = (int(cx - dx), int(cy - dy ))

def init_screen(width, height):
	global node_pos
	global spotsize, fontheight
	global centre_x, centre_y
	global kbhelp, spotsurf, glyphsurf, countsurf, halo, msgsurf

	glyphsurf = pygame.Surface((width,height),flags=pygame.SRCALPHA)
	spotsurf = pygame.Surface((width,height),flags=pygame.SRCALPHA)
	countsurf = pygame.Surface((width,height),flags=pygame.SRCALPHA)
	halo = pygame.Surface((width,height),flags=pygame.SRCALPHA)
	msgsurf = pygame.Surface((width,height),flags=pygame.SRCALPHA)

	centre_x = width/2
	centre_y = height/2

	#suitably sized boxes for results
	fontheight = height/8

	spotsize = int(height/44)

	node_pos = [0]*11
	init_nodes(glyphsurf, node_pos)

	#draw the spots
	spotsurf.lock()
	spotsurf.fill((0,0,0,0))
	w = (255,255,255)
	for n in node_pos:
		pygame.draw.circle(spotsurf, w, n, spotsize, 1)
	spotsurf.unlock()

	#show the glyph names to help keyboard users
	if showkeys:
		kbhelp = pygame.Surface((width,height),flags=pygame.SRCALPHA)
		helpfont = pygame.font.Font(None,int(spotsize*1.5))
		for k in range(11):
			label = helpfont.render(node_keys[k],True,right)
			kbhelp.blit(label,(node_pos[k][0]+spotsize,node_pos[k][1]))

def refresh():
	#clear the canvas
	surface.lock()
	surface.fill((0,0,0))
	surface.unlock()

	#draw each layer at a time
	surface.blit(countsurf,(0,0))
	surface.blit(spotsurf,(0,0))
	surface.blit(glyphsurf,(0,0))
	surface.blit(halo,(0,0))
	surface.blit(msgsurf,(0,0))

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

#takes string and colour; returns a box holding it
#with black bg and a frame
def msgbox(string,rgba):
	mfont = pygame.font.Font(None,int(fontheight))
	ibox = mfont.render(string,True,rgba)
	ix,iy = ibox.get_size()
	box = pygame.Surface((ix+6,iy+6))
	box.fill((0,0,0))
	box.blit(ibox,(3,3))
	pygame.draw.rect(box,rgba,(0,0,ix+6,iy+6),3)

	return box

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
	glyphsurf.lock()
	glyphsurf.fill((0,0,0,0))
	glyphsurf.unlock()

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

def miniglyph(arclist, rgba, surface, np, border):
	surface.lock()
	surface.fill((0,0,0,0))
	#hexagon outline
	pygame.draw.polygon( surface, (rgba[0]/2, rgba[1]/2, rgba[2]/2), border, 4)
	#hexagon fill
	pygame.draw.polygon( surface, (rgba[0]/4, rgba[1]/4, rgba[2]/4), border)
	for a in arclist:
		pygame.draw.line(surface, rgba, np[a[0]], np[a[1]], 4)
	surface.unlock()

def input(e):
	global pressed, arcs, sequence

	glyphsdone = len(sequence)

	if e.type == pygame.KEYUP:
		# remove key from pressed list
		key = e.key
		if key in pressed:
			del pressed[key]
			haloes()
			release.play()
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

		sym = e.unicode
		if sym not in node_keys:
			#key not a node
			if debug:
				print("ignoring key {}".format(sym))
			return
		# add to currently-pressed list
		node = node_keys.index(sym)
		pressed[e.key] = node
		light_node(node,beige)
		haloes()
		press.play()

		#new glyph, start timer
		if len(pressed) == 1:
			times[glyphsdone] = [ pygame.time.get_ticks() , 0 ]

		# create arc to any other pressed nodes
		for k,src in pressed.items():
			if src==node:
				continue
			else:
				#add the arc to the list
				arcs.append(sort_pair([src,node]))
				light_arc(src,node,beige)
	refresh()

#simple input mode for testing pad
def padtest():
	pygame.event.set_allowed((pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP, pygame.VIDEORESIZE))
	#render message now, blit it when required
	mbox = msgbox("REDO",(128,128,64))
	mx,my = mbox.get_size()

	while True:
		refresh()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.VIDEORESIZE:
				screen = pygame.display.set_mode((event.size))
				init_screen(event.w, event.h)
			if event.type == pygame.KEYDOWN:
				#start when pad pressed
				if event.unicode in node_keys:
					node = node_keys.index(event.unicode)
					pressed[event.key] = node
					haloes()
				elif event.key == pygame.K_BACKSPACE:
					msgsurf.blit(mbox,(int(centre_x-mx/2),int(centre_y-2*my)))
				press.play()
			if event.type == pygame.KEYUP:
				# remove key from pressed list
				key = event.key
				if key in pressed:
					del pressed[key]
					haloes()
				elif key == pygame.K_BACKSPACE:
					msgsurf.fill((0,0,0,0))
				release.play()
		refresh()
		pygame.time.wait(33)


def usage():
	print("Usage:")
	print("{} <options>".format(sys.argv[0]))
	print("")
	print("	-c       : complex hack")
	print("	-g <num> : set length of glyph sequence")
	print("	-h       : show this message")
	print("	-k       : display key bindings on screen")
	print("	-l <num> : set hack level")
	print("	-p       : pad test mode")
	print("	-s       : simple hack")
	print("	-u <url> : URL to query for portal information")
	print("	-v       : verbose (misc debugging messages)")
	quit()

def read_options():
	global requested, delay, level, debug, showkeys, url, testpad
	requested = 0
	level = None
	url = ''
	debug = False
	showkeys = False
	testpad = False
	delay = 1000
	opts, args = getopt.getopt(sys.argv[1:],"cg:hkl:psu:v")
	for o,a in opts:
		if o == '-g':
			requested=int(a)
		elif o == '-h':
			usage()
		elif o == '-k':
			showkeys=True
		elif o == '-c':
			delay = 300
		elif o == '-p':
			testpad = True
		elif o == '-s':
			delay = 2000
		elif o == '-l':
			level=int(a)
		elif o == '-u':
			url=a
		elif o == '-v':
			debug=True

def gameloop():
	global needed, level
	global sequence, times

	waiting = True
	#await start signal (or screen resize)
	pygame.event.set_allowed((pygame.QUIT, pygame.KEYDOWN, pygame.VIDEORESIZE))
	while waiting:
		refresh()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.VIDEORESIZE:
				screen = pygame.display.set_mode((event.size))
				init_screen(event.w, event.h)
			if event.type == pygame.KEYDOWN:
				#start when pad pressed
				if event.unicode in node_keys:
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
			numglyphs = glyphcount[level]
		else:
			print("Unexpected portal level {}".format(level))
			quit()
	elif requested:
		numglyphs = requested
	else:
		numglyphs = random.randint(1,5)
	target_list = sequence_dicts[numglyphs]
	target_phrase = target_list[random.randrange(len(target_list))]

	needed = numglyphs

	#count user in with "incoming" message
	mbox = msgbox("INCOMING GLYPH SEQUENCE",(128,128,64))
	mx,my = mbox.get_size()

	for i in range(3):
		msgsurf.fill((0,0,0,0))
		msgsurf.blit(mbox, (centre_x - mx/2, centre_y - 2*my) )
		refresh()
		pygame.event.pump()
		pygame.time.wait(int(delay*3/4))

		msgsurf.fill((0,0,0,0))
		refresh()
		pygame.event.pump()
		pygame.time.wait(int(delay*1/4))

	#show glyphs
	for i in range(0,needed):
		glyphname=target_phrase[i]
		arclist = glyph_dict[glyphname]
		drawglyph(arclist, beige)
		progress(i+1)
		refresh()
		pygame.event.pump()
		pygame.time.wait(delay)

	progress(0)
	clearglyph()
	if showkeys:
		surface.blit(kbhelp,(0,0))

	#ignore anything entered during animation

	pygame.event.clear((pygame.KEYDOWN,pygame.KEYUP))
	#read user input
	pygame.event.set_allowed((pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP))
	glyphing = True
	sequence = []
	times = [0]*5
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

	progress(0)

	if debug:
		print("checking results")

	rfont = pygame.font.Font(None,int(fontheight))

	#check how much space the results will take
	rwidth=0
	twidth=0
	rheight=needed*fontheight
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

	#miniature glyph on left
	miniwidth = int(fontheight * 1.4)
	minisurf = pygame.Surface((miniwidth,fontheight))
	mp = [0]*11
	hp = [0]*6
	init_nodes(minisurf,mp)
	init_hex(minisurf,hp)

	#now make a big enough box and write each line into it
	rbox = pygame.Surface((rwidth+twidth+miniwidth,rheight))
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
		miniglyph(target_arcs,rcol, minisurf, mp,hp)
		rbox.blit(minisurf, (0,ry))
		rline = rfont.render(name,True,rcol)
		lineoffset = int( (fontheight - rline.get_height())/2)
		rbox.blit(rline, (miniwidth, ry+lineoffset) )
		#display times next to correct glyphs
		if ms:
			tline=rfont.render("  {:.2f}s".format(ms),True,rcol)
			rbox.blit(tline, (miniwidth+rwidth,ry+lineoffset))
		ry += fontheight

		surface.lock()
		surface.fill((0,0,0))
		surface.unlock()
		surface.blit(rbox, (int(centre_x - (rwidth+twidth+miniwidth)/2), int(centre_y - rheight/2)) )
		pygame.display.flip()
		pygame.event.pump()

		pygame.time.wait(delay)

	pygame.time.wait(2000)


def main():
	global surface

	pygame.mixer.pre_init(22050,-16,1,256)
	pygame.init()

	pygame.display.set_caption("Glyph Hack")

	read_options()

	screen = pygame.display.set_mode((sc_width,sc_height))
	surface = screen

	init_sounds()
	init_screen(sc_width, sc_height)

	if testpad:
		padtest()
		#shouldn't return
		quit()

	while True:
		gameloop()

if __name__ == '__main__':
	main()
