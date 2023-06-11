// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:srv/MapLocationUpdate.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__STRUCT_H_
#define INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/MapLocationUpdate in the package interfaces.
typedef struct interfaces__srv__MapLocationUpdate_Request
{
  int16_t applicant;
  /// x y是要移动到的坐标位置，左上为0，0
  /// 申请者要移动到的位置 横坐标
  int16_t x;
  /// 申请者要移动到的位置 纵坐标
  int16_t y;
} interfaces__srv__MapLocationUpdate_Request;

// Struct for a sequence of interfaces__srv__MapLocationUpdate_Request.
typedef struct interfaces__srv__MapLocationUpdate_Request__Sequence
{
  interfaces__srv__MapLocationUpdate_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__MapLocationUpdate_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/MapLocationUpdate in the package interfaces.
typedef struct interfaces__srv__MapLocationUpdate_Response
{
  /// 成功了吗
  bool success;
} interfaces__srv__MapLocationUpdate_Response;

// Struct for a sequence of interfaces__srv__MapLocationUpdate_Response.
typedef struct interfaces__srv__MapLocationUpdate_Response__Sequence
{
  interfaces__srv__MapLocationUpdate_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__MapLocationUpdate_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__STRUCT_H_
