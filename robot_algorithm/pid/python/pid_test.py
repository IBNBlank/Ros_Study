# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-02-21 19:44:50
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-02-21 20:59:17


import incremental_pid
import locational_pid

import matplotlib.pyplot as plt


def init_parameter(inc, loc, actual=0., expect=100.):
	inc.sensor_actual(actual)
	inc.set_expect(expect)

	loc.sensor_actual(actual)
	loc.set_expect(expect)


def test(inc, loc, num, actual=0., expect=100.):
	inc_data = [actual]
	loc_data = [actual]
	exp_data = [expect]
	nums = [0]

	init_parameter(inc, loc, actual, expect)

	for i in range(1, num+1):
		inc_data.append(inc.pid_step())
		loc_data.append(loc.pid_step())
		exp_data.append(expect)
		nums.append(i)

	plt.plot(nums, exp_data, "g--", label="Expect")
	plt.plot(nums, inc_data, label="Incremental Pid")
	plt.plot(nums, loc_data, label="Locational Pid")
	plt.legend()
	plt.show()


if __name__ == '__main__':
	inc = incremental_pid.IncrementalPID(kp=.1, ki=.2, kd=0.3)
	loc = locational_pid.LocationalPID(kp=.3, ki=.2, kd=0.1)

	test(inc, loc, 200)