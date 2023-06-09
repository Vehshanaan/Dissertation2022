// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:srv/ApplyForSending.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__APPLY_FOR_SENDING__STRUCT_H_
#define INTERFACES__SRV__DETAIL__APPLY_FOR_SENDING__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'data'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/ApplyForSending in the package interfaces.
typedef struct interfaces__srv__ApplyForSending_Request
{
  /// 申请者编号
  int16_t applicant;
  /// 申请哪个槽
  int16_t apply_slot;
  /// 待发送的数据
  rosidl_runtime_c__String data;
} interfaces__srv__ApplyForSending_Request;

// Struct for a sequence of interfaces__srv__ApplyForSending_Request.
typedef struct interfaces__srv__ApplyForSending_Request__Sequence
{
  interfaces__srv__ApplyForSending_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__ApplyForSending_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/ApplyForSending in the package interfaces.
typedef struct interfaces__srv__ApplyForSending_Response
{
  /// 成功了吗
  bool result;
} interfaces__srv__ApplyForSending_Response;

// Struct for a sequence of interfaces__srv__ApplyForSending_Response.
typedef struct interfaces__srv__ApplyForSending_Response__Sequence
{
  interfaces__srv__ApplyForSending_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__ApplyForSending_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__SRV__DETAIL__APPLY_FOR_SENDING__STRUCT_H_
