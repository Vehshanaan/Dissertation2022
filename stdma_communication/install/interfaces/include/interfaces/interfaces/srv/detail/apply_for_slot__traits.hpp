// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/ApplyForSlot.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__TRAITS_HPP_
#define INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/srv/detail/apply_for_slot__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const ApplyForSlot_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: applicant
  {
    out << "applicant: ";
    rosidl_generator_traits::value_to_yaml(msg.applicant, out);
    out << ", ";
  }

  // member: apply_slot
  {
    out << "apply_slot: ";
    rosidl_generator_traits::value_to_yaml(msg.apply_slot, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ApplyForSlot_Request & msg,
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

  // member: apply_slot
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "apply_slot: ";
    rosidl_generator_traits::value_to_yaml(msg.apply_slot, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ApplyForSlot_Request & msg, bool use_flow_style = false)
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
  const interfaces::srv::ApplyForSlot_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::ApplyForSlot_Request & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::ApplyForSlot_Request>()
{
  return "interfaces::srv::ApplyForSlot_Request";
}

template<>
inline const char * name<interfaces::srv::ApplyForSlot_Request>()
{
  return "interfaces/srv/ApplyForSlot_Request";
}

template<>
struct has_fixed_size<interfaces::srv::ApplyForSlot_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::ApplyForSlot_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::ApplyForSlot_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const ApplyForSlot_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: result
  {
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ApplyForSlot_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ApplyForSlot_Response & msg, bool use_flow_style = false)
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
  const interfaces::srv::ApplyForSlot_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::ApplyForSlot_Response & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::ApplyForSlot_Response>()
{
  return "interfaces::srv::ApplyForSlot_Response";
}

template<>
inline const char * name<interfaces::srv::ApplyForSlot_Response>()
{
  return "interfaces/srv/ApplyForSlot_Response";
}

template<>
struct has_fixed_size<interfaces::srv::ApplyForSlot_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::ApplyForSlot_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::ApplyForSlot_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::ApplyForSlot>()
{
  return "interfaces::srv::ApplyForSlot";
}

template<>
inline const char * name<interfaces::srv::ApplyForSlot>()
{
  return "interfaces/srv/ApplyForSlot";
}

template<>
struct has_fixed_size<interfaces::srv::ApplyForSlot>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::ApplyForSlot_Request>::value &&
    has_fixed_size<interfaces::srv::ApplyForSlot_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::ApplyForSlot>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::ApplyForSlot_Request>::value &&
    has_bounded_size<interfaces::srv::ApplyForSlot_Response>::value
  >
{
};

template<>
struct is_service<interfaces::srv::ApplyForSlot>
  : std::true_type
{
};

template<>
struct is_service_request<interfaces::srv::ApplyForSlot_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interfaces::srv::ApplyForSlot_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__TRAITS_HPP_
