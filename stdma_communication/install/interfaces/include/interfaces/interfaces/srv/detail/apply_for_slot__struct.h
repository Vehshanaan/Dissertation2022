﻿// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:srv/ApplyForSlot.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__STRUCT_H_
#define INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/ApplyForSlot in the package interfaces.
typedef struct interfaces__srv__ApplyForSlot_Request
{
  /// 申请者编号
  int16_t applicant;
  /// 申请哪个槽
  int16_t apply_slot;
} interfaces__srv__ApplyForSlot_Request;

// Struct for a sequence of interfaces__srv__ApplyForSlot_Request.
typedef struct interfaces__srv__ApplyForSlot_Request__Sequence
{
  interfaces__srv__ApplyForSlot_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__ApplyForSlot_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/ApplyForSlot in the package interfaces.
typedef struct interfaces__srv__ApplyForSlot_Response
{
  /// 成功了吗
  bool result;
} interfaces__srv__ApplyForSlot_Response;

// Struct for a sequence of interfaces__srv__ApplyForSlot_Response.
typedef struct interfaces__srv__ApplyForSlot_Response__Sequence
{
  interfaces__srv__ApplyForSlot_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__ApplyForSlot_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__STRUCT_H_