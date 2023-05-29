// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from prototype_interfaces:msg/Prototype.idl
// generated code does not contain a copyright notice

#ifndef PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__BUILDER_HPP_
#define PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "prototype_interfaces/msg/detail/prototype__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace prototype_interfaces
{

namespace msg
{

namespace builder
{

class Init_Prototype_image
{
public:
  explicit Init_Prototype_image(::prototype_interfaces::msg::Prototype & msg)
  : msg_(msg)
  {}
  ::prototype_interfaces::msg::Prototype image(::prototype_interfaces::msg::Prototype::_image_type arg)
  {
    msg_.image = std::move(arg);
    return std::move(msg_);
  }

private:
  ::prototype_interfaces::msg::Prototype msg_;
};

class Init_Prototype_content
{
public:
  Init_Prototype_content()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Prototype_image content(::prototype_interfaces::msg::Prototype::_content_type arg)
  {
    msg_.content = std::move(arg);
    return Init_Prototype_image(msg_);
  }

private:
  ::prototype_interfaces::msg::Prototype msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::prototype_interfaces::msg::Prototype>()
{
  return prototype_interfaces::msg::builder::Init_Prototype_content();
}

}  // namespace prototype_interfaces

#endif  // PROTOTYPE_INTERFACES__MSG__DETAIL__PROTOTYPE__BUILDER_HPP_
