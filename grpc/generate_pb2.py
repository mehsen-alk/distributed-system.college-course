# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generate.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egenerate.proto\"\"\n\nSumRequest\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"\x17\n\x08SumReply\x12\x0b\n\x03sum\x18\x01 \x01(\t\"\x18\n\x0b\x46\x61\x63tRequest\x12\t\n\x01n\x18\x01 \x01(\x05\"\x19\n\tFactReply\x12\x0c\n\x04\x66\x61\x63t\x18\x01 \x01(\t2S\n\x06summer\x12\"\n\x06SumNum\x12\x0b.SumRequest\x1a\t.SumReply\"\x00\x12%\n\x07\x46\x61\x63tNum\x12\x0c.FactRequest\x1a\n.FactReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SUMREQUEST']._serialized_start=18
  _globals['_SUMREQUEST']._serialized_end=52
  _globals['_SUMREPLY']._serialized_start=54
  _globals['_SUMREPLY']._serialized_end=77
  _globals['_FACTREQUEST']._serialized_start=79
  _globals['_FACTREQUEST']._serialized_end=103
  _globals['_FACTREPLY']._serialized_start=105
  _globals['_FACTREPLY']._serialized_end=130
  _globals['_SUMMER']._serialized_start=132
  _globals['_SUMMER']._serialized_end=215
# @@protoc_insertion_point(module_scope)
