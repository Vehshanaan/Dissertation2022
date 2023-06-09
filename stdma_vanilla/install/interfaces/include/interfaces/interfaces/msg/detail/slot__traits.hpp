// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/Slot.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__SLOT__TRAITS_HPP_
#define INTERFACES__MSG__DETAIL__SLOT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/msg/detail/slot__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Slot & msg,
  std::ostream & out)
{
  out << "{";
  // member: slot_no
  {
    out << "slot_no: ";
    rosidl_generator_traits::value_to_yaml(msg.slot_no, out);
    out << ", ";
  }

  // member: slot_total
  {
    out << "slot_total: ";
    rosidl_generator_traits::value_to_yaml(msg.slot_total, out);
    out << ", ";
  }

  // member: sender_no
  {
    out << "sender_no: ";
    rosidl_generator_traits::value_to_yaml(msg.sender_no, out);
    out << ", ";
  }

  // member: occupied
  {
    out << "occupied: ";
    rosidl_generator_traits::value_to_yaml(msg.occupied, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Slot & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: slot_no
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "slot_no: ";
    rosidl_generator_traits::value_to_yaml(msg.slot_no, out);
    out << "\n";
  }

  // member: slot_total
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "slot_total: ";
    rosidl_generator_traits::value_to_yaml(msg.slot_total, out);
    out << "\n";
  }

  // member: sender_no
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sender_no: ";
    rosidl_generator_traits::value_to_yaml(msg.sender_no, out);
    out << "\n";
  }

  // member: occupied
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "occupied: ";
    rosidl_generator_traits::value_to_yaml(msg.occupied, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Slot & msg, bool use_flow_style = false)
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

}  // namespace interfaces

namespace rosidl_generator_traits
{

[[deprecated("use interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces::msg::Slot & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::msg::Slot & msg)
{
  return interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::msg::Slot>()
{
  return "interfaces::msg::Slot";
}

template<>
inline const char * name<interfaces::msg::Slot>()
{
  return "interfaces/msg/Slot";
}

template<>
struct has_fixed_size<interfaces::msg::Slot>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::msg::Slot>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::msg::Slot>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__DETAIL__SLOT__TRAITS_HPP_
