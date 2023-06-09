// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from prototype_interfaces:srv/PrototypeSrv.idl
// generated code does not contain a copyright notice

#ifndef PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__STRUCT_H_
#define PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/PrototypeSrv in the package prototype_interfaces.
typedef struct prototype_interfaces__srv__PrototypeSrv_Request
{
  /// 借钱者名字
  rosidl_runtime_c__String name;
  /// 想借多少钱
  int32_t borrow;
} prototype_interfaces__srv__PrototypeSrv_Request;

// Struct for a sequence of prototype_interfaces__srv__PrototypeSrv_Request.
typedef struct prototype_interfaces__srv__PrototypeSrv_Request__Sequence
{
  prototype_interfaces__srv__PrototypeSrv_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} prototype_interfaces__srv__PrototypeSrv_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/PrototypeSrv in the package prototype_interfaces.
typedef struct prototype_interfaces__srv__PrototypeSrv_Response
{
  /// 再是服务端返回的结果格式
  /// 借不借？
  bool lend_or_not;
  /// 借多少钱
  int32_t lend;
} prototype_interfaces__srv__PrototypeSrv_Response;

// Struct for a sequence of prototype_interfaces__srv__PrototypeSrv_Response.
typedef struct prototype_interfaces__srv__PrototypeSrv_Response__Sequence
{
  prototype_interfaces__srv__PrototypeSrv_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} prototype_interfaces__srv__PrototypeSrv_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__STRUCT_H_
