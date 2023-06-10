// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:srv/MapSending.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MAP_SENDING__STRUCT_H_
#define INTERFACES__SRV__DETAIL__MAP_SENDING__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/MapSending in the package interfaces.
typedef struct interfaces__srv__MapSending_Request
{
  int16_t applicant;
} interfaces__srv__MapSending_Request;

// Struct for a sequence of interfaces__srv__MapSending_Request.
typedef struct interfaces__srv__MapSending_Request__Sequence
{
  interfaces__srv__MapSending_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__MapSending_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'map_data'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/MapSending in the package interfaces.
typedef struct interfaces__srv__MapSending_Response
{
  /// 返回地图数据
  rosidl_runtime_c__int16__Sequence map_data;
} interfaces__srv__MapSending_Response;

// Struct for a sequence of interfaces__srv__MapSending_Response.
typedef struct interfaces__srv__MapSending_Response__Sequence
{
  interfaces__srv__MapSending_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__MapSending_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__SRV__DETAIL__MAP_SENDING__STRUCT_H_
