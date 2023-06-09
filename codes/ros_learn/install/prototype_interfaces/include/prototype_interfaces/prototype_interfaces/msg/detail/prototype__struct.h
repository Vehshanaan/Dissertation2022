// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from prototype_interfaces:msg/Prototype.idl
// generated code does not contain a copyright notice

#ifndef PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__STRUCT_H_
#define PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'content'
#include "std_msgs/msg/detail/string__struct.h"
// Member 'image'
#include "sensor_msgs/msg/detail/image__struct.h"

/// Struct defined in msg/Prototype in the package prototype_interfaces.
/**
  * 在此文件中可以用井号插入注释
 */
typedef struct prototype_interfaces__msg__Prototype
{
  /// 加入一个标准消息接口std_mags 下的string
  std_msgs__msg__String content;
  /// 加入一个Image类型
  sensor_msgs__msg__Image image;
} prototype_interfaces__msg__Prototype;

// Struct for a sequence of prototype_interfaces__msg__Prototype.
typedef struct prototype_interfaces__msg__Prototype__Sequence
{
  prototype_interfaces__msg__Prototype * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} prototype_interfaces__msg__Prototype__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__STRUCT_H_
