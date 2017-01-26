
#
# Copyright 2015-2017 University of Southern California
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
#

"""Volume rendering via two-pass ray-casting.

Sub-modules:

  data: 3D volume image handling

  geometry: 3D volume bounding-box geometry

  render: OpenGL rendering methods

  util: file handling and basic functions

  viewer: a volume viewer user-interface

"""

import util

try:
    import data
    import geometry
    import render
    import viewer
except ImportError, e:
    import sys
    sys.stderr.write("WARNING: %s\n" % e)
