# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: actions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='actions.proto',
  package='kmounter',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ractions.proto\x12\x08kmounter\" \n\rActionMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\"B\n\x06Umount\x12\x12\n\nmount_name\x18\x01 \x01(\t\x12\x15\n\rhome_sym_link\x18\x02 \x01(\t\x12\r\n\x05\x66orce\x18\x03 \x01(\x08\"V\n\x08MountNFS\x12\x12\n\nmount_name\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0f\n\x07options\x18\x03 \x01(\t\x12\x15\n\rhome_sym_link\x18\x04 \x01(\t\"A\n\x05Mount\x12\x0c\n\x04type\x18\x01 \x01(\t\x12!\n\x03nfs\x18\x02 \x01(\x0b\x32\x12.kmounter.MountNFSH\x00\x42\x07\n\x05mount\"D\n\nBackupSync\x12\x1e\n\x05mount\x18\x01 \x01(\x0b\x32\x0f.kmounter.Mount\x12\x16\n\x0etarget_to_sync\x18\x02 \x01(\t\"\"\n\x08StopSync\x12\x16\n\x0etarget_to_sync\x18\x01 \x01(\tb\x06proto3'
)




_ACTIONMESSAGE = _descriptor.Descriptor(
  name='ActionMessage',
  full_name='kmounter.ActionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='kmounter.ActionMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=59,
)


_UMOUNT = _descriptor.Descriptor(
  name='Umount',
  full_name='kmounter.Umount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mount_name', full_name='kmounter.Umount.mount_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='home_sym_link', full_name='kmounter.Umount.home_sym_link', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='force', full_name='kmounter.Umount.force', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=127,
)


_MOUNTNFS = _descriptor.Descriptor(
  name='MountNFS',
  full_name='kmounter.MountNFS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mount_name', full_name='kmounter.MountNFS.mount_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='kmounter.MountNFS.source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='options', full_name='kmounter.MountNFS.options', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='home_sym_link', full_name='kmounter.MountNFS.home_sym_link', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=215,
)


_MOUNT = _descriptor.Descriptor(
  name='Mount',
  full_name='kmounter.Mount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='kmounter.Mount.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nfs', full_name='kmounter.Mount.nfs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='mount', full_name='kmounter.Mount.mount',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=217,
  serialized_end=282,
)


_BACKUPSYNC = _descriptor.Descriptor(
  name='BackupSync',
  full_name='kmounter.BackupSync',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mount', full_name='kmounter.BackupSync.mount', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_to_sync', full_name='kmounter.BackupSync.target_to_sync', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=352,
)


_STOPSYNC = _descriptor.Descriptor(
  name='StopSync',
  full_name='kmounter.StopSync',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_to_sync', full_name='kmounter.StopSync.target_to_sync', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=388,
)

_MOUNT.fields_by_name['nfs'].message_type = _MOUNTNFS
_MOUNT.oneofs_by_name['mount'].fields.append(
  _MOUNT.fields_by_name['nfs'])
_MOUNT.fields_by_name['nfs'].containing_oneof = _MOUNT.oneofs_by_name['mount']
_BACKUPSYNC.fields_by_name['mount'].message_type = _MOUNT
DESCRIPTOR.message_types_by_name['ActionMessage'] = _ACTIONMESSAGE
DESCRIPTOR.message_types_by_name['Umount'] = _UMOUNT
DESCRIPTOR.message_types_by_name['MountNFS'] = _MOUNTNFS
DESCRIPTOR.message_types_by_name['Mount'] = _MOUNT
DESCRIPTOR.message_types_by_name['BackupSync'] = _BACKUPSYNC
DESCRIPTOR.message_types_by_name['StopSync'] = _STOPSYNC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActionMessage = _reflection.GeneratedProtocolMessageType('ActionMessage', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONMESSAGE,
  '__module__' : 'actions_pb2'
  # @@protoc_insertion_point(class_scope:kmounter.ActionMessage)
  })
_sym_db.RegisterMessage(ActionMessage)

Umount = _reflection.GeneratedProtocolMessageType('Umount', (_message.Message,), {
  'DESCRIPTOR' : _UMOUNT,
  '__module__' : 'actions_pb2'
  # @@protoc_insertion_point(class_scope:kmounter.Umount)
  })
_sym_db.RegisterMessage(Umount)

MountNFS = _reflection.GeneratedProtocolMessageType('MountNFS', (_message.Message,), {
  'DESCRIPTOR' : _MOUNTNFS,
  '__module__' : 'actions_pb2'
  # @@protoc_insertion_point(class_scope:kmounter.MountNFS)
  })
_sym_db.RegisterMessage(MountNFS)

Mount = _reflection.GeneratedProtocolMessageType('Mount', (_message.Message,), {
  'DESCRIPTOR' : _MOUNT,
  '__module__' : 'actions_pb2'
  # @@protoc_insertion_point(class_scope:kmounter.Mount)
  })
_sym_db.RegisterMessage(Mount)

BackupSync = _reflection.GeneratedProtocolMessageType('BackupSync', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPSYNC,
  '__module__' : 'actions_pb2'
  # @@protoc_insertion_point(class_scope:kmounter.BackupSync)
  })
_sym_db.RegisterMessage(BackupSync)

StopSync = _reflection.GeneratedProtocolMessageType('StopSync', (_message.Message,), {
  'DESCRIPTOR' : _STOPSYNC,
  '__module__' : 'actions_pb2'
  # @@protoc_insertion_point(class_scope:kmounter.StopSync)
  })
_sym_db.RegisterMessage(StopSync)


# @@protoc_insertion_point(module_scope)
