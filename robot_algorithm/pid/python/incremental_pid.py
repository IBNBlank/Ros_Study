# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-02-21 19:14:48
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-02-21 20:52:32


class IncrementalPID(object):

	def __init__(self, kp=0., ki=0., kd=0., actual=0., expect=0.):
		self.__kp = kp
		self.__ki = ki
		self.__kd = kd

		self.__error = [0., 0.]

		self.__actual = actual
		self.__expect = expect


	def sensor_actual(self, actual):
		self.__actual = actual


	def set_expect(self, expect):
		self.__expect = expect


	def pid_step(self):
		error = self.__expect - self.__actual

		increase = ( self.__kp * (error-self.__error[1])
			+ self.__ki * error
			+ self.__kd * (error-2*self.__error[1]+self.__error[0]) )
		self.__actual += increase

		self.__error.pop(0)
		self.__error.append(error)

		return self.__actual