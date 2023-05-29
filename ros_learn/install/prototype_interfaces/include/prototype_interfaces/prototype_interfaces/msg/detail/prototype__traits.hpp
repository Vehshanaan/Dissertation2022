// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from prototype_interfaces:msg/Prototype.idl
// generated code does not contain a copyright notice

#ifndef PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__TRAITS_HPP_
#define PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "prototype_interfaces/msg/detail/prototype__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'content'
#include "std_msgs/msg/detail/string__traits.hpp"
// Member 'image'
#include "sensor_msgs/msg/detail/image__traits.hpp"

namespace prototype_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Prototype & msg,
  std::ostream & out)
{
  out << "{";
  // member: content
  {
    out << "content: ";
    to_flow_style_yaml(msg.content, out);
    out << ", ";
  }

  // member: image
  {
    out << "image: ";
    to_flow_style_yaml(msg.image, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Prototype & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: content
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "content:\n";
    to_block_style_yaml(msg.content, out, indentation + 2);
  }

  // member: image
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "image:\n";
    to_block_style_yaml(msg.image, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Prototype & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace prototype_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use prototype_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const prototype_interfaces::msg::Prototype & msg,
  std::ostream & out, size_t indentation = 0)
{
  prototype_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use prototype_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const prototype_interfaces::msg::Prototype & msg)
{
  return prototype_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<prototype_interfaces::msg::Prototype>()
{
  return "prototype_interfaces::msg::Prototype";
}

template<>
inline const char * name<prototype_interfaces::msg::Prototype>()
{
  return "prototype_interfaces/msg/Prototype";
}

template<>
struct has_fixed_size<prototype_interfaces::msg::Prototype>
  : std::integral_constant<bool, has_fixed_size<sensor_msgs::msg::Image>::value && has_fixed_size<std_msgs::msg::String>::value> {};

template<>
struct has_bounded_size<prototype_interfaces::msg::Prototype>
  : std::integral_constant<bool, has_bounded_size<sensor_msgs::msg::Image>::value && has_bounded_size<std_msgs::msg::String>::value> {};

template<>
struct is_message<prototype_interfaces::msg::Prototype>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__TRAITS_HPP_
