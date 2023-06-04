// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/ApplyForSlot.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/apply_for_slot__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_ApplyForSlot_Request_apply_slot
{
public:
  explicit Init_ApplyForSlot_Request_apply_slot(::interfaces::srv::ApplyForSlot_Request & msg)
  : msg_(msg)
  {}
  ::interfaces::srv::ApplyForSlot_Request apply_slot(::interfaces::srv::ApplyForSlot_Request::_apply_slot_type arg)
  {
    msg_.apply_slot = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::ApplyForSlot_Request msg_;
};

class Init_ApplyForSlot_Request_applicant
{
public:
  Init_ApplyForSlot_Request_applicant()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ApplyForSlot_Request_apply_slot applicant(::interfaces::srv::ApplyForSlot_Request::_applicant_type arg)
  {
    msg_.applicant = std::move(arg);
    return Init_ApplyForSlot_Request_apply_slot(msg_);
  }

private:
  ::interfaces::srv::ApplyForSlot_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::ApplyForSlot_Request>()
{
  return interfaces::srv::builder::Init_ApplyForSlot_Request_applicant();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_ApplyForSlot_Response_result
{
public:
  Init_ApplyForSlot_Response_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::ApplyForSlot_Response result(::interfaces::srv::ApplyForSlot_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::ApplyForSlot_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::ApplyForSlot_Response>()
{
  return interfaces::srv::builder::Init_ApplyForSlot_Response_result();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__APPLY_FOR_SLOT__BUILDER_HPP_
