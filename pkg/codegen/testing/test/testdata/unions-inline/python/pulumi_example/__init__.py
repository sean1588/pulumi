# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .example_server import *
from .provider import *
from ._inputs import *
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "example",
  "mod": "index",
  "fqn": "pulumi_example",
  "classes": {
   "example:index:ExampleServer": "ExampleServer"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "example",
  "token": "pulumi:providers:example",
  "fqn": "pulumi_example",
  "class": "Provider"
 }
]
"""
)
