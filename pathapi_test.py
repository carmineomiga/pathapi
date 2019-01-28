#!/usr/bin/env python
#coding:utf8
import unittest
from pathapi import *

class Test_path(unittest.TestCase):
	def test_project(self):
		self.assertEqual(project("/project/circle"), ("circle", None))
		self.assertEqual(project("/project/circle/"), ("circle", None))
		self.assertEqual(project("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.1001.nk"), ("circle", None))
		self.assertEqual(project("\\\\10.20.30.40\\project\\circle\\"), ("circle", None))
		self.assertEqual(project("\\\\10.20.30.41\\server1\\project\\circle"), ("circle", None))
		self.assertEqual(project("/server1/project/circle"), ("circle", None))	
		self.assertEqual(project("/server2/project/circle"), ("circle", None))
		self.assertEqual(project("/project/coco"), ("coco", None))
		self.assertEqual(project("/project/coco/"), ("coco", None))

	def test_seq(self):
		self.assertEqual(seq("/project/circle/shot/FOO"), ("FOO", None))
		self.assertEqual(seq("/project/circle/shot/FOO/"), ("FOO", None))
		self.assertEqual(seq("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.1001.nk"), ("FOO", None))
		self.assertEqual(seq("/project/circle/shot/ROO"), ("ROO", None))
		self.assertEqual(seq("/project/circle/shot/ROO/"), ("ROO", None))

	def test_shot(self):
		self.assertEqual(shot("/project/circle/shot/FOO/0010"), ("0010", None))
		self.assertEqual(shot("/project/circle/shot/FOO/0010/"), ("0010", None))
		self.assertEqual(shot("/project/circle/shot/FOO/N1234"), ("N1234", None))
		self.assertEqual(shot("/project/circle/shot/FOO/8977/"), ("8977", None))
		self.assertEqual(shot("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.1001.nk"), ("0010", None))

	def test_task(self):
		self.assertEqual(task("/project/circle/shot/FOO/0010/comp"), ("comp", None))
		self.assertEqual(task("/project/circle/shot/FOO/0010/model"), ("model", None))
		self.assertEqual(task("/project/circle/shot/FOO/0010/render"), ("render", None))
		self.assertEqual(task("/project/circle/shot/FOO/0010/comp/"), ("comp", None))
		self.assertEqual(task("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.1001.nk"), ("comp", None))

	def test_ver(self):
		self.assertEqual(ver("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001"), (1, None))
		self.assertEqual(ver("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001."), (1, None))
		self.assertEqual(ver("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v2488"), (2488, None))
		self.assertEqual(ver("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.1001.nk"), (1, None))

	def test_seqNum(self):
		self.assertEqual(seqNum("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.10011."), (10011, None))
		self.assertEqual(seqNum("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.777765."), (777765, None))
		self.assertEqual(seqNum("/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.1001.nk"), (1001, None))

if __name__ == "__main__":
	unittest.main()
