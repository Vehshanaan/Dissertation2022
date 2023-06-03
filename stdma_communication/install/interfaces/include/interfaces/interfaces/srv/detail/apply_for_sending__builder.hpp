// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/ApplyForSending.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__APPLY_FOR_SENDING__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__APPLY_FOR_SENDING__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/apply_for_sending__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_ApplyForSending_Request_apply_slot
{
public:
  explicit Init_ApplyForSending_Request_apply_slot(::interfaces::srv::ApplyForSending_Request & msg)
  : msg_(msg)
  {}
  ::interfaces::srv::ApplyForSending_Request apply_slot(::interfaces::srv::ApplyForSending_Request::_apply_slot_type arg)
  {
    msg_.apply_slot = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::ApplyForSending_Request msg_;
};

class Init_ApplyForSending_Request_applicant
{
public:
  Init_ApplyForSending_Request_applicant()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ApplyForSending_Request_apply_slot applicant(::interfaces::srv::ApplyForSending_Request::_applicant_type arg)
  {
    msg_.applicant = std::move(arg);
    return Init_ApplyForSending_Request_apply_slot(msg_);
  }

private:
  ::interfaces::srv::ApplyForSending_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::ApplyForSending_Request>()
{
  return interfaces::srv::builder::Init_ApplyForSending_Request_applicant();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_ApplyForSending_Response_result
{
public:
  Init_ApplyForSending_Response_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::ApplyForSending_Response result(::interfaces::srv::ApplyForSending_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::ApplyForSending_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::ApplyForSending_Response>()
{
  return interfaces::srv::builder::Init_ApplyForSending_Response_result();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__APPLY_FOR_SENDING__BUILDER_HPP_
