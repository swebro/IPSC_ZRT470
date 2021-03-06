#
# IPSC_ZRT470
# Copyright (C) 2018 Kristoffer Forss
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import config
import ZRT470

conf = Config()

if conf.rxFreq == conf.txFreq:
    rx = ZRT470(conf,'s')
    tx = rx
    rx.init()
else:
    rx = ZRT470(conf,'rx')
    tx = ZRT470(conf,'tx')
    rx.init()
    tx.init()
    
    
sd
