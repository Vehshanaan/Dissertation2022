// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/MapVisualiserSiteMoves.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__MAP_VISUALISER_SITE_MOVES__TRAITS_HPP_
#define INTERFACES__MSG__DETAIL__MAP_VISUALISER_SITE_MOVES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/msg/detail/map_visualiser_site_moves__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const MapVisualiserSiteMoves & msg,
  std::ostream & out)
{
  out << "{";
  // member: site_no
  {
    out << "site_no: ";
    rosidl_generator_traits::value_to_yaml(msg.site_no, out);
    out << ", ";
  }

  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MapVisualiserSiteMoves & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: site_no
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "site_no: ";
    rosidl_generator_traits::value_to_yaml(msg.site_no, out);
    out << "\n";
  }

  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MapVisualiserSiteMoves & msg, bool use_flow_style = false)
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
  const interfaces::msg::MapVisualiserSiteMoves & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::msg::MapVisualiserSiteMoves & msg)
{
  return interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::msg::MapVisualiserSiteMoves>()
{
  return "interfaces::msg::MapVisualiserSiteMoves";
}

template<>
inline const char * name<interfaces::msg::MapVisualiserSiteMoves>()
{
  return "interfaces/msg/MapVisualiserSiteMoves";
}

template<>
struct has_fixed_size<interfaces::msg::MapVisualiserSiteMoves>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::msg::MapVisualiserSiteMoves>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::msg::MapVisualiserSiteMoves>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__DETAIL__MAP_VISUALISER_SITE_MOVES__TRAITS_HPP_
