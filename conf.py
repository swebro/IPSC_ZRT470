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

class Conf:
    """Configuration for IPSC_ZRT470"""
    # Connection configuration
    master = ' '            # IP/domain of master server
    port = ' '              # Port of master server
    passphrase = ' '        # Passphrase given by master server admin
    pingTime = 60           # How often to ping the master server in seconds
    numOfPings = 10         # How many dead pings before calling connection dead
    
    # IPSC configuration
    signature = 'RPTC'      # The IPSC command for configuration
    callsign = ' ' * 8      # 8 Byte ASCII
    rptrId = '00000000'     # 3 Bytes registered DMR-ID for public repeaters,
                                # 4 Bytes for private repeaters, HEX
    rxFreq = '434787500'    # RX frequency in Hz
    txFreq = '434787500'    # TX frequency in Hz
    txPwr = '00'            # TX power in dBm, decimal (00-99)
    CC = '01'               # ColorCode/Systemcode of the repeater (01-15)
    lat = '+00.0000'        # Latitude in ASCII (8 Digits including 4 decimals,
                                # - and decimal elimiter)
    long = '+000.0000'      # Latitude in ASCII (9 Digits including 4 decimals,
                                # - and decimal elimiter)
    height = '000'          # Antenna height over ground level in meters (000-999)
    loc = ' ' * 20          # The nominal location of the repeater. This is a
                                # free form text field. (only ASCII, no special
                                # country specific characters or HTML codes, URLs)
                                # 20 Chars
    desc = ' ' * 20         # Optional information about the repeater. This is
                                # a free form text field. (only ASCII, no 
                                # special country specific characters or 
                                # HTML codes, URLs, no advertisements or 
                                # non-Amateur Radio content)
                                # 20 Chars
    URL = ' ' * 124         # Optional web page for the repeater or group.
                                # This is a free form text field.
                                # (no advertisements or non-Amateur Radio
                                # related links) “http://” not required 
                                # 124 Chars
    sId = ' ' * 40          # Software-ID with version number (no HTML, 
                                # no advertising, only identification
                                # 40 Chars
    pId = ' ' * 40          # Package-ID with version number and platform
                                # (no HTML, no advertising, only identification)
                                # 40 Chars
