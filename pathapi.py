#!/usr/bin/env python
#coding:utf8
import re

def project(path):
	"""
	경로를 넣으면 project 이름을 반환한다.
	"""
	p = re.findall('/project/(\w+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 project 정보를 가지고 올 수 없습니다."
	return p[0], None

def seq(path):
	"""
	경로를 넣으면 seq 이름을 반환한다.
	"""
	p = re.findall('/shot/(\w+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 seq 정보를 가지고 올 수 없습니다."
	return p[0], None

def shot(path):
	"""
	경로를 넣으면 shot 이름을 반환한다.
	"""
	p = re.findall('/shot/\w+/(\w+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 shot 정보를 가지고 올 수 없습니다."
	return p[0], None

def task(path):
	"""
	경로를 넣으면 task 이름을 반환한다.
	"""
	p = re.findall('/shot/\w+/\w+/(\w+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 task 정보를 가지고 올 수 없습니다."
	return p[0], None

def ver(path):
	"""
	경로를 넣으면 version 숫자를 반환한다.
	"""
	p = re.findall('_v(\w+)', path.replace("\\", "/"))
	if len(p) != 1:
		return -1, "경로에서 version 정보를 가지고 올 수 없습니다."
	return int(p[0]), None

def seqNum(path):
	"""
	경로를 넣으면 seq Number를 반환한다.
	"""
	p = re.findall('\.(\w+)\.', path.replace("\\", "/"))
	if len(p) != 1:
		return -1, "경로에서 seq Number 정보를 가지고 올 수 없습니다."
	return int(p[0]), None
	
