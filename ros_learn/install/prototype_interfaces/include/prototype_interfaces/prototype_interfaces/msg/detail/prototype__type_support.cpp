// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from prototype_interfaces:msg/Prototype.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "prototype_interfaces/msg/detail/prototype__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace prototype_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Prototype_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) prototype_interfaces::msg::Prototype(_init);
}

void Prototype_fini_function(void * message_memory)
{
  auto typed_message = static_cast<prototype_interfaces::msg::Prototype *>(message_memory);
  typed_message->~Prototype();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Prototype_message_member_array[2] = {
  {
    "content",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::String>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(prototype_interfaces::msg::Prototype, content),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "image",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<sensor_msgs::msg::Image>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(prototype_interfaces::msg::Prototype, image),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Prototype_message_members = {
  "prototype_interfaces::msg",  // message namespace
  "Prototype",  // message name
  2,  // number of fields
  sizeof(prototype_interfaces::msg::Prototype),
  Prototype_message_member_array,  // message members
  Prototype_init_function,  // function to initialize message memory (memory has to be allocated)
  Prototype_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Prototype_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Prototype_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace prototype_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<prototype_interfaces::msg::Prototype>()
{
  return &::prototype_interfaces::msg::rosidl_typesupport_introspection_cpp::Prototype_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, prototype_interfaces, msg, Prototype)() {
  return &::prototype_interfaces::msg::rosidl_typesupport_introspection_cpp::Prototype_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
