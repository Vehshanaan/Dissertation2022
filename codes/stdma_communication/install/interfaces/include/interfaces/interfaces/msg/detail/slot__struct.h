// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/Slot.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__SLOT__STRUCT_H_
#define INTERFACES__MSG__DETAIL__SLOT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Slot in the package interfaces.
/**
  * slot数据的格式，采用topic进行此类数据的传输
 */
typedef struct interfaces__msg__Slot
{
  /// 当前slot的编号，从1开始
  int16_t slot_no;
  /// 一帧有多少个slot
  int16_t slot_total;
  /// 当前发送者编号（“node几的那个几”）
  int16_t sender_no;
  /// 此slot是否有主
  bool occupied;
} interfaces__msg__Slot;

// Struct for a sequence of interfaces__msg__Slot.
typedef struct interfaces__msg__Slot__Sequence
{
  interfaces__msg__Slot * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__Slot__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__DETAIL__SLOT__STRUCT_H_
