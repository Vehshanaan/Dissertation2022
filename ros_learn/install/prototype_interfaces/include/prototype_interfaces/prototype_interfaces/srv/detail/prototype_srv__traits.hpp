// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from prototype_interfaces:srv/PrototypeSrv.idl
// generated code does not contain a copyright notice

#ifndef PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__TRAITS_HPP_
#define PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "prototype_interfaces/srv/detail/prototype_srv__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace prototype_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const PrototypeSrv_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: name
  {
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << ", ";
  }

  // member: borrow
  {
    out << "borrow: ";
    rosidl_generator_traits::value_to_yaml(msg.borrow, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PrototypeSrv_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << "\n";
  }

  // member: borrow
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "borrow: ";
    rosidl_generator_traits::value_to_yaml(msg.borrow, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PrototypeSrv_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace prototype_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use prototype_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const prototype_interfaces::srv::PrototypeSrv_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  prototype_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use prototype_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const prototype_interfaces::srv::PrototypeSrv_Request & msg)
{
  return prototype_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<prototype_interfaces::srv::PrototypeSrv_Request>()
{
  return "prototype_interfaces::srv::PrototypeSrv_Request";
}

template<>
inline const char * name<prototype_interfaces::srv::PrototypeSrv_Request>()
{
  return "prototype_interfaces/srv/PrototypeSrv_Request";
}

template<>
struct has_fixed_size<prototype_interfaces::srv::PrototypeSrv_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<prototype_interfaces::srv::PrototypeSrv_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<prototype_interfaces::srv::PrototypeSrv_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace prototype_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const PrototypeSrv_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: lend_or_not
  {
    out << "lend_or_not: ";
    rosidl_generator_traits::value_to_yaml(msg.lend_or_not, out);
    out << ", ";
  }

  // member: lend
  {
    out << "lend: ";
    rosidl_generator_traits::value_to_yaml(msg.lend, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PrototypeSrv_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: lend_or_not
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lend_or_not: ";
    rosidl_generator_traits::value_to_yaml(msg.lend_or_not, out);
    out << "\n";
  }

  // member: lend
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lend: ";
    rosidl_generator_traits::value_to_yaml(msg.lend, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PrototypeSrv_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace prototype_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use prototype_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const prototype_interfaces::srv::PrototypeSrv_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  prototype_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use prototype_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const prototype_interfaces::srv::PrototypeSrv_Response & msg)
{
  return prototype_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<prototype_interfaces::srv::PrototypeSrv_Response>()
{
  return "prototype_interfaces::srv::PrototypeSrv_Response";
}

template<>
inline const char * name<prototype_interfaces::srv::PrototypeSrv_Response>()
{
  return "prototype_interfaces/srv/PrototypeSrv_Response";
}

template<>
struct has_fixed_size<prototype_interfaces::srv::PrototypeSrv_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<prototype_interfaces::srv::PrototypeSrv_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<prototype_interfaces::srv::PrototypeSrv_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<prototype_interfaces::srv::PrototypeSrv>()
{
  return "prototype_interfaces::srv::PrototypeSrv";
}

template<>
inline const char * name<prototype_interfaces::srv::PrototypeSrv>()
{
  return "prototype_interfaces/srv/PrototypeSrv";
}

template<>
struct has_fixed_size<prototype_interfaces::srv::PrototypeSrv>
  : std::integral_constant<
    bool,
    has_fixed_size<prototype_interfaces::srv::PrototypeSrv_Request>::value &&
    has_fixed_size<prototype_interfaces::srv::PrototypeSrv_Response>::value
  >
{
};

template<>
struct has_bounded_size<prototype_interfaces::srv::PrototypeSrv>
  : std::integral_constant<
    bool,
    has_bounded_size<prototype_interfaces::srv::PrototypeSrv_Request>::value &&
    has_bounded_size<prototype_interfaces::srv::PrototypeSrv_Response>::value
  >
{
};

template<>
struct is_service<prototype_interfaces::srv::PrototypeSrv>
  : std::true_type
{
};

template<>
struct is_service_request<prototype_interfaces::srv::PrototypeSrv_Request>
  : std::true_type
{
};

template<>
struct is_service_response<prototype_interfaces::srv::PrototypeSrv_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__TRAITS_HPP_
