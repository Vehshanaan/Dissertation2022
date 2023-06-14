// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/MapVisualiserSiteMoves.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__MAP_VISUALISER_SITE_MOVES__STRUCT_H_
#define INTERFACES__MSG__DETAIL__MAP_VISUALISER_SITE_MOVES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/MapVisualiserSiteMoves in the package interfaces.
/**
  * 移动了的节点的编号
 */
typedef struct interfaces__msg__MapVisualiserSiteMoves
{
  int16_t site_no;
  /// 其坐标
  int16_t x;
  int16_t y;
} interfaces__msg__MapVisualiserSiteMoves;

// Struct for a sequence of interfaces__msg__MapVisualiserSiteMoves.
typedef struct interfaces__msg__MapVisualiserSiteMoves__Sequence
{
  interfaces__msg__MapVisualiserSiteMoves * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__MapVisualiserSiteMoves__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__DETAIL__MAP_VISUALISER_SITE_MOVES__STRUCT_H_
