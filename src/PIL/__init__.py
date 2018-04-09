"""Pillow {} (Fork of the Python Imaging Library)

Pillow is the friendly PIL fork by Alex Clark and Contributors.
    https://github.com/python-pillow/Pillow/

It's forked from PIL 1.1.7, released in 2009

Access the version strings, use:
    PIL.PILLOW_VERSION (for this Pillow version)
    PIL.VERSION        (for the old PIL version)

PIL is the Python Imaging Library by Fredrik Lundh and Contributors.
Copyright (c) 1999 by Secret Labs AB.

See the README file for more information.
"""

PILLOW_VERSION = '5.1.0' # this Pillow release
VERSION = '1.1.7' # last PIL release (2009), which Pillow is based on

__doc__ = __doc__.format(PILLOW_VERSION) # include version in docstring
from . import version # uses PILLOW_VERSION defined above
__version__ = PILLOW_VERSION # https://github.com/python-pillow/Pillow/pull/2027

_plugins = ['BlpImagePlugin',
            'BmpImagePlugin',
            'BufrStubImagePlugin',
            'CurImagePlugin',
            'DcxImagePlugin',
            'DdsImagePlugin',
            'EpsImagePlugin',
            'FitsStubImagePlugin',
            'FliImagePlugin',
            'FpxImagePlugin',
            'FtexImagePlugin',
            'GbrImagePlugin',
            'GifImagePlugin',
            'GribStubImagePlugin',
            'Hdf5StubImagePlugin',
            'IcnsImagePlugin',
            'IcoImagePlugin',
            'ImImagePlugin',
            'ImtImagePlugin',
            'IptcImagePlugin',
            'JpegImagePlugin',
            'Jpeg2KImagePlugin',
            'McIdasImagePlugin',
            'MicImagePlugin',
            'MpegImagePlugin',
            'MpoImagePlugin',
            'MspImagePlugin',
            'PalmImagePlugin',
            'PcdImagePlugin',
            'PcxImagePlugin',
            'PdfImagePlugin',
            'PixarImagePlugin',
            'PngImagePlugin',
            'PpmImagePlugin',
            'PsdImagePlugin',
            'SgiImagePlugin',
            'SpiderImagePlugin',
            'SunImagePlugin',
            'TgaImagePlugin',
            'TiffImagePlugin',
            'WebPImagePlugin',
            'WmfImagePlugin',
            'XbmImagePlugin',
            'XpmImagePlugin',
            'XVThumbImagePlugin']
