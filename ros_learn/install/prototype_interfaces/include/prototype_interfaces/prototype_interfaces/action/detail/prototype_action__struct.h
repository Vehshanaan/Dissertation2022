// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from prototype_interfaces:action/PrototypeAction.idl
// generated code does not contain a copyright notice

#ifndef PROTOTYPE_INTERFACES__ACTION__DETAIL__PROTOTYPE_ACTION__STRUCT_H_
#define PROTOTYPE_INTERFACES__ACTION__DETAIL__PROTOTYPE_ACTION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/PrototypeAction in the package prototype_interfaces.
typedef struct prototype_interfaces__action__PrototypeAction_Goal
{
  /// 目标：斐波那契数列的order
  int32_t order;
} prototype_interfaces__action__PrototypeAction_Goal;

// Struct for a sequence of prototype_interfaces__action__PrototypeAction_Goal.
typedef struct prototype_interfaces__action__PrototypeAction_Goal__Sequence
{
  prototype_interfaces__action__PrototypeAction_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} prototype_interfaces__action__PrototypeAction_Goal__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'sequence'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in action/PrototypeAction in the package prototype_interfaces.
typedef struct prototype_interfaces__action__PrototypeAction_Result
{
  /// 结果： 当目标完成时，从服务器向客户端返回执行的结果
  /// 结果：生成的对应order的斐波那契数列
  rosidl_runtime_c__int32__Sequence sequence;
} prototype_interfaces__action__PrototypeAction_Result;

// Struct for a sequence of prototype_interfaces__action__PrototypeAction_Result.
typedef struct prototype_interfaces__action__PrototypeAction_Result__Sequence
{
  prototype_interfaces__action__PrototypeAction_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} prototype_interfaces__action__PrototypeAction_Result__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'partial_sequence'
// already included above
// #include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in action/PrototypeAction in the package prototype_interfaces.
typedef struct prototype_interfaces__action__PrototypeAction_Feedback
{
  /// 反馈：从服务器向客户端定时发送的数据，内容是关于执行任务的过程信息
  /// 反馈： 当前已生成的数列部分
  rosidl_runtime_c__int32__Sequence partial_sequence;
} prototype_interfaces__action__PrototypeAction_Feedback;

// Struct for a sequence of prototype_interfaces__action__PrototypeAction_Feedback.
typedef struct prototype_interfaces__action__PrototypeAction_Feedback__Sequence
{
  prototype_interfaces__action__PrototypeAction_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} prototype_interfaces__action__PrototypeAction_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "prototype_interfaces/action/detail/prototype_action__struct.h"

/// Struct defined in action/PrototypeAction in the package prototype_interfaces.
typedef struct prototype_interfaces__action__PrototypeAction_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  prototype_interfaces__action__PrototypeAction_Goal goal;
} prototype_interfaces__action__PrototypeAction_SendGoal_Request;

// Struct for a sequence of prototype_interfaces__action__PrototypeAction_SendGoal_Request.
typedef struct prototype_interfaces__action__PrototypeAction_SendGoal_Request__Sequence
{
  prototype_interfaces__action__PrototypeAction_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} prototype_interfaces__action__PrototypeAction_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/PrototypeAction in the package prototype_interfaces.
typedef struct prototype_interfaces__action__PrototypeAction_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} prototype_interfaces__action__PrototypeAction_SendGoal_Response;

// Struct for a sequence of prototype_interfaces__action__PrototypeAction_SendGoal_Response.
typedef struct prototype_interfaces__action__PrototypeAction_SendGoal_Response__Sequence
{
  prototype_interfaces__action__PrototypeAction_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} prototype_interfaces__action__PrototypeAction_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/PrototypeAction in the package prototype_interfaces.
typedef struct prototype_interfaces__action__PrototypeAction_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} prototype_interfaces__action__PrototypeAction_GetResult_Request;

// Struct for a sequence of prototype_interfaces__action__PrototypeAction_GetResult_Request.
typedef struct prototype_interfaces__action__PrototypeAction_GetResult_Request__Sequence
{
  prototype_interfaces__action__PrototypeAction_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} prototype_interfaces__action__PrototypeAction_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "prototype_interfaces/action/detail/prototype_action__struct.h"

/// Struct defined in action/PrototypeAction in the package prototype_interfaces.
typedef struct prototype_interfaces__action__PrototypeAction_GetResult_Response
{
  int8_t status;
  prototype_interfaces__action__PrototypeAction_Result result;
} prototype_interfaces__action__PrototypeAction_GetResult_Response;

// Struct for a sequence of prototype_interfaces__action__PrototypeAction_GetResult_Response.
typedef struct prototype_interfaces__action__PrototypeAction_GetResult_Response__Sequence
{
  prototype_interfaces__action__PrototypeAction_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} prototype_interfaces__action__PrototypeAction_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "prototype_interfaces/action/detail/prototype_action__struct.h"

/// Struct defined in action/PrototypeAction in the package prototype_interfaces.
typedef struct prototype_interfaces__action__PrototypeAction_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  prototype_interfaces__action__PrototypeAction_Feedback feedback;
} prototype_interfaces__action__PrototypeAction_FeedbackMessage;

// Struct for a sequence of prototype_interfaces__action__PrototypeAction_FeedbackMessage.
typedef struct prototype_interfaces__action__PrototypeAction_FeedbackMessage__Sequence
{
  prototype_interfaces__action__PrototypeAction_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} prototype_interfaces__action__PrototypeAction_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PROTOTYPE_INTERFACES__ACTION__DETAIL__PROTOTYPE_ACTION__STRUCT_H_
