// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from prototype_interfaces:srv/PrototypeSrv.idl
// generated code does not contain a copyright notice

#ifndef PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__BUILDER_HPP_
#define PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "prototype_interfaces/srv/detail/prototype_srv__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace prototype_interfaces
{

namespace srv
{

namespace builder
{

class Init_PrototypeSrv_Request_borrow
{
public:
  explicit Init_PrototypeSrv_Request_borrow(::prototype_interfaces::srv::PrototypeSrv_Request & msg)
  : msg_(msg)
  {}
  ::prototype_interfaces::srv::PrototypeSrv_Request borrow(::prototype_interfaces::srv::PrototypeSrv_Request::_borrow_type arg)
  {
    msg_.borrow = std::move(arg);
    return std::move(msg_);
  }

private:
  ::prototype_interfaces::srv::PrototypeSrv_Request msg_;
};

class Init_PrototypeSrv_Request_name
{
public:
  Init_PrototypeSrv_Request_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PrototypeSrv_Request_borrow name(::prototype_interfaces::srv::PrototypeSrv_Request::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_PrototypeSrv_Request_borrow(msg_);
  }

private:
  ::prototype_interfaces::srv::PrototypeSrv_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::prototype_interfaces::srv::PrototypeSrv_Request>()
{
  return prototype_interfaces::srv::builder::Init_PrototypeSrv_Request_name();
}

}  // namespace prototype_interfaces


namespace prototype_interfaces
{

namespace srv
{

namespace builder
{

class Init_PrototypeSrv_Response_lend
{
public:
  explicit Init_PrototypeSrv_Response_lend(::prototype_interfaces::srv::PrototypeSrv_Response & msg)
  : msg_(msg)
  {}
  ::prototype_interfaces::srv::PrototypeSrv_Response lend(::prototype_interfaces::srv::PrototypeSrv_Response::_lend_type arg)
  {
    msg_.lend = std::move(arg);
    return std::move(msg_);
  }

private:
  ::prototype_interfaces::srv::PrototypeSrv_Response msg_;
};

class Init_PrototypeSrv_Response_lend_or_not
{
public:
  Init_PrototypeSrv_Response_lend_or_not()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PrototypeSrv_Response_lend lend_or_not(::prototype_interfaces::srv::PrototypeSrv_Response::_lend_or_not_type arg)
  {
    msg_.lend_or_not = std::move(arg);
    return Init_PrototypeSrv_Response_lend(msg_);
  }

private:
  ::prototype_interfaces::srv::PrototypeSrv_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::prototype_interfaces::srv::PrototypeSrv_Response>()
{
  return prototype_interfaces::srv::builder::Init_PrototypeSrv_Response_lend_or_not();
}

}  // namespace prototype_interfaces

#endif  // PROTOTYPE_INTERFACES__SRV__DETAIL__PROTOTYPE_SRV__BUILDER_HPP_
