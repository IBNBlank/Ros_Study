# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-02-21 19:19:05
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-02-21 20:47:18


class LocationalPID(object):

	def __init__(self, kp=0., ki=0., kd=0., actual=0., expect=0.):
		self.__kp = kp
		self.__ki = ki
		self.__kd = kd

		self.__last_error = 0.
		self.__integral = 0.

		self.__actual = actual
		self.__expect = expect


	def sensor_actual(self, actual):
		self.__actual = actual


	def set_expect(self, expect):
		self.__expect = expect


	def pid_step(self):
		error = self.__expect - self.__actual
		self.__integral += error

		self.__actual = ( self.__kp * error
			+ self.__ki * self.__integral
			+ self.__kd * (error-self.__last_error) )

		self.__last_error = error

		return self.__actual