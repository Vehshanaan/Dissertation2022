// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/MapLocationUpdate.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__TRAITS_HPP_
#define INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/srv/detail/map_location_update__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const MapLocationUpdate_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: applicant
  {
    out << "applicant: ";
    rosidl_generator_traits::value_to_yaml(msg.applicant, out);
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
  const MapLocationUpdate_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: applicant
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "applicant: ";
    rosidl_generator_traits::value_to_yaml(msg.applicant, out);
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

inline std::string to_yaml(const MapLocationUpdate_Request & msg, bool use_flow_style = false)
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

}  // namespace interfaces

namespace rosidl_generator_traits
{

[[deprecated("use interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces::srv::MapLocationUpdate_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::MapLocationUpdate_Request & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::MapLocationUpdate_Request>()
{
  return "interfaces::srv::MapLocationUpdate_Request";
}

template<>
inline const char * name<interfaces::srv::MapLocationUpdate_Request>()
{
  return "interfaces/srv/MapLocationUpdate_Request";
}

template<>
struct has_fixed_size<interfaces::srv::MapLocationUpdate_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::MapLocationUpdate_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::MapLocationUpdate_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const MapLocationUpdate_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MapLocationUpdate_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MapLocationUpdate_Response & msg, bool use_flow_style = false)
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

}  // namespace interfaces

namespace rosidl_generator_traits
{

[[deprecated("use interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces::srv::MapLocationUpdate_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::MapLocationUpdate_Response & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::MapLocationUpdate_Response>()
{
  return "interfaces::srv::MapLocationUpdate_Response";
}

template<>
inline const char * name<interfaces::srv::MapLocationUpdate_Response>()
{
  return "interfaces/srv/MapLocationUpdate_Response";
}

template<>
struct has_fixed_size<interfaces::srv::MapLocationUpdate_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::MapLocationUpdate_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::MapLocationUpdate_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::MapLocationUpdate>()
{
  return "interfaces::srv::MapLocationUpdate";
}

template<>
inline const char * name<interfaces::srv::MapLocationUpdate>()
{
  return "interfaces/srv/MapLocationUpdate";
}

template<>
struct has_fixed_size<interfaces::srv::MapLocationUpdate>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::MapLocationUpdate_Request>::value &&
    has_fixed_size<interfaces::srv::MapLocationUpdate_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::MapLocationUpdate>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::MapLocationUpdate_Request>::value &&
    has_bounded_size<interfaces::srv::MapLocationUpdate_Response>::value
  >
{
};

template<>
struct is_service<interfaces::srv::MapLocationUpdate>
  : std::true_type
{
};

template<>
struct is_service_request<interfaces::srv::MapLocationUpdate_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interfaces::srv::MapLocationUpdate_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__DETAIL__MAP_LOCATION_UPDATE__TRAITS_HPP_
