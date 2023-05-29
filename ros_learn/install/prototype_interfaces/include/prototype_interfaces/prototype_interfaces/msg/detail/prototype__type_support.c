// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from prototype_interfaces:msg/Prototype.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "prototype_interfaces/msg/detail/prototype__rosidl_typesupport_introspection_c.h"
#include "prototype_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "prototype_interfaces/msg/detail/prototype__functions.h"
#include "prototype_interfaces/msg/detail/prototype__struct.h"


// Include directives for member types
// Member `content`
#include "std_msgs/msg/string.h"
// Member `content`
#include "std_msgs/msg/detail/string__rosidl_typesupport_introspection_c.h"
// Member `image`
#include "sensor_msgs/msg/image.h"
// Member `image`
#include "sensor_msgs/msg/detail/image__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  prototype_interfaces__msg__Prototype__init(message_memory);
}

void prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_fini_function(void * message_memory)
{
  prototype_interfaces__msg__Prototype__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_message_member_array[2] = {
  {
    "content",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(prototype_interfaces__msg__Prototype, content),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "image",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(prototype_interfaces__msg__Prototype, image),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_message_members = {
  "prototype_interfaces__msg",  // message namespace
  "Prototype",  // message name
  2,  // number of fields
  sizeof(prototype_interfaces__msg__Prototype),
  prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_message_member_array,  // message members
  prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_init_function,  // function to initialize message memory (memory has to be allocated)
  prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_message_type_support_handle = {
  0,
  &prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_prototype_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, prototype_interfaces, msg, Prototype)() {
  prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, String)();
  prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensor_msgs, msg, Image)();
  if (!prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_message_type_support_handle.typesupport_identifier) {
    prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &prototype_interfaces__msg__Prototype__rosidl_typesupport_introspection_c__Prototype_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
